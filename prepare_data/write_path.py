import os

def write_path(fw, paths):
    for path in paths:
        fw.write(path)

def prepare_Bosphorus(src_root, dst_root):
    print 'Prepare Bosphorus dataset'
    dataset_name = 'Bosphorus'
    dst_folder = os.path.join(dst_root,dataset_name)
    if not os.path.exists(dst_folder):
        os.makedirs(dst_folder)
    results = []
    data_folder = os.path.join(src_root,dataset_name,'BosphorusDB/BosphorusDB')
    folders = os.listdir(data_folder)
    for folder in folders:
        samples_folder = os.path.join(data_folder, folder)
        if os.path.isdir(samples_folder):
            dst_folder = os.path.join(dst_root,dataset_name,folder)
            line = samples_folder+','+dst_folder+'\n'
            results.append(line)
    return results

# BU_3DFE
def prepare_bu_3dfe(src_root, dst_root):
    print 'Prepare BU_3DFE dataset'
    dataset_name = 'BU_3DFE'
    dst_folder = os.path.join(dst_root, dataset_name)
    if not os.path.exists(dst_folder):
        os.makedirs(dst_folder)
    results = []
    data_folder = os.path.join(src_root, dataset_name)
    folders = os.listdir(data_folder)
    print data_folder
    for folder in folders:
        samples_path = os.path.join(data_folder,folder)
        if os.path.isdir(samples_path):
            dst_path = os.path.join(dst_folder, folder)
            line = samples_path+','+dst_path+'\n'
            # print line
            results.append(line)
    return results

# BU_4DFE
def prepare_bu_4dfe(src_root, dst_root):
    print 'Prepare BU_4DFE dataset'
    dataset_name = 'BU_4DFE'
    dst_folder = os.path.join(dst_root, dataset_name)
    if not os.path.exists(dst_folder):
        os.makedirs(dst_folder)
    results = []
    dataset_path = os.path.join(src_root, dataset_name)
    samples_folder = os.listdir(dataset_path)
    for sample_folder in samples_folder:
        sample_path = os.path.join(dataset_path,sample_folder)
        if os.path.isdir(sample_path):
            subsamples_folder = os.listdir(sample_path)
            for subsample in subsamples_folder:
                src_path = os.path.join(sample_path,subsample)
                dst_dir = os.path.join(dst_folder,sample_folder)
                if not os.path.exists(dst_dir):
                    os.makedirs(dst_dir)
                dst_path = os.path.join(dst_dir,subsample)
                line = src_path+','+dst_path+'\n'
                results.append(line)
    return results

# CK+
def prepare_ck(src_root, dst_root):
    print 'Prepare CK+ dataset'
    dataset_name = 'CK+'
    dst_folder = os.path.join(dst_root, dataset_name)
    if not os.path.exists(dst_folder):
        os.makedirs(dst_folder)
    results = []
    dataset_path = os.path.join(src_root, dataset_name,'extended-cohn-kanade-images/cohn-kanade-images')
    subjects_folder = os.listdir(dataset_path)
    for subject_folder in subjects_folder:
        subject_path = os.path.join(dataset_path, subject_folder)
        samples = os.listdir(subject_path)
        for sample in samples:
            src_path = os.path.join(subject_path, sample)
            dst_path = os.path.join(dst_folder,subject_folder,sample)
            if os.path.isdir(src_path):
                line = src_path+','+dst_path+'\n'
                results.append(line)
    return results





if __name__ == '__main__':
    src_root = '/usr0/multicomp/datasets'
    dst_root = '/usr0/home/liangkeg/InMind/FG/data_cnn'
    file_path = '/usr0/home/liangkeg/InMind/FG/data_cnn/data_path.list'
    fw = open(file_path,'wb')

    # paths = prepare_Bosphorus(src_root, dst_root)
    # write_path(fw, paths)

    paths = prepare_bu_3dfe(src_root, dst_root)
    write_path(fw, paths)

    paths = prepare_bu_4dfe(src_root, dst_root)
    write_path(fw, paths)

    paths = prepare_ck(src_root, dst_root)
    write_path(fw, paths)

    fw.close()