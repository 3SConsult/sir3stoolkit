# This script is AI-generated
# cd ...\sir3stoolkit\docs\source\tutorials before running this script

import os
import re
import zipfile

# Get the current working directory
base_dir = os.getcwd()
print(f"Working directory: {base_dir}")

# Pattern to match directories like TutorialX_Assets where X is an integer or 'X'
pattern = re.compile(r'^Tutorial(\d+|X)_Assets$')

# List all entries in the current directory
entries = os.listdir(base_dir)
print("Directory entries found:")
for entry in entries:
    print(f" - {entry}")

# List to store matched directories
matched_dirs = []

# Create individual zip files for each matching directory
for entry in entries:
    full_path = os.path.join(base_dir, entry)
    if os.path.isdir(full_path) and pattern.match(entry):
        print(f"Matched directory: {entry}")
        matched_dirs.append(entry)
        zip_filename = f"{entry}.zip"
        print(f"Creating zip: {zip_filename}")
        with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, _, files in os.walk(full_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, base_dir)
                    print(f"  Adding file: {arcname}")
                    zipf.write(file_path, arcname)

# Create a combined zip file with all matched directories
if matched_dirs:
    combined_zip_name = "Tutorials000-049_Assets.zip"
    print(f"Creating combined zip: {combined_zip_name}")
    with zipfile.ZipFile(combined_zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for dir_name in matched_dirs:
            dir_path = os.path.join(base_dir, dir_name)
            for root, _, files in os.walk(dir_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, base_dir)
                    print(f"  Adding file to combined zip: {arcname}")
                    zipf.write(file_path, arcname)
else:
    print("No matching directories found.")

print("Zipping complete.")
