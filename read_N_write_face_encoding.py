import face_recognition
import os
import pickle

from get_names_folder_or_img_in_dir import get_folders

training_data_encodings =[]
training_data_labels =[]

face_dataset = get_folders('faces/')
# print(face_dataset)
print('Face sample found for')
# KNOWN_FACES_DIR = 'faces/Nandan'
# # print("loading known faces")

training_data = []
labels =[]

    # print(os.listdir(KNOWN_FACES_DIR))
    # for name in os.listdir(KNOWN_FACES_DIR):

for eachFolder in face_dataset:
    training_data = []
    labels = []
    for eachImg in os.listdir(f"faces/{eachFolder}"):
        if eachImg.endswith(".jpg") or eachImg.endswith(".png") or eachImg.endswith(".jpeg") or eachImg.endswith(".JPG"):
            # print(f"{KNOWN_FACES_DIR}/{name}")
            image = face_recognition.load_image_file(f"faces/{eachFolder}/{eachImg}")
            encoding = face_recognition.face_encodings(image)[0]    #it returna a list ,we provide with an image with single face,hence need not to iterate
            training_data.append(encoding)
            labels.append(eachImg.split(".")[0])
    # print(labels)
    print(eachFolder,'(',len(training_data),')')

    with open(f"faces/{eachFolder}/{eachFolder}.data",mode='wb') as fw:
            pickle.dump(training_data,fw)

    # with open("faces/Nandan/Nandan.data",mode='rb') as fr:
    #         training_data_read = pickle.load(fr)
    # # print("training_data_read ",type(training_data_read))
    # print("Training Faces ",len(training_data_read))
    # for a in training_data_read:
    #     print(type(a))

def get_enconding_faces(target_faces):
    for entry in target_faces:
        with open(f"faces/{entry}/{entry}.data", mode='rb') as fr:
            training_data_read = pickle.load(fr)
        # print('Known faces read for ',entry)
        # print("training_data_read ",type(training_data_read))
        training_data_read_count = len(training_data_read)
        # print("Training Faces found for ",entry,training_data_read_count)

        for x in range(training_data_read_count):
            training_data_labels.append(entry)

        training_data_encodings.extend(training_data_read)
        # print("Training Faces ",len(training_data_encodings))
        # print(training_data_labels)

    return training_data_encodings,training_data_labels

# get_enconding_faces(['Nandan','Rubal'])