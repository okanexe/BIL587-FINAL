import numpy as np
import pandas as pd 
from PIL import Image
from tqdm import tqdm
import os

TRAIN_NUMBER = 28709

# convert string to integer
def atoi(s):
    n = 0
    for i in s:
        n = n*10 + ord(i) - ord("0")
    return n

def save(img, train_or_test, name, i):
    img.save('../data/{}/{}/im'.format(train_or_test, name)+str(i)+'.png')
    i += 1

outer_names = ['test','train']
inner_names = ['angry', 'disgusted', 'fearful', 'happy', 'sad', 'surprised', 'neutral']
os.makedirs('data', exist_ok=True)
for outer_name in outer_names:
    os.makedirs(os.path.join('data',outer_name), exist_ok=True)
    for inner_name in inner_names:
        os.makedirs(os.path.join('data',outer_name,inner_name), exist_ok=True)

angry = 0
disgusted = 0
fearful = 0
happy = 0
sad = 0
surprised = 0
neutral = 0
angry_test = 0
disgusted_test = 0
fearful_test = 0
happy_test = 0
sad_test = 0
surprised_test = 0
neutral_test = 0

df = pd.read_csv('../data/fer2013.csv')
matrix = np.zeros((48,48),dtype=np.uint8)
print("Saving images...")

# read the csv file line by line
for i in tqdm(range(len(df))):
    txt = df['pixels'][i]
    words = txt.split()

    # the image size is 48x48
    for j in range(2304):
        xind = j // 48
        yind = j % 48
        matrix[xind][yind] = atoi(words[j])
    img = Image.fromarray(matrix)

    # train
    if i < TRAIN_NUMBER:
        if df['emotion'][i] == 0:
            save(img, 'train', 'angry', angry)
        elif df['emotion'][i] == 1:
            save(img, 'train', 'disgusted', disgusted)
        elif df['emotion'][i] == 2:
            save(img, 'train', 'fearful', fearful)
        elif df['emotion'][i] == 3:
            save(img, 'train', 'happy', happy)
        elif df['emotion'][i] == 4:
            save(img, 'train', 'sad', sad)
        elif df['emotion'][i] == 5:
            save(img, 'train', 'surprised', surprised)
        elif df['emotion'][i] == 6:
            save(img, 'train', 'neutral', neutral)
    # test
    else:
        if df['emotion'][i] == 0:
            save(img, 'test', 'angry', angry_test)
        elif df['emotion'][i] == 1:
            save(img, 'test', 'disgusted', disgusted_test)
        elif df['emotion'][i] == 2:
            save(img, 'test', 'fearful', fearful_test)
        elif df['emotion'][i] == 3:
            save(img, 'test', 'happy', happy_test)
        elif df['emotion'][i] == 4:
            save(img, 'test', 'sad', sad_test)
        elif df['emotion'][i] == 5:
            save(img, 'test', 'surprised', surprised_test)
        elif df['emotion'][i] == 6:
            save(img, 'test', 'neutral', neutral_test)