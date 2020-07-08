import shutil
def save_img(path_of_imgfile,mode=1):
    if mode == 0:
        newpath = shutil.copy(src=path_of_imgfile,dst="searched images")

    elif mode == 1:
        newpath = shutil.move(src=path_of_imgfile, dst="E:/NANDAN/Redmi8 1 backup/WhatsApp/Media/WhatsApp Images/Private/NJ")

    else:
        print("invalid mode entered")
        print("press 0 for copy")
        print("press 1 for move")
    # print(newpath)
# save_img("F:/python/ImageSearch/face_rec/IMG-2019.jpg")

