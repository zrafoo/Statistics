import math
import random
import matplotlib.pyplot as plt


def gen_Bernolli(theta:float)->int:
    if 0<=random.uniform(0,1)<=1-theta: return 0
    else: return 1 #генерация Бернулли

def gen_NBin(m:int,theta:float)->int:
    count=0
    succ=0
    while succ!=m:
        if gen_Bernolli(theta)==1:
            succ+=1
        else:count+=1
    return count #реализация отр.бин.с.в. через испытание Бернулли

def five_sel_Nbin(n:int,m:int,theta:float)->list:
    sel=[]
    for i in range(5):
        a = []
        for i in range(n):
            a.append(gen_NBin(m, theta))
        a.sort()
        sel.append(a)
    return sel #создает list list'ов по n элементов каждой выборки


a5=five_sel_Nbin(5,10,0.5)
a10=five_sel_Nbin(10,10,0.5)
a100=five_sel_Nbin(100,10,0.5)
a200=five_sel_Nbin(200,10,0.5)
a400=five_sel_Nbin(400,10,0.5)
a600=five_sel_Nbin(600,10,0.5)
a800=five_sel_Nbin(800,10,0.5)
a1000=five_sel_Nbin(1000,10,0.5)#list'ы list'ов различных размеров

#aa=[a5,a10,a100,a200,a400,a600,a800,a1000]

'''max=0
file=open('nbin_D.txt','w')
for t in range(len(aa)):
    for tt in range(len(aa)):
            for i in range(len(aa[t])):
                for j in range(len(aa[tt])):
                    for q in range(len(aa[tt][i])):
                        for z in range(len(aa[tt][j])):
                            if abs(aa[tt][i][q]-aa[tt][i][z])>max:
                                max=abs(aa[tt][i][q]-aa[tt][i][z])
            strr='D('+str(len(aa[t][i]))+','+str(len(aa[tt][j]))+')='+str(math.sqrt((len(aa[t][i])*len(aa[tt][j]))/(len(aa[tt][j])+len(aa[t][i])))*max)+'\n'
            file.write(strr)
            max=0
file.close()'''#подсчет D(n,m) по всем парам выборок разных размеров


'''def emp_func(n:int,a:list)->list:
    ans=[]
    for i in range(len(a[n])):
        ans.append(0)
    for i in range(len(a[n])):
        for j in range(len(a[n])):
            if a[n][j]<a[n][i] and (i!=j):
                ans[i]+=1
    for i in range(len(a[n])):
        ans[i]=ans[i]/len(a[n])
    return ans'''

'''#cdf
nbin=[]
for i in range(10000):
    nbin.append(gen_NBin(10,0.5))
nbin.sort()

nbinch=nbin.copy()
for i in range(len(nbinch)):
    nbinch[i]=0

for i in range(len(nbin)):
    count=0
    for j in range(len(nbin)):
        if nbin[i]>nbin[j] and i!=j:
            count+=1
    nbinch[i]=count

for i in range(len(nbinch)):
    nbinch[i]/=len(nbin)
#cdf

plt.plot(nbin,nbinch,label='Ф-ия распределения')

axs=plt.subplot()
axs.step(a800[0],emp_func(0,a800),where='post',label='Эмп. ф. 1ой выборки')
axs.step(a800[1],emp_func(1,a800),where='post',label='Эмп. ф. 2ой выборки')
axs.step(a800[2],emp_func(2,a800),where='post',label='Эмп. ф. 3ей выборки')
axs.step(a800[3],emp_func(3,a800),where='post',label='Эмп. ф. 4ой выборки')
axs.step(a800[4],emp_func(4,a800),where='post',label='Эмп. ф. 5ой выборки')
plt.legend()
plt.show()'''#эмпирические функции выборок размера 1000 (для остальных размеров менял параметр в скобке a1000 на a100 etc.)


'''#pmf
nbin=[]
for i in range(100000):
    nbin.append(gen_NBin(10,0.5))
nbin.sort()

nbin_value=[]
for i in range(100000):
    if nbin[i] not in nbin_value:
        nbin_value.append(nbin[i])
nbin_value.sort()
nbin_chance=nbin_value.copy()
for i in range(len(nbin_chance)):
    nbin_chance[i]=0
for i in range(100000):
    for j in range(len(nbin_value)):
        if nbin[i]==nbin_value[j]:
            nbin_chance[j]+=1
for i in range(len(nbin_chance)):
    nbin_chance[i]/=100000

plt.plot(nbin_value,nbin_chance)

#pmf
nbin_value1=[]
for i in range(len(a1000[0])):
    if a1000[0][i] not in nbin_value1:
        nbin_value1.append(a1000[0][i])
nbin_value1.sort()
nbin_chance1=nbin_value1.copy()
for i in range(len(nbin_chance1)):
    nbin_chance1[i]=0
for i in range(len(a1000[0])):
    for j in range(len(nbin_value1)):
        if a1000[0][i]==nbin_value1[j]:
            nbin_chance1[j]+=1
for i in range(len(nbin_chance1)):
    nbin_chance1[i]/=len(a1000[0])# 6 times

plt.plot(nbin_value1,nbin_chance1)
plt.show()'''#полигон частот (для других выборок менять размер a1000 на другой)

'''#theta=0.5, m=10
file=open('nbin_X.txt','w')
for i in range(len(aa)):
    for j in range(len(aa[i])):
        X=0
        for q in range(len(aa[i][j])):
            X+=1/len(aa[i][j])*aa[i][j][q]
        strr='X('+str(len(aa[i][j]))+')='+str(X)+'\n'
        file.write(strr)
file.close()'''#X
'''file=open('nbin_S.txt','w')
for i in range(len(aa)):
    for j in range(len(aa[i])):
        X=0
        S=0.
        for q in range(len(aa[i][j])):
            X+=1/len(aa[i][j])*aa[i][j][q]
        for q in range(len(aa[i][j])):
            S=S+1/len(aa[i][j])*pow(aa[i][j][q]-X,2)
        strr='S('+str(len(aa[i][j]))+')='+str(S)+'\n'
        file.write(strr)
file.close()'''#S