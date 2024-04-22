# AHMET EMİN KAZAN 19010011039
import random
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
# cvs dosyası oluşturularak genler yazılmaktadır.
# genetik algoritma için eleme algoritması : TURNUVA
# başlangıç 2 gen dizisinini popülasyonu 32
# kromozom eşleşmesi rastgele
# durma şartı 1 gen kalana kadar yani en iyi gen seçilene kadar
class Genetic:
    def __init__(self, gen1, gen2):
        self.gen1 = gen1
        self.gen2 = gen2
        self.population = []
        self.labels = []
        self.minimumy = float('inf')
        self.minimumindis1 = 0
        self.minimumindis2 = 0
        self.tempopulation = []
        
    def StyblinskiTang(self,x1,x2):
        return (((x1**4 - 16*x1**2 + 5*x1) + (x2**4 - 16*x2**2 + 5*x2)) / 2)
    
    # def ThreeHumpCamel(self,x1,x2):
    #     return (2*x1**2 - 1.05*x1**4 + x1**6/6 +x1*x2 + x2**2) + (2*x1**2 - 1.05*x1**4 + x1**6/6 +x1*x2 + x2**2)
    
    # def matyas_function(self,x, y):
    #     return 0.26 * (x**2 + y**2) - 0.48 * x * y

    def fit(self):
        while(len(self.population) != 1): # TOURNAMENT
            self.population = []
            while self.gen1:
                r = random.randint(0,len(self.gen1) - 1)
                r2 = random.randint(0,len(self.gen2) - 1)
                self.population.append([self.gen1[r],self.gen2[r2]])
                self.gen1.pop(r)
                self.gen2.pop(r2)
                
            for i in range(len(self.population)):
                y = self.StyblinskiTang(self.population[i][0], self.population[i][1])
                if y not in self.population[i]:
                    self.population[i].append(y)
            self.population.sort(key=lambda item: item[2]) # populasyon item[2] yani y değerine göre kucukten buyuge dogrusıralandı
            #print(self.population)
            self.tempopulation.append(self.population)
            
            self.population = self.population[:len(self.population)//2] # sıralanan popülasyonun yari boyutuna indirilerek minimum yani en iyi genler secildi
            
            for i in range(len(self.population)):
                self.gen1.append(self.population[i][0])
                self.gen2.append(self.population[i][1])
            print("1. dizinin secilen genleri : :",self.gen1)
            print("2. dizinin secilen genleri : :",self.gen2)
            
            
        return self.population[0], self.tempopulation


dizi1 = [random.uniform(-5, 5) for _ in range(32)]  # diziler aynı boyuttla olmalı !!!
dizi2 = [random.uniform(-5, 5) for _ in range(32)]

gen = Genetic(dizi1,dizi2)
populasyon, data = gen.fit()

print("en iyi popülasyon : ",populasyon[0] , populasyon[1])
print("global minimum : ",populasyon[2])
#print(data)
data.append([[populasyon[0] , populasyon[1], populasyon[2]]])
#print(data)
num_plots = len(data)
fig, axs = plt.subplots(1, num_plots, figsize=(15, 3))

for i in range(num_plots):
    axs[i].plot(np.array(data[i])[:, 0], 'o-', label='gen 1')
    axs[i].plot(np.array(data[i])[:, 1], 'x-', label='gen 2')
    axs[i].plot(np.array(data[i])[:, 2], '^-', label='minimum değer')
    
    axs[i].set_title(f'Turnuva Turu: {i + 1}')
    axs[i].legend()

plt.show()

import csv

# Örnek bir liste

# CSV dosyasını yazma
with open('veriler.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    for i in range(len(data)):
        writer.writerow(f"{i+1}.Turnuva turu:")
        writer.writerow("gen1 - gen2 -  kendi egitimim Y degeri")
        writer.writerows(data[i])

print("CSV dosyası başarıyla oluşturuldu.")

