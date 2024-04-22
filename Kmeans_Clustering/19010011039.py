# 19010011039 Ahmet Emin Kazan
import pandas as pd
import random
import math
import numpy as np
import matplotlib.pyplot as plt
import time

class KMeansClustering:
    
    def __init__(self, iteration, K):
        self.iteration = iteration
        self.K = K
        
    def oklid(self,x,y,x1,y1):
        value = (x - x1)**2 + (y - y1)**2
        return math.sqrt(value)

    def fit(self, X, Y, Labels):
        centers = []
        oklids = np.array([])
        while(self.K > 0):
            randomx = X.sample().iloc[0]
            randomy = Y.sample().iloc[0]
            centers.append((randomx, randomy))
            self.K -= 1
            
        dataset = pd.DataFrame({'X': X, 'Y': Y, 'Labels': Labels})

        while self.iteration > 0:
            start_time = time.time()
            for row in range(len(X)):
                for c in range(len(centers)):
                    oklids = np.append(oklids, self.oklid(centers[c][0], centers[c][1], X[row], Y[row]))
                min_index = np.argmin(oklids)
                dataset.at[row, 'Labels'] = min_index
                oklids = []
            centers_len = len(centers)
            centers = []
            for c in range(centers_len):
                x_mean = dataset[dataset['Labels'] == c]['X'].mean()
                y_mean = dataset[dataset['Labels'] == c]['Y'].mean()
                centers.append((x_mean,y_mean))

            self.iteration -= 1
        end_time = time.time()
        learn_time = end_time - start_time
        
        return dataset,learn_time
            
def minmaxnormalize(dataset, column_name, new_min, new_max):
    column = dataset[column_name]
    min_val = column.min()
    max_val = column.max()
    normalized_column = (column - min_val) / (max_val - min_val) * (new_max - new_min) + new_min
    dataset[column_name] = normalized_column
    return dataset

def minmaxnormalize2(dataset, new_min, new_max):
    for col in dataset.columns:
        if col != 'country' and col != 'advance':
            X_min = dataset[col].min()
            X_max = dataset[col].max()
            dataset[col] = ((dataset[col] - X_min) / (X_max - X_min)) * (new_max - new_min) + new_min  
    return dataset

def delete_specific_data(dataset,column,row):
    dataset.at[row, column] = None
    return dataset

def delete_random_data(dataset,deletedatanumber,between_row):

    if deletedatanumber == 0:
        return dataset
    random_row = random.randint(0, between_row)
    selected_columns = dataset.drop(['country', 'advance'], axis=1).columns
    random_column = random.choice(selected_columns)
    if pd.isnull(dataset.at[random_row, random_column]): #pd.isnull return true if data is None else return False
        return delete_random_data(dataset,deletedatanumber,between_row)
        
    dataset.at[random_row, random_column] = None
    
    return delete_random_data(dataset,(deletedatanumber-1),between_row)
    
def fillemptydat(dataset):
    dataset['child_mort'].fillna(dataset['child_mort'].mean(), inplace=True)
    dataset['exports'].fillna(dataset['exports'].mean(), inplace=True)
    dataset['health'].fillna(dataset['health'].mean(), inplace=True)
    dataset['imports'].fillna(dataset['imports'].mean(), inplace=True)
    dataset['income'].fillna(dataset['income'].mean(), inplace=True)
    dataset['inflation'].fillna(dataset['inflation'].mean(), inplace=True)
    dataset['life_expec'].fillna(dataset['life_expec'].mean(), inplace=True)
    dataset['total_fer'].fillna(dataset['total_fer'].mean(), inplace=True)
    dataset['gdpp'].fillna(dataset['gdpp'].mean(), inplace=True)
    
    return dataset
