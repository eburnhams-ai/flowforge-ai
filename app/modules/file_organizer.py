import os
import shutil
import zipfile
import tempfile
from collections import defaultdict

DEFAULT_FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "PDFs": [".pdf"],
    "Excel": [".xlsx", ".xls"],
    "CSV": [".csv"],
    "Text": [".txt", ".md"],
    "Zips": [".zip"],
    "Documents": [".doc", ".docx"],
}


def _safe_join(base_dir, filename):
    return os.path.join(base_dir, os.path.basename(filename))


def organize_uploaded_files(uploaded_files, custom_rules=None):
    temp_dir = tempfile.mkdtemp()
    input_dir = os.path.join(temp_dir, "input")
    output_dir = os.path.join(temp_dir, "organized")

    os.makedirs(input_dir, exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)

    moved_files = []
    summary = defaultdict(int)
    seen_files = set()
    duplicates = []

    rules = custom_rules if custom_rules else DEFAULT_FILE_TYPES

    for uploaded_file in uploaded_files:
        if uploaded_file.name in seen_files:
            duplicates.append(uploaded_file.name)
            continue

        seen_files.add(uploaded_file.name)

        file_path = _safe_join(input_dir, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        _, ext = os.path.splitext(uploaded_file.name)
        ext = ext.lower()
        placed = False

        for folder_name, extensions in rules.items():
            normalized_extensions = [e.lower() for e in extensions]
            if ext in normalized_extensions:
                target_folder = os.path.join(output_dir, folder_name)
                os.makedirs(target_folder, exist_ok=True)
                shutil.copy(file_path, _safe_join(target_folder, uploaded_file.name))
                summary[folder_name] += 1
                placed = True
                break

        if not placed:
            other_folder = os.path.join(output_dir, "Others")
            os.makedirs(other_folder, exist_ok=True)
            shutil.copy(file_path, _safe_join(other_folder, uploaded_file.name))
            summary["Others"] += 1

        moved_files.append(uploaded_file.name)

    zip_path = os.path.join(temp_dir, "organized_files.zip")
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(output_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, output_dir)
                zipf.write(file_path, arcname)

    return zip_path, moved_files, dict(summary), duplicates


def organize_folder(folder_path):
    if not os.path.isdir(folder_path):
        return "Folder does not exist"

    output_dir = os.path.join(folder_path, "Organized")
    os.makedirs(output_dir, exist_ok=True)

    moved_count = 0
    for filename in os.listdir(folder_path):
        source = os.path.join(folder_path, filename)
        if not os.path.isfile(source):
            continue

        _, ext = os.path.splitext(filename)
        ext = ext.lower()
        target_category = "Others"

        for category, extensions in DEFAULT_FILE_TYPES.items():
            if ext in extensions:
                target_category = category
                break

        target_folder = os.path.join(output_dir, target_category)
        os.makedirs(target_folder, exist_ok=True)
        shutil.move(source, os.path.join(target_folder, filename))
        moved_count += 1

    return f"Organization complete. Moved {moved_count} files."
