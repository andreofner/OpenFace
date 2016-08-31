
import os

if __name__ == '__main__':
    data_path = './test.txt'
    labels = {}
    with open(data_path, 'rb') as fr:
        lines = fr.readlines()
        for line in lines:
            splits = line.split(' ')
            if int(splits[1]) in labels:
                labels[int(splits[1])] = labels[int(splits[1])] + 1
            else:
                labels[int(splits[1])] = 1
    print labels