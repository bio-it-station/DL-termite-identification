# A robust deep learning based classification for the smartphone images of termite pest species

Code of the paper "A robust deep learning based classification for the smartphone images of termite pest species".

## Abstract 

Termites are important urban pests, which cause economic and social impact on
urban communities. An accurate and timely identification of termite species can help build
effective control strategies. However, the termite identification requires expertise and could be
labor-intensive. Despite recent deep neural network technologies have brought promise
performance in pest recognition, the automatic termite recognition has still not been well studied.
Since no off-the-shelf dataset consisting of smartphone-captured termite images was available,
we collected four major termite pest species in various locations in Taiwan and acquired large
number of termite images using a smartphone. In this work, we constructed a dataset with 24,000
individual insect images of four termite species with physically variabilities in termite postures
and conditions. Next, we implemented a termite classification system by using a deep learning
based model, MobileNetV2, which is suitable for mobile vision applications. Our models
achieve high accuracy of 0.947, 0.946, and 0.929 for images of soldier, worker, and both castes,
respectively for classification. The results of present research demonstrate the potential for
classification of termite species automatically and future applications with portable mobile
devices to facilitate the termite pest control management.

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

### For researchers to train

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


### For experts to test

Please refer to https://github.com/meow23571379/Termite-Human-testing-version.

There are two versions of images : original resolution(Windows) and Deep Learning view(Windows_x130).

Simply clone that repo and double click the .exe files in Windows_x130 and Windows to start test. 
Be sure to carefully follow popped up instructions.
The visualization tool is in progress and will be pushed to that repo shortly in the future.
For now, to visualize your results please send the files in "answer" or "results" folder that created after your test to me([Bonnie Liu](https://github.com/meow23571379)).




## Details


### Training dataset files

**[ ] / [Soldier] / [Worker]** : Both Castes / Soldier Only / Worker Only

**[trainfile] / [valfile] / [testfile]** : training set / validation set / testing set

**[1] / [2] / [3]** : experiment 1 / experiment 2 / experiment 3

**[ ] / [sub200] / [200aug]** : 1000 pc / sub-dataset 200pc / 1000pc augmented from 200pc 

For example:

**BENCHMARK-LARGE_Ind_testfile_soldier_1.txt**  ------ Only Soldier, Testset file of Experiment 1 (Test on Location 1 so there are only Location 1 images)

                      
