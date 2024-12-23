import os
import json


def folder_to_dict(path):
    result = {"name": os.path.basename(path), "type": "folder", "children": []}
    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        if os.path.isdir(full_path):
            result["children"].append(folder_to_dict(full_path))
        else:
            result["children"].append({"name": item, "type": "file"})
    return result


folder_path = "./"
with open("folder_structure.json", "w") as f:
    json.dump(folder_to_dict(folder_path), f, indent=4)
