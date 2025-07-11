import json
import os
from Commands.constants import CONFIG_FILE


def get_settings():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r", encoding="utf-8") as file:
                real_data = json.load(file)
                return real_data
        except:
            pass


def set_settings(printer, path_dir):
    formated_data = {
        "impressora": printer,
        "path_dir": path_dir
    }

    with open(CONFIG_FILE, "w", encoding="utf-8") as file:
        print("salvando JSON")
        json.dump(formated_data, file, indent=4)
    print(formated_data)

