import os
import shutil
import zipfile
import tempfile
from collections import defaultdict

DEFAULT_FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "PDFs": [".pdf"],
    "Excel": [".xlsx", ".xls"],
    "CSV": [".csv"],
    "Text": [".txt"],
    "Zips": [".zip"]
}

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

    # Save uploads
    for file in uploaded_files:
        if file.name in seen_files:
            duplicates.append(file.name)
            continue

        seen_files.add(file.name)

        file_path = os.path.join(input_dir, file.name)
        with open(file_path, "wb") as f:
            f.write(file.getbuffer())

        _, ext = os.path.splitext(file.name)
        placed = False

        for folder_name, extensions in rules.items():
            if ext.lower() in extensions:
                target_folder = os.path.join(output_dir, folder_name)
                os.makedirs(target_folder, exist_ok=True)
                shutil.copy(file_path, os.path.join(target_folder, file.name))
                summary[folder_name] += 1
                placed = True
                break

        if not placed:
            other_folder = os.path.join(output_dir, "Others")
            os.makedirs(other_folder, exist_ok=True)
            shutil.copy(file_path, os.path.join(other_folder, file.name))
            summary["Others"] += 1

        moved_files.append(file.name)

    # Create ZIP
    zip_path = os.path.join(temp_dir, "organized_files.zip")

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(output_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, output_dir)
                zipf.write(file_path, arcname)

    return zip_path, moved_files, dict(summary), duplicates
