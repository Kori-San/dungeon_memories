# > Import
from src.header import *


def walk_os(root):
    # [ Define Root Path to "/sheets" ]
    root_path = str(root) + "/sheets"
    file_list = []
    print("\n> 📜 Files found: ")
    # [ Loop in files of root_path ]
    for path, subdirs, files in os.walk(root_path):
        for name in files:
            # [ Check if file is YML/YAML ]
            if name.endswith('.yml') or name.endswith('.yaml'):
                print("  ↪", path, "+", name)
                # [ Add Subdir to name ]
                if path != root_path:
                    name = path[len(root_path) + 1:] + "/" + name
                # [ Append to File_list ]
                file_list.append(name)
    return file_list


def fetchin(master, root, file_entry, info_tree, stat_tree):
    # [ Check if file is Selected ]
    if file_entry.get() == "Choose a file":
        print("\n> ❌ Choose a file")
        return
    # [ Open YML/YAML File ]
    file = file_entry.get()
    path = root + "/sheets/" + file
    with io.open(path, 'r') as stream:
        data_loaded = yaml.safe_load(stream)
    # [ Load Data ]
    info_key, info_value = load_data("info", data_loaded, info_tree)
    stat_key, stat_value = load_data("stat", data_loaded, stat_tree)
    # [ CLI Log ]
    fetchin_log("Information", file, info_key, info_value)
    fetchin_log("Statistics", file, stat_key, stat_value)
    # [ Center Display ]
    master.eval('tk::PlaceWindow . center')


def load_data(master_key, data_loaded, tree):
    # [ Create Lists to return ]
    key_list = []
    key_value = []
    # [ Append Keys and Values ]
    for key in data_loaded[master_key]:
        key_list.append(key)
        key_value.append(data_loaded[master_key][key])
    # [ Create Column in Tree ]
    create_columns(tree, key_list, key_value)
    # [ Return Lists ]
    return key_list, key_value


def create_columns(tree, key_list, key_value):
    # [ Set Tree Columns to Keys ]
    tree["columns"] = (key_list)
    for key in key_list:
        tree.column(key, anchor=tk.CENTER, width=tree_width)
        tree.heading(key, text=key, anchor=tk.CENTER)
    # [ Refresh Values of Tree ]
    tree.delete(*tree.get_children())
    # [ Insert Values for Keys ]
    tree.insert(parent='', index='end', text='', values=key_value)


def fetchin_log(master_key, file, key_list, key_value):
    # [ Loop into Both files to display Log ]
    print("\n> ✅", master_key, "Loaded from:", file)
    for index in range(0, len(key_list)):
        print("  ↪", key_list[index], ":", key_value[index])
