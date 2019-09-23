import re
import glob
import os

paths = '/media/ferdyan/NewDisk/3d_bbox_depth/train_dataset/training/'
save = paths + 'label_2_car/'

pathss = os.path.join(paths, "label_2_convert/")
print("pathss = ", pathss)
path_total = sorted(os.listdir(pathss))
print("path_total = ", path_total)

for name in path_total:
    try:
        print("name = ", name)
        baru = save+name
        buka = pathss+name
        with open(buka, 'r+') as f:
            with open(baru, 'w') as fd:
                for line in f:
                        if line.startswith('Van'):
                            print("van")
                            line = line.replace(line[:line.index(' ')], "Car", 1)
                            fd.write(line)
                        elif line.startswith('Truck'):
                            print("truck")
                            line = line.replace(line[:line.index(' ')], "Car", 1)
                            fd.write(line)
                        else:
                            fd.write(line)
    except IOError as exc:
        if exc.errno != errno.EISDIR:
            raise
