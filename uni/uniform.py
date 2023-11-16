import random
import math
import matplotlib.pyplot as plt


def gen_uniform(theta: float) -> float:
    return random.uniform(0, 1) * theta #реализация с.в.

def five_sel_uniform(n:int,theta:float)->list:
    sel=[]
    for i in range(5):
        a = []
        for i in range(n):
            a.append(gen_uniform(theta))
        a.sort()
        sel.append(a)
    return sel #создает list list'ов по n элементов каждой выборки

a5=five_sel_uniform(5,10)
a10=five_sel_uniform(10,10)
a100=five_sel_uniform(100,10)
a200=five_sel_uniform(200,10)
a400=five_sel_uniform(400,10)
a600=five_sel_uniform(600,10)
a800=five_sel_uniform(800,10)
a1000=five_sel_uniform(1000,10)#list'ы list'ов различных размеров

#aa=[a5,a10,a100,a200,a400,a600,a800,a1000]


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
    return ans#эмпирическая функция

#cdf
uniform=[]
for i in range(1000):
    uniform.append(gen_uniform(10))
uniform.sort()

uniformch=uniform.copy()
for i in range(len(uniformch)):
    uniformch[i]=0

for i in range(len(uniform)):
    count=0
    for j in range(len(uniform)):
        if uniform[i]>uniform[j] and i!=j:
            count+=1
    uniformch[i]=count

for i in range(len(uniformch)):
    uniformch[i]/=len(uniform)
#cdf

plt.plot(uniform,uniformch,label='Ф-ия распределения')

axs=plt.subplot()
axs.step(a1000[0],emp_func(0,a1000),where='post',label='Эмп. ф. 1ой выборки')
axs.step(a1000[1],emp_func(1,a1000),where='post',label='Эмп. ф. 2ой выборки')
axs.step(a1000[2],emp_func(2,a1000),where='post',label='Эмп. ф. 3ей выборки')
axs.step(a1000[3],emp_func(3,a1000),where='post',label='Эмп. ф. 4ой выборки')
axs.step(a1000[4],emp_func(4,a1000),where='post',label='Эмп. ф. 5ой выборки')
plt.legend()
plt.show()'''#эмпирические функции выборок размера 1000 (для остальных размеров менял параметр в скобке a1000 на a100 etc.)

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

'''max=0
file=open('uniform_D.txt','w')
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

'''file=open('uniform_X.txt','w')
for i in range(len(aa)):
    for j in range(len(aa[i])):
        X=0
        for q in range(len(aa[i][j])):
            X+=1/len(aa[i][j])*aa[i][j][q]
        strr='X('+str(len(aa[i][j]))+')='+str(X)+'\n'
        file.write(strr)
file.close()'''#подсчет X в отдельный файл

'''file=open('uniform_S.txt','w')
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
file.close()''' #подсчет S в отдельный файл