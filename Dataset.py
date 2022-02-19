# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 20:56:35 2022

@author: Yo Mero
"""

import csv
import pandas as pd
import shutil
import matplotlib.pyplot as plt

path = "G:\\tesina\\Licencias\\CASME2-coding-20190701.xlsx"
df = pd.read_excel(path)
print(df)
print(df['Estimated Emotion'].unique())

labels = ('Emotion', 'Subject', 'ME_Number')

myFile = open('train_data.csv', 'w')
writer = csv.DictWriter(myFile, fieldnames=labels, lineterminator='\n')
myFile2 = open('val_data.csv', 'w')
writer2 = csv.DictWriter(myFile2, fieldnames=labels, lineterminator='\n')

allEmotions = ['happiness', 'disgust', 'surprise']
positive = ['happiness']
negative = ['disgust']
other = ['surprise']
emotionCount = {'happiness': 0, 'disgust': 0, 'surprise': 0}
emotionAddedCount = {'happiness': 0, 'disgust': 0, 'surprise': 0}

for i in df.index:
    if allEmotions.count(df['Estimated Emotion'][i]) > 0:
        emotionCount[df['Estimated Emotion'][i]] += 1

print(emotionCount)
plt.bar(allEmotions, emotionCount.values())

# Legenda en el eje y
plt.ylabel('Number of samples')

# Legenda en el eje x
plt.xlabel('Emotions')

# Título de Gráfica
plt.title('Number of samples per emotion')

# Mostramos Gráfica
plt.show()
plt.close()
for name in allEmotions:
    emotionCount[name] = round(emotionCount[name]*.8)

for i in df.index:
    emo = df['Estimated Emotion'][i]
    if allEmotions.count(emo) > 0:
        if emotionAddedCount[emo] < emotionCount[emo]:
            shutil.copytree('G:\\tesina\\Licencias\\Cropped\\' + str(df['Subject'][i]) + '\\' + str(df['Filename'][i]),
                            'G:\\tesina\\Licencias\\MicroExpressions_Data2\\train\\'+emo+'\\' + str(
                                df['Subject'][i]) + '\\' + df['Filename'][i])
            writer.writerow({'Emotion': emo, 'Subject': str(df['Subject'][i]), 'ME_Number': str(df['Filename'][i])})
            emotionAddedCount[emo] += 1
        else:
            shutil.copytree('G:\\tesina\\Licencias\\Cropped\\' + str(df['Subject'][i]) + '\\' + str(df['Filename'][i]),
                            'G:\\tesina\\Licencias\\MicroExpressions_Data2\\val\\'+emo+'\\' + str(
                                df['Subject'][i]) + '\\' + df['Filename'][i])
            writer2.writerow(
                {'Emotion': emo, 'Subject': str(df['Subject'][i]), 'ME_Number': str(df['Filename'][i])})



plt.bar(allEmotions, emotionCount.values())

# Legenda en el eje y
plt.ylabel('Number of samples')

# Legenda en el eje x
plt.xlabel('Emotions')

# Título de Gráfica
plt.title('Number of samples per emotion')

# Mostramos Gráfica
plt.show()
plt.close()

print(emotionCount)
myFile.close()
myFile2.close()