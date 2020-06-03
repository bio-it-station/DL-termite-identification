from random import shuffle
import glob
import sys
import cv2
import numpy as np
#import skimage.io as io


train_addrs = []
train_labels = []
val_addrs = []
val_labels = []
test_addrs = []
test_labels=[]
name = ["台灣土白蟻兵蟻", "台灣土白蟻工蟻", "台灣家白蟻兵蟻", "台灣家白蟻工蟻","截頭堆沙兵蟻", "截頭堆沙工蟻", "黃肢散兵蟻",   "黃肢散工蟻"]
location = ["L1", "L2", "L3"]
for n in name:
    for l in location:
        cat_dog_train_path = '/home/jimmy/Bitsstor03/Termite/individual/BENCHMARK/{}/{}/*.jpg'.format(n, l)
        # read addresses and labels from the 'train' folder
        ADDRS = glob.glob(cat_dog_train_path)
#         print(ADDRS)
        labels0 = []
        labels1 = []
        labels2 = []
        labels3 = []
        labels4 = []
        labels5 = []
        labels6 = []
        labels7 = []
        addrs0 = []
        addrs1 = []
        addrs2 = []
        addrs3 = []
        addrs4 = []
        addrs5 = []
        addrs6 = []
        addrs7 = []

        count = [0] * 8
        for addr in ADDRS:
            if '台灣土白蟻兵蟻' in addr:
                labels0.append(0)
                addrs0.append(addr)
                count[0] = count[0] + 1
            elif '台灣土白蟻工蟻' in addr:
                labels1.append(1)
                addrs1.append(addr)
                count[1] = count[1] + 1
            elif '台灣家白蟻兵蟻' in addr:
                labels2.append(2)
                addrs2.append(addr)
                count[2] = count[2] + 1
            elif '台灣家白蟻工蟻' in addr:
                labels3.append(3)
                addrs3.append(addr)
                count[3] = count[3] + 1
            elif '截頭堆沙兵蟻' in addr:
                labels4.append(4)
                addrs4.append(addr)
                count[4] = count[4] + 1
            elif '截頭堆沙工蟻' in addr:
                labels5.append(5)
                addrs5.append(addr)
                count[5] = count[5] + 1
            elif '黃肢散兵蟻' in addr:
                labels6.append(6)
                addrs6.append(addr)
                count[6] = count[6] + 1
            elif '黃肢散工蟻' in addr:
                labels7.append(7)
                addrs7.append(addr)
                count[7] = count[7] + 1
        labels = [labels0, labels1, labels2, labels3, labels4, labels5, labels6, labels7]
        addrs = [addrs0, addrs1, addrs2, addrs3, addrs4, addrs5, addrs6, addrs7]
        print(n, l, count)


        for i in labels:
            i.sort()



        for i in addrs:
        #     print(i[0])
            total = len(i)
            train_addrs.extend(i[0:int(total*0.6)])
            val_addrs.extend(i[int(total*0.6):int(total*0.8)])
            test_addrs.extend(i[int(0.8*total):total])

        for i in labels:
            train_addrs.extend(i[0:int(total*0.8)])
            val_addrs.extend(i[int(total*0.6):int(total*0.8)])
            test_addrs.extend(i[int(0.8*total):total])
        
        

        print("train: ", len(train_addrs))
        print("validation: ", len(val_addrs))
        print("test: ", len(test_addrs))

        
print(train_addrs)
print(val_addrs)
print(test_addrs)
filename = "/home/ytliu/Termite-Bonnie/PAPER_termite/Ind_trainfile_ALL.txt"
# Open the file with writing permission
myfile = open(filename, 'w')
for lines in zip(train_addrs, train_labels):
    # Write a line to the file
    myfile.write("{} {}\n".format(lines[0], lines[1]))
# Close the file
myfile.close()

filename = "/home/ytliu/Termite-Bonnie/PAPER_termite/Ind_valfile_ALL.txt"
# Open the file with writing permission
myfile = open(filename, 'w')
for lines in zip(val_addrs, val_labels):
    # Write a line to the file
    myfile.write("{} {}\n".format(lines[0], lines[1]))
# Close the file
myfile.close()

filename = "/home/ytliu/Termite-Bonnie/PAPER_termite/Ind_testfile_ALL.txt"
# Open the file with writing permission
myfile = open(filename, 'w')
for lines in zip(test_addrs, test_labels):
    # Write a line to the file
    myfile.write("{} {}\n".format(lines[0], lines[1]))
# Close the file
myfile.close()
