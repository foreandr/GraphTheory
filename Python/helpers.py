import os.path

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def print_green(string):
    print(bcolors.OKGREEN + str(string) + bcolors.ENDC)


def print_title(string):
    print(bcolors.HEADER + bcolors.UNDERLINE + str(string) + bcolors.ENDC)


def print_error(string):
    print(bcolors.FAIL + str(string) + bcolors.ENDC)

def print_warning(string):
    print(bcolors.WARNING + str(string) + bcolors.ENDC)


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


def get_filetype(string):
    txt = string[::-1]
    my_text = txt.split(".")[0]
    return my_text[::-1]
