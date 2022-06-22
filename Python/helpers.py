# import networkx as nx
# import matplotlib
# graph = nx.Graph()  # NODES ARE EXCLUISIVE
# graph.add_node("tom")
# print(nx.nodes(graph))

import os.path


def save_to_file(filename="demofile"):
    save_path = 'GraphTheory'
    completeName = os.path.join(save_path, filename + ".csv")


def turn_pic_to_hex(filepath="../#UserData/userpic.jpg"):
    with open(filepath, 'rb') as f:
        content = f.read()
    return content


def check_and_save_dir(path):
    isExist = os.path.exists(path)
    # print(isExist)
    if not isExist:
        # Create a new directory because it does not exist
        os.makedirs(path)
        print("The new directory is created:", path)


def turn_hex_to_pic_save(hex_string, username="DEMO-USERNAME"):
    import binascii
    # my_ascii = (binascii.hexlify(hex_string))
    with open(F'../#DemoData/{username}-image.jpg', 'wb') as file:
        file.write(hex_string)


