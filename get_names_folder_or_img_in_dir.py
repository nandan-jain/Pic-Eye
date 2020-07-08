import os
onlyFolders = []
onlyImages = []
allImagesPath = []

def get_folders(target_path):

    mylist=os.listdir(target_path)
    for f in mylist:
        if '.' not in f:
            onlyFolders.append(f)

    return onlyFolders


# print(get_folders("E:\projects\Learning python"))

def get_img_from_dir(person_name):
    mylist = os.listdir(f"faces/{person_name}")
    for f in mylist:
        if f.endswith(".jpg") or f.endswith(".png") or f.endswith(".jpeg"):
            onlyImages.append(f)

    return onlyImages

# print(get_img_from_dir("Nandan"))

def get_img_from_dir_and_subdir(target_path):
    for root, dirs, files in os.walk(target_path):
        for file in files:
            if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg") or file.endswith(".JPG"):
                #print(root)
                allImagesPath.append(f"{root}\{file}")

    return allImagesPath

# print(get_img_from_dir_and_subdir("F:/NANDAN/Redmi8 1 backup/SHAREit/pictures"))
