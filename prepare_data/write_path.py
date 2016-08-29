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
            dst_folder = os.path.join(dst_root,dataset_name,folder+'.hog')
            line = samples_folder+','+dst_folder+'\n'
            results.append(line)
    return results


if __name__ == '__main__':
    src_root = '/usr0/multicomp/datasets'
    dst_root = '/usr0/home/liangkeg/InMind/FG/data_cnn'
    file_path = '/usr0/home/liangkeg/InMind/FG/data_cnn/data_path.list'
    fw = open(file_path,'wb')

    paths = prepare_Bosphorus(src_root, dst_root)
    write_path(fw, paths)

    fw.close()