from get_names_folder_or_img_in_dir import get_folders,get_img_from_dir_and_subdir
from read_N_write_face_encoding import get_enconding_faces
from copy_required_images import save_img
from resizing import ResizeWithAspectRatio

import face_recognition
import cv2
import os

user_input1=input('Enter name or names ')
target_faces = user_input1.split(" ")

# print(target_faces)
print('Loading dataset')
face_dataset = get_folders("faces/")
# print(face_dataset)
# for entry in target_faces:
#     if entry in face_dataset:
#         print('Face dataset found for ',entry)
#
#     else:
#         print('Face dataset not found for ',entry)

'''Load face_encoding for target faces'''
loaded_face_encodings,loaded_face_labels = get_enconding_faces(target_faces)


user_input2=input("Enter path ")
target_path=user_input2.replace(os.sep,'/')
print(target_path)
print('Loading images from directory and subdirectory')

list_of_imagesPath = get_img_from_dir_and_subdir(target_path)
print('No. of Images found ',len(list_of_imagesPath))

print('Recognising Faces in Images')
for imgfile in list_of_imagesPath:
    image = face_recognition.load_image_file(imgfile)

    locations = face_recognition.face_locations(image)
    print(locations)

    if len(locations) <= len(target_faces):
        continue

    encodings = face_recognition.face_encodings(image, locations)

    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    print(imgfile)
    recognised_face_count = 0

    for face_encoding , face_location in zip(encodings,locations):
        results = face_recognition.compare_faces(known_face_encodings=loaded_face_encodings,face_encoding_to_check=face_encoding,tolerance=0.5)
        # print(results)
        # print(results.index(True))


        if True in results:
            recognised_face_count+=1
            face_text = loaded_face_labels[results.index(True)]

        else:
            face_text  = "Unknown"


        top_left = (face_location[3] , face_location[0])
        bottom_right = (face_location[1], face_location[2])
        cv2.rectangle(image,top_left,bottom_right,(255,195,77), 2)

        top_left = (face_location[3], face_location[2])
        bottom_right = (face_location[1], face_location[2]+22)
        cv2.rectangle(image, top_left, bottom_right, (255, 195, 77), cv2.FILLED)

        cv2.putText(image,face_text,(face_location[3]+10, face_location[2]+15),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),2)


    if recognised_face_count == len(target_faces):
        ResizeWithAspectRatio(image,width=800)
        cv2.imshow("filename", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        save_img(imgfile)

