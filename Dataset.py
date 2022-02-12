# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 20:56:35 2022

@author: Yo Mero
"""

import csv

import pandas as pd
import shutil

path = "G:\\tesina\\Licencias\\CASME2-coding-20190701.xlsx"
df = pd.read_excel(path)
print(df)
print(df['Estimated Emotion'].unique())

labels = ('Emotion', 'Subject', 'ME_Number')

myFile = open('train_data.csv', 'w')
writer = csv.DictWriter(myFile, fieldnames=labels, lineterminator='\n')

positive = ['happiness']
negative = ['disgust']
other = ['surprise']

for i in df.index:
    if positive.count(df['Estimated Emotion'][i]) > 0:
        shutil.copytree('G:\\tesina\\Licencias\\Cropped\\' + str(df['Subject'][i]) + '\\' + str(df['Filename'][i]),
                        'G:\\tesina\\Licencias\\MicroExpressions_Data2\\train\\Happiness\\' + str(
                            df['Subject'][i]) + '\\' + df['Filename'][i])
        writer.writerow({'Emotion': "Happiness", 'Subject': str(df['Subject'][i]), 'ME_Number': str(df['Filename'][i])})
    elif negative.count(df['Estimated Emotion'][i]) > 0:
        shutil.copytree('G:\\tesina\\Licencias\\Cropped\\' + str(df['Subject'][i]) + '\\' + str(df['Filename'][i]),
                        'G:\\tesina\\Licencias\\MicroExpressions_Data2\\train\\Disgust\\' + str(
                            df['Subject'][i]) + '\\' + df['Filename'][i])
        writer.writerow({'Emotion': "Disgust", 'Subject': str(df['Subject'][i]), 'ME_Number': str(df['Filename'][i])})
    else:
        shutil.copytree('G:\\tesina\\Licencias\\Cropped\\' + str(df['Subject'][i]) + '\\' + str(df['Filename'][i]),
                        'G:\\tesina\\Licencias\\MicroExpressions_Data2\\train\\Surprise\\' + str(
                            df['Subject'][i]) + '\\' + str(df['Filename'][i]))
        writer.writerow({'Emotion': "Surprise", 'Subject': str(df['Subject'][i]), 'ME_Number': str(df['Filename'][i])})

myFile.close()