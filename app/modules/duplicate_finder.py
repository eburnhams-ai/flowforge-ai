import csv
import hashlib
import io
from collections import defaultdict


def file_hash(uploaded_file):
    uploaded_file.seek(0)
    hasher = hashlib.sha256()

    while True:
        chunk = uploaded_file.read(8192)
        if not chunk:
            break
        hasher.update(chunk)

    uploaded_file.seek(0)
    return hasher.hexdigest()


def find_duplicates(uploaded_files):
    hashes = defaultdict(list)

    for uploaded_file in uploaded_files:
        digest = file_hash(uploaded_file)
        hashes[digest].append(
            {
                "name": uploaded_file.name,
                "size": len(uploaded_file.getbuffer()),
                "hash": digest,
            }
        )

    duplicate_groups = {
        digest: files for digest, files in hashes.items() if len(files) > 1
    }

    duplicate_count = sum(len(files) - 1 for files in duplicate_groups.values())
    recoverable_space = sum(
        sum(file_info["size"] for file_info in files[1:])
        for files in duplicate_groups.values()
    )

    return duplicate_groups, duplicate_count, recoverable_space


def build_duplicate_report_csv(duplicate_groups):
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["Group", "File Name", "Size Bytes", "SHA-256 Hash"])

    for index, files in enumerate(duplicate_groups.values(), start=1):
        for file_info in files:
            writer.writerow([index, file_info["name"], file_info["size"], file_info["hash"]])

    return output.getvalue()


def format_size(size_bytes):
    size = float(size_bytes)
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} PB"