def fillemptydatabygroup(dataset,column_name):
    
    grouped = dataset.groupby('advance')

    average_0 = grouped.get_group(0)[column_name].mean()
    average_1 = grouped.get_group(1)[column_name].mean()
    average_2 = grouped.get_group(2)[column_name].mean()

    dataset.loc[dataset['advance'] == 0, column_name] = dataset.loc[df['advance'] == 0, column_name].fillna(average_0)
    dataset.loc[dataset['advance'] == 1, column_name] = dataset.loc[df['advance'] == 1, column_name].fillna(average_1)
    dataset.loc[dataset['advance'] == 2, column_name] = dataset.loc[df['advance'] == 2, column_name].fillna(average_2)

    return dataset
           
df = pd.read_csv('19010011039.csv')
df2 = df.copy()
sutun1 = 'health'
sutun2 = 'income'
sutun3 = 'advance'
unique_values = df['advance'].unique() # kaç farklı sinif oldugunu bulduk
k = len(unique_values)
kmeans = KMeansClustering(10,k)
dataset , ham_learn_time = kmeans.fit(df[sutun1],df[sutun2],df[sutun3])

normalize_df = minmaxnormalize(df,'child_mort',0,100)
normalize_df = minmaxnormalize(normalize_df,'income',0,1000)

normalize_df = delete_specific_data(normalize_df,'child_mort', 0)
normalize_df = delete_specific_data(normalize_df,'child_mort', 1)
normalize_df = delete_specific_data(normalize_df,'child_mort', 8)
normalize_df = delete_specific_data(normalize_df,'health', 2)
normalize_df = delete_specific_data(normalize_df,'health', 4)
normalize_df = delete_specific_data(normalize_df,'income', 1)
normalize_df = delete_specific_data(normalize_df,'life_expec', 8)

normalize_df = delete_random_data(normalize_df,5,10)
normalize_df = fillemptydatabygroup(normalize_df,'child_mort')
normalize_df = fillemptydatabygroup(normalize_df,'exports')
normalize_df = fillemptydatabygroup(normalize_df,'health')
normalize_df = fillemptydatabygroup(normalize_df,'imports')
normalize_df = fillemptydatabygroup(normalize_df,'income')
normalize_df = fillemptydatabygroup(normalize_df,'inflation')
normalize_df = fillemptydatabygroup(normalize_df,'life_expec')
normalize_df = fillemptydatabygroup(normalize_df,'total_fer')
normalize_df = fillemptydatabygroup(normalize_df,'gdpp')

unique_values = normalize_df['advance'].unique() # kaç farklı sinif oldugunu bulduk
k = len(unique_values)
normalize_kmeans = KMeansClustering(10,k)
normalize_dataset, normalize_learn_time = normalize_kmeans.fit(normalize_df[sutun1],normalize_df[sutun2],normalize_df[sutun3])

from sklearn.metrics import adjusted_rand_score

ham_dogrulukorani = adjusted_rand_score(dataset['Labels'],df2['advance'])
normalize_dogrulukorani = adjusted_rand_score(normalize_dataset['Labels'],df2['advance'])

print(f'ham verisetinin dogruluk performans metriği: {ham_dogrulukorani} egitim suresi {ham_learn_time}')
print(f'normalize verisetinin dogruluk performans metriği: {normalize_dogrulukorani} egitim suresi {normalize_learn_time}')

colors = {0: 'red', 1: 'green', 2: 'blue'}

fig, axes = plt.subplots(1, 3, figsize=(15, 5))
axes[0].scatter(normalize_dataset['X'], normalize_dataset['Y'], c=[colors[label] for label in normalize_dataset['Labels']], marker='o')
axes[0].set_xlabel('X')
axes[0].set_ylabel('Y')
axes[0].set_title('Normalized Dataset')

axes[1].scatter(dataset['X'], dataset['Y'], c=[colors[label] for label in dataset['Labels']], marker='o')
axes[1].set_xlabel('X')
axes[1].set_ylabel('Y')
axes[1].set_title('HAM Dataset')

axes[2].scatter(df2[sutun1], df2[sutun2], c=[colors[label] for label in df2['advance']], marker='o')
axes[2].set_xlabel(sutun1)
axes[2].set_ylabel(sutun2)
axes[2].set_title('DOGRU Dataset')

plt.tight_layout()
plt.show()
