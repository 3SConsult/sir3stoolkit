import os
import json
import re

def load_names_to_anonymize(names_file_path):
    with open(names_file_path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def anonymize_text(text, names_to_anonymize):
    for name in names_to_anonymize:
        text = re.sub(rf"\b{name}\b", "aUsername", text, flags=re.IGNORECASE)
    return text

def anonymize_notebook(notebook_path, names_to_anonymize):
    with open(notebook_path, "r", encoding="utf-8") as f:
        notebook = json.load(f)

    modified = False
    replaced_names = set()

    for cell in notebook.get("cells", []):
        # Source (code or markdown)
        if "source" in cell:
            original_source = "".join(cell["source"])
            new_source = anonymize_text(original_source, names_to_anonymize)
            if new_source != original_source:
                cell["source"] = [new_source]
                modified = True
                for name in names_to_anonymize:
                    if re.search(rf"\b{name}\b", original_source, flags=re.IGNORECASE):
                        replaced_names.add(name)

        # Outputs
        if "outputs" in cell:
            for output in cell["outputs"]:
                if "text" in output:
                    original_text = "".join(output["text"])
                    new_text = anonymize_text(original_text, names_to_anonymize)
                    if new_text != original_text:
                        output["text"] = [new_text]
                        modified = True
                        for name in names_to_anonymize:
                            if re.search(rf"\b{name}\b", original_text, flags=re.IGNORECASE):
                                replaced_names.add(name)
                if "data" in output:
                    for key, value in output["data"].items():
                        if isinstance(value, list):
                            new_list = []
                            for item in value:
                                new_item = anonymize_text(item, names_to_anonymize)
                                if new_item != item:
                                    modified = True
                                    for name in names_to_anonymize:
                                        if re.search(rf"\b{name}\b", item, flags=re.IGNORECASE):
                                            replaced_names.add(name)
                                new_list.append(new_item)
                            output["data"][key] = new_list

    if modified:
        with open(notebook_path, "w", encoding="utf-8") as f:
            json.dump(notebook, f, indent=1, ensure_ascii=False)
        return notebook_path, replaced_names
    return None, None

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    names_file_path = os.path.join(script_dir, "names_to_anonymize.txt")

    if not os.path.exists(names_file_path):
        print(f"Names file not found: {names_file_path}")
        return

    names_to_anonymize = load_names_to_anonymize(names_file_path)

    print("Starting anonymization...")
    log = []
    for root, _, files in os.walk(script_dir):
        for file in files:
            if file.endswith(".ipynb"):
                notebook_path = os.path.join(root, file)
                result_path, replaced = anonymize_notebook(notebook_path, names_to_anonymize)
                if result_path:
                    log.append((result_path, sorted(replaced)))

    if log:
        print("\nAnonymization Log:")
        for path, names in log:
            print(f"- {path}: replaced {', '.join(names)}")
    else:
        print("No changes made. All notebooks are already anonymized.")

if __name__ == "__main__":
    main()
