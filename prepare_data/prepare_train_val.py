import os
import glob
import fnmatch
import random
import math

def write_path(fw, paths):
    for path in paths:
        fw.write(path)

def get_ck_label(label):
    if label == 0 or label == 1:
        return label
    elif label >= 3:
        return label - 1

def split_ck():
    image_root = '/usr0/home/liangkeg/InMind/FG/data_cnn/CK+/'
    label_root = '/usr0/multicomp/datasets/CK+/Emotion_labels/Emotion'
    subjects = os.listdir(image_root)
    subject_list = []
    for subject in subjects:
        subject_path = os.path.join(image_root, subject)
        samples = os.listdir(subject_path)
        for sample in samples:
            label_path = os.path.join(label_root, subject, sample)
            if os.path.isdir(label_path) and len(os.listdir(label_path)) > 0:
                subject_list.append(subject)
    subject_list = list(set(subject_list))
    random.seed(4)
    random.shuffle(subject_list)
    train_list = subject_list[:108]
    test_list = subject_list[108:]
    return train_list, test_list

def prepare_ck(split_list):
    image_root = '/usr0/home/liangkeg/InMind/FG/data_cnn/CK+/'
    label_root = '/usr0/multicomp/datasets/CK+/Emotion_labels/Emotion'
    results = []
    subjects = os.listdir(image_root)
    for subject in subjects:
        if subject in split_list:
            subject_path = os.path.join(image_root, subject)
            samples = os.listdir(subject_path)
            for sample in samples:
                label_path = os.path.join(label_root, subject, sample)
                if os.path.isdir(label_path) and len(os.listdir(label_path)) > 0:
                    label_file = os.listdir(label_path)
                    file_path = os.path.join(label_path, label_file[0])
                    with open(file_path, 'rb') as fr:
                        labels = fr.readlines()
                        raw_label = int(float(labels[0].strip()))
                        if raw_label == 2:
                            continue
                        label = get_ck_label(raw_label)
                        images = glob.glob(os.path.join(image_root, subject, sample,'*.png'))
                        line = images[0]+' '+str(label)+'\n'
                        results.append(line)
                        line = images[0]+' '+str(label)+'\n'
                        results.append(line)
    return results


def split_bu3dfe():
    src_root = '/usr0/home/liangkeg/InMind/FG/data_cnn/BU_3DFE/'
    folders = os.listdir(src_root)
    subject_list = []
    for folder in folders:
        folder_path = os.path.join(src_root, folder)
        if os.path.isdir(folder_path):
            subject_list.append(folder)
    subject_list = list(set(subject_list))
    random.seed(4)
    random.shuffle(subject_list)
    
    train_list = subject_list[:91]
    test_list = subject_list[91:]
    return train_list,test_list

def get_bu3dfe_label(image_path):
    label = ''
    splits = image_path.split('/')
    label_name = splits[-1].split('_')[1][0:2]
    intensity = int(splits[-1].split('_')[1][2:4])
    if label_name != 'NE' and intensity == 4:
        label = label_name
    elif label_name == 'NE':
        label = label_name
    return label


def prepare_bu3dfe(split_list):
    src_root = '/usr0/home/liangkeg/InMind/FG/data_cnn/BU_3DFE/'
    results = []
    labels = {}
    labels['NE'] = 0
    labels['AN'] = 1
    labels['DI'] = 2
    labels['FE'] = 3
    labels['HA'] = 4
    labels['SA'] = 5
    labels['SU'] = 6

    folders = os.listdir(src_root)
    for folder in folders:
        if folder in split_list:
            folder_path = os.path.join(src_root, folder)
            if os.path.isdir(folder_path):
                images = os.listdir(folder_path)
                for image in images:
                    if fnmatch.fnmatch(image, '*_F2D.bmp'):
                        image_path = os.path.join(folder_path, image)
                        label = get_bu3dfe_label(image_path)
                        if label != '':
                            line = image_path + ' '+ str(labels[label])+'\n'
                            results.append(line)
    return results

def split_bu4dfe():
    src_root = '/usr0/home/liangkeg/InMind/FG/data_cnn/BU_4DFE'
    folders = os.listdir(src_root)
    random.seed(4)
    random.shuffle(folders)
    train_list = folders[:91]
    test_list = folders[91:]
    return train_list, test_list

def prepare_bu4dfe(split_list):
    src_root = '/usr0/home/liangkeg/InMind/FG/data_cnn/BU_4DFE'
    results = []
    labels = {}
    labels['Angry'] = 1
    labels['Disgust'] = 2
    labels['Fear'] = 3
    labels['Happy'] = 4
    labels['Sad'] = 5
    labels['Surprise'] = 6

    folders = os.listdir(src_root)
    for folder in folders:
        if folder in split_list:
            subject_path = os.path.join(src_root, folder)
            if os.path.isdir(subject_path) and ('F0' in folder or 'M0' in folder):
                classes = os.listdir(subject_path)
                for label in classes:
                    samples_path = os.path.join(subject_path, label)
                    samples = glob.glob(os.path.join(samples_path, '*.jpg'))
                    num_samples = len(samples)
                    sample_index = int(math.floor(num_samples / 2))
                    line = samples[sample_index] + ' '+ str(labels[label])+'\n'
                    results.append(line)
    return results

if __name__ == '__main__':
    train_file_path = './train.txt'
    test_file_path = './test.txt'

    fw_train = open(train_file_path, 'wb')
    fw_test = open(test_file_path, 'wb')

    ck_train_list, ck_test_list = split_ck()
    ck_train_paths = prepare_ck(ck_train_list)
    write_path(fw_train, ck_train_paths)
    ck_test_paths = prepare_ck(ck_test_list)
    print len(ck_test_paths)
    write_path(fw_test, ck_test_paths)


    bu3dfe_train_list, bu3dfe_test_list = split_bu3dfe()
    bu3dfe_train_paths = prepare_bu3dfe(bu3dfe_train_list)
    write_path(fw_train, bu3dfe_train_paths)
    bu3dfe_test_paths = prepare_bu3dfe(bu3dfe_test_list)
    print len(bu3dfe_test_paths)
    write_path(fw_test, bu3dfe_test_paths)

    bu4dfe_train_list, bu4dfe_test_list = split_bu4dfe()
    bu4dfe_train_paths = prepare_bu4dfe(bu4dfe_train_list)
    write_path(fw_train, bu4dfe_train_paths)
    bu4dfe_test_paths = prepare_bu4dfe(bu4dfe_test_list)
    print len(bu4dfe_test_paths)
    write_path(fw_test, bu4dfe_test_paths)

