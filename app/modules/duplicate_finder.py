import hashlib
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

        hashes[digest].append({
            "name": uploaded_file.name,
            "size": len(uploaded_file.getbuffer()),
            "hash": digest
        })

    duplicate_groups = {
        h: files
        for h, files in hashes.items()
        if len(files) > 1
    }

    duplicate_count = sum(
        len(files) - 1
        for files in duplicate_groups.values()
    )

    recoverable_space = sum(
        sum(file["size"] for file in files[1:])
        for files in duplicate_groups.values()
    )

    return duplicate_groups, duplicate_count, recoverable_space


def format_size(size):
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024

    return f"{size:.2f} PB"