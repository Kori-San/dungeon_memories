# > Import
#   ↪ Custom Functions
from src.header import *
from src.data_func import *


def init_window(root):
    # [ Create Master ]
    master = tk.Tk()
    adjust_master(master)
    # [ Create && pack() Tk.objects ]
    file_entry = choice_box(master, root)
    tk.Button(master, text="Set", command=lambda: fetchin(
        master, root, file_entry, info_tree, stat_tree)).pack()
    #   ↪ Set Tree to selected File values
    # [ TreeView ]
    info_tree = ttk.Treeview(height=tree_height)
    stat_tree = ttk.Treeview(height=tree_height)
    tree_list = [("Informations", info_tree), ("Statistics", stat_tree)]
    init_trees(master, tree_list)
    # [ Launch Loop ]
    tk.mainloop()


def adjust_master(master):
    # [ Adjust Master ]
    master.title("Dungeon Memories")
    master.eval('tk::PlaceWindow . center')  # Center Window


def choice_box(master, root):
    tk.Label(master, text="Sheet").pack()
    # [ Set File Var ]
    file_var = tk.StringVar(master)
    file_var.set("Choose a file")
    #   ↪ Default Value
    file_entry = tk.Entry(master, textvariable=file_var)
    # [ Create and pack() Choice Box ]
    tk.OptionMenu(master, file_var, *walk_os(root)).pack()
    #   ↪ Choice Box
    return file_entry


def init_trees(master, tree_list):
    #   ↪ Tree_List = [(Label_1, Tree_1), ... , (Label_n, Tree_n)]
    for label, tree in tree_list:
        # [ Create && pack() Label ]
        tk.Label(master, text=label).pack()
        # [ Set Common Settings ]
        tree.column("#0", width=0,  stretch=tk.NO)
        tree.heading("#0", text="", anchor=tk.CENTER)
        # [ pack() && create default columns ]
        tree.pack()
        create_columns(tree, ['No Value'], ['None'])
