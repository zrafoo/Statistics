import math
import numpy as np
import random
import matplotlib.pyplot as plt


def gen_Bernolli(theta:float)->int:
    if 0<=random.uniform(0,1)<=1-theta: return 0
    else: return 1

def gen_NBin(m:int,theta:float)->int:
    count=0
    succ=0
    while succ!=m:
        if gen_Bernolli(theta)==1:
            succ+=1
        else:count+=1
    return count

def five_sel_Nbin(n:int,m:int,theta:float)->list:
    sel=[]
    for i in range(5):
        a = []
        for i in range(n):
            a.append(gen_NBin(m, theta))
        a.sort()
        sel.append(a)
    return sel

a5=five_sel_Nbin(5,10,0.5)
a10=five_sel_Nbin(10,10,0.5)
a100=five_sel_Nbin(100,10,0.5)
a200=five_sel_Nbin(200,10,0.5)
a400=five_sel_Nbin(400,10,0.5)
a600=five_sel_Nbin(600,10,0.5)
a800=five_sel_Nbin(800,10,0.5)
a1000=five_sel_Nbin(1000,10,0.5)


def emp_func(n:int,a:list)->list:
    ans=[]
    for i in range(len(a[n])):
        ans.append(0)
    for i in range(len(a[n])):
        for j in range(len(a[n])):
            if a[n][j]<a[n][i] and (i!=j):
                ans[i]+=1
    for i in range(len(a[n])):
        ans[i]=ans[i]/len(a[n])
    return ans#эмпирическая функция

#cdf
nbin=[]
for i in range(1000):
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

'''plt.plot(nbin,nbinch,label='Ф-ия распределения')

axs=plt.subplot()
axs.step(a1000[0],emp_func(0,a1000),where='post',label='Эмп. ф. 1ой выборки')
axs.step(a1000[1],emp_func(1,a1000),where='post',label='Эмп. ф. 2ой выборки')
axs.step(a1000[2],emp_func(2,a1000),where='post',label='Эмп. ф. 3ей выборки')
axs.step(a1000[3],emp_func(3,a1000),where='post',label='Эмп. ф. 4ой выборки')
axs.step(a1000[4],emp_func(4,a1000),where='post',label='Эмп. ф. 5ой выборки')
plt.legend()
plt.show()#эмпирические функции выборок размера 1000 (для остальных размеров менял параметр в скобке a1000 на a100 etc.)


'''
slimnbin=nbin
slimnbinch=nbinch
for x in slimnbin:
    while slimnbin.count(x)!=1:
        slimnbin.remove(x)
for x in slimnbinch:
    while slimnbinch.count(x)!=1:
        slimnbinch.remove(x)
slima=a10[0]
slimaemp=emp_func(0,a10)
for x in slima:
    while slima.count(x)!=1:
        slima.remove(x)
for x in slimaemp:
    while slimaemp.count(x)!=1:
        slimaemp.remove(x)

max=0
for i  in range(len(slimnbin)):
    for j in range(len(slima)):
        if slima[j]==slimnbin[i]:
            if abs(slimnbinch[i]-slimaemp[j])>max:
                max=abs(slimnbinch[i]-slimaemp[j])
                break
            break
print(max)

'''#pmf
uniform=[]
for i in range(1000):
    uniform.append(gen_uniform(10))
uniform.sort()

uniform_value=[]
for i in range(1000):
    if uniform[i] not in uniform_value:
        uniform_value.append(uniform[i])
uniform_value.sort()
uniform_chance=uniform_value.copy()
for i in range(len(uniform_chance)):
    uniform_chance[i]=1/10


plt.plot(uniform_value,uniform_chance)


uniform_value1=[]
for i in range(len(a100[0])):
    if a100[0][i] not in uniform_value1:
        uniform_value1.append(a100[0][i])
uniform_value1.sort()
uniform_chance1=uniform_value1.copy()
for i in range(len(uniform_chance1)):
    uniform_chance1[i]=0
for i in range(len(a100[0])):
    for j in range(len(uniform_value1)):
        if a100[0][i]==uniform_value1[j]:
            uniform_chance1[j]+=1
for i in range(len(uniform_chance1)):
    uniform_chance1[i]/=len(a100[0])# 6 times

plt.plot(uniform_value1,uniform_chance1)
plt.show()'''#полигон частот (для других выборок менять размер a100 на другой)
#pmf
