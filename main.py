import pandas as pd
import os
import xlrd
import openpyxl
print('\nTask 1\n-----------------------------')
data = ''
with open('data/input (3).txt', 'r') as file:
    for line in file:
        x = 0
        line = " ".join(line.split()).split()
        for number in line:
            x += int(number)
        data = data + str(x) + ' '
    data = data[:-1]
print(data)
print('\nTask 2\n---------------------------')
num_lines = 0
with open('data/input (2).txt', 'r') as file:
    for line in file:
        text = ''
        num_lines += 1
        if (num_lines - 1) % 2 == 0:
            row = line.split()
            for i in row:
                text = text + i[::-1] + ' '
            print(text[:-1])
        else:
            print(line, end='')
print('\nTask 3\n----------------------------')
num_lines = 0
letters = 0
words = 0
with open('data/input (5).txt', 'r') as file:
    for line in file:
        num_lines += 1
        split_string = line.split()
        words += len(split_string)
        for word in split_string:
            for i in word:
                if i.isalpha() is True:
                    letters += 1
print(f'Input file contains: {letters} letters, {words} words, {num_lines} lines')
print('\nTask 4\n---------------------')
data = pd.read_csv('data/input (1).csv', delimiter=';')
minimal = (data.select_dtypes(include=['int64']).min().min())
selected = data.select_dtypes(include=['int64']).min()
print(selected.where(selected == minimal).dropna().to_string())
print('\nTask 5\n-------------------------')
flag = True
list_of_files = os.listdir('data/rogaikopyta/')
for file in list_of_files:
    file = 'data/rogaikopyta/' + file
    df = pd.read_excel(file)
    df.columns = ['Рассчётный лист','ФИО', 'Начислено', 'Сумма']
    df = df.drop(index = 1, columns=['Рассчётный лист', 'Начислено'])
    if flag == True:
        dataframe = df
        flag = False
    else:
        dataframe = dataframe.append(df, ignore_index=True)
dataframe = dataframe.sort_values('ФИО')
print(dataframe)
print('\nTask 6\n-------------------------')
df = pd.read_excel('data/salaries.xlsx')
df.rename(columns={'Unnamed: 0' : 'Город'}, inplace=True)
y = df.median(axis=1, numeric_only=True)
print(df['Город'][y.idxmax()] + ': ' + str(y.max()))
x = df.median(axis=0, numeric_only=True)
print(x.idxmax() + ': ' + str(x.max()))

