# call openface from python
# -rigid  -verbose -fdir "../../image_sequence" -of "./output_features_seq/image_sequence.txt"  -hogalign "./output_features_seq/image_sequence.hog"
import os
from multiprocessing import Pool


def run_cmd(line):
    cmd = '../build/bin/FeatureExtraction -rigid -q -no2Dfp -no3Dfp -noMparams -noPose -noAUs -noGaze'
    splits = line.split(',')
    src_path = splits[0]
    dst_path = splits[1]
    print src_path
    if os.path.isdir(src_path): # the src is images
        command = cmd + ' -fdir '+src_path+' -simalign '+dst_path.rstrip('\n')
    else:
        command = cmd + ' -asvid -f' + src_path + ' -simalign '+ dst_path.rstrip('\n')
    os.system(command)

if __name__ == '__main__':
    pool = Pool(processes=16)
    fr = open('../../data_cnn/data_path.list','rb')
    lines = fr.readlines()
    for line in lines:
        pool.apply_async(run_cmd,args=(line,))
    pool.close()
    pool.join()