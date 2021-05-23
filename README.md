# Termite pest identification method based on deep convolution neural network

Code of the paper "Termite pest identification method based on deep convolution neural network".

## Abstract 

Several species of drywood termites, subterranean termites, and fungus-growing termites are major construction, gardening, and agriculture pests, causing extensive economic losses annually worldwide. Because no universal method is available for controlling all termites, correct species identification is crucial for termite management. Despite deep neural network technologies’ promising performance in pest recognition, a method for automatic termite recognition remains lacking. To develop an automated deep learning classifier for termite image recognition suitable for mobile applications, we used smartphones to acquire 18 000 original images each of four termite pest species: Kalotermitidae: Cryptotermes domesticus (Haviland); Rhinotermitidae: Coptotermes formosanus Shiraki and Reticulitermes flaviceps (Oshima); and Termitidae: Odontotermes formosanus (Shiraki). Each original image included multiple individuals, and we applied five image segmentation techniques for capturing individual termites. We used 24 000 individual termite images (4 species × 2 castes × 3 groups × 1000 images) for model development and testing. We implemented a termite classification system by using a deep learning–based model, MobileNetV2. Our models achieved high accuracy scores of 0.947, 0.946, and 0.929 for identifying soldiers, workers, and both castes, respectively, which is not significantly different from human expert performance. When model training images were reduced from 1000 to 200 per termite morphotype, classification accuracy significantly decreased. We further applied image augmentation techniques, including geometrical transformations and intensity transformations, to individual termite images. The results revealed that the same classification accuracy can be achieved by using 1000 augmented images derived from only 200 individual termite images, thus facilitating further model development on the basis of many fewer original images. Our image-based identification system can enable the selection of termite control tools for pest management professionals or homeowners.

## Accuracy and Result Details

| Classifiers        | Experiments | Total testing time (sec) | Accuracy | Average accuracy |
|--------------------|-------------|--------------------------:|----------:|------------------:|
| MobNet-Soldier     |     CV_1    |            33            |   0.963  |       0.947      |
|                    |     CV_2    |            38            |   0.973  |                  |
|                    |     CV_3    |            36            |   0.905  |                  |
| MobNet-Worker      |     CV_1    |            36            |   0.930  |       0.946      |
|                    |     CV_2    |            30            |   0.941  |                  |
|                    |     CV_3    |            35            |   0.968  |                  |
| MobNet-Both-castes |     CV_1    |            243           |   0.919  |       0.93       |
|                    |     CV_2    |            235           |   0.936  |                  |
|                    |     CV_3    |            231           |   0.934  |                  |
| Human-Both castes  |   Expert_1  |           17043          |   0.963  |       0.942      |
|                    |   Expert_2  |           13039          |   0.898  |                  |
|                    |   Expert_3  |           05934          |   0.966  |                  |


## Usage

### For researchers to train and test on Deep Learning Models



#### Requirements

1. CUDA 10
2. torchvision 0.4.1
3. Pytorch 1.3.0
4. python 3.7

#### Training setups

1. Number of epochs: 100
2. Batch size: 64
3. Learning rate: 0.0001

#### Dataset 

1. Categories: *O. formosanus, C. formosanus, R.flaviceps, C. domesticus*.
2. Number of images: 24000 pcs in total.(1000 pcs/Location, 3 Location/Caste, 2 Caste/Category,4 Categories.)

#### Steps

1. Please Clone this repo 
2. Type the following command to pull down the big files.
``` 
git lfs pull
```
3. unzip(tar) the tar/tgz files to see the full content.
```
tar -zxvf images.tgz
tar -zxvf weights.tar.gz
```

### For experts to test manually

Please refer to https://github.com/meow23571379/Termite-Human-testing-version.

There are two versions of images : **original resolution(Windows) and Deep Learning view(Windows_x130)**.

Simply clone that repo and double click the .exe files in Windows_x130 and Windows to start test. 
Be sure to carefully follow popped up instructions.
The visualization tool is in progress and will be pushed to that repo shortly in the future.
For now, to visualize your results please send the files in "answer" or "results" folder that created after your test to me([Bonnie Liu](https://github.com/meow23571379)).




## Details


### Training dataset file name rules

- **[ ] / [Soldier] / [Worker]** : Both Castes / Soldier Only / Worker Only

- **[trainfile] / [valfile] / [testfile]** : training set / validation set / testing set

- **[1] / [2] / [3]** : experiment 1 / experiment 2 / experiment 3

- **[ ] / [sub200] / [200aug]** : 1000 pc / sub-dataset 200pc in each location / 1000pc augmented from 200pc 

For example:

BENCHMARK-LARGE_Ind_testfile_soldier_1.txt  ------ Only Soldier, Testset file of Experiment 1 (Test on Location 1 so there are only Location 1 images)

### weights file name rules

- **[ ] / [Soldier] / [Worker]** : Both Castes / Soldier Only / Worker Only

- **[1] / [2] / [3]** : experiment 1 / experiment 2 / experiment 3

- **[ ] / [sub200] / [200aug]** : 1000 pc / sub-dataset 200pc in each location/ 1000pc augmented from 200pc

- **100_weights.pt** : Trained weights on epoch 100 with pytorch

- **confusion_matrix_100.jpg** : confusion matrix of testing epoch 100

- **[train] / [val] / [test] \_[acc] / [loss] \_E100** : training / validation / testing , accuracy / loss curves on epoch 100. 

For example:

BENCHMARK-LARGE_1_sub800/train_acc_E100.jpg ------ (Both Castes, Experiment 1, trained on subset 800 pc,) training accuracy of epoch 100.



                      
