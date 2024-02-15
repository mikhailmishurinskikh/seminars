import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import argparse

def plot():
    fig, ax = plt.subplots(2, 1, figsize = (16, 9))
    sns.lineplot(
            data = data,
            x = 'День',
            y = 'Сумма',
            hue = 'Категория',
            ax = ax[0])
    ax[0].legend()
    
    sns.barplot(
            data = data,
            x = 'Сумма',
            y = 'Категория',
            orient = 'h',
            estimator = 'sum',
            errorbar = None,
            ax = ax[1])
    plt.show()

parser = argparse.ArgumentParser()
parser.add_argument('month', type=str)
parser.add_argument('year', type=int)
args = parser.parse_args()

if (not (args.year == 2023 and int(args.month) > 5 and int(args.month) < 13)
    and not (args.year, int(args.month)) == (2024, 1)):
    print('No infomation about month')    
else:
    data = pd.read_excel(f'outcome_{args.month}.{args.year}.xlsx')
    data['День'] = [int(x.split()[0]) for x in data['Дата']]
    plot()
