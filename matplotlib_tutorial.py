#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# 
# <H3> Temel Çizim İşlemleri </H3>
# 
# Plot y versus x as lines and/or markers.
# plot(\*args[, scalex, scaley, data])
# 

# In[2]:


plt.plot([1,2,3,4], [1,4,9,16])


# In[3]:


x = [1,2,3,4]
y = [1,4,9,16]


plt.plot(x,y)
plt.show()


# In[4]:


plt.title("İlk grafiğimiz!")
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.plot(x,y)
plt.show()


# In[5]:



# Normalde çentikler otomatik olarak yerleştirilir
# Kendiniz de çentiklerin yerini tanımlayabilirsiniz

plt.xticks([1,2,3,4])   #küsüratları da gösterebilir!
plt.yticks([1,4,9,16])
plt.title("İlk grafiğimiz!")
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.plot(x,y)
plt.show()


# <H3> Lejant koyma  </H3>
# 

# In[6]:


plt.plot(x,y, label='x^2', color='green')
plt.xticks([1,2,3,4,5])   
plt.yticks([1,4,9,16,25])
plt.title("İlk grafiğimiz!")
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.legend()
plt.show()


# In[7]:


# linewidth ekleme
plt.plot(x,y, label='x^2', color='blue', linewidth = 2, linestyle = '--', marker='.')
plt.xticks([1,2,3,4,5])   
plt.yticks([1,4,9,16,25])
plt.title("İlk grafiğimiz!")
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.legend()
plt.show()


# <H3> Aynı grafikte birden fazla çizim yapmak </H3>
# 

# In[8]:


plt.plot(x,y, label='x^2', color='green', linewidth = 2, linestyle = '--', marker='.')
plt.xticks([0,1,2,3,4,5])   
plt.yticks([0,1,4,9,16,25])
plt.title("İlk grafiğimiz!")
plt.xlabel('x axis')
plt.ylabel('y axis')


# 2.Çizgimizi çiziyoruz
x2 = np.arange(0,5,0.5)
plt.plot(x2,x2*2,color='red', linewidth = 2, marker='.', label='2*x')

plt.legend()
plt.show()


# <H3> Grafiğinizi bilgisayarınıza kaydetme </H3>
# 

# In[9]:


plt.plot(x,y, label='x^2', color='green', linewidth = 2, linestyle = '--', marker='.')
plt.xticks([0,1,2,3,4,5])   
plt.yticks([0,1,4,9,16,25])
plt.title("İlk grafiğimiz!")
plt.xlabel('x axis')
plt.ylabel('y axis')


# 2.Çizgimizi çiziyoruz
x2 = np.arange(0,5,0.5)
plt.plot(x2,x2*2,color='red', linewidth = 2, marker='.', label='2*x')

plt.legend()

plt.savefig('ilkgrafigim.png', dpi=300)

plt.show()


# <H3>Barchart</H3>

# In[10]:


x = ['Ankara', 'İstanbul', 'İzmir']
y = [120, 178, 87]

plt.bar(x,y)
plt.show()


# In[11]:



# Eğer çubuklardan bir tanesini diğerlerinden farklılaştırmak için içini boyamak isterseniz:
x = ['Ankara', 'İstanbul', 'İzmir']
y = [120, 178, 87]

cubuklar = plt.bar(x,y)
cubuklar[1].set_hatch('/')
cubuklar[0].set_hatch('.')
plt.show()


# <H1> Detaylı Örnekler </H1>
# 

# In[12]:


gas = pd.read_csv('petrolfiyatlari.csv')

gas


# In[13]:


plt.title('Petrol Fiyatları')
plt.plot(gas['Year'], gas['USA'], 'b-', label='USA')

plt.xlabel('Yıl')
plt.ylabel('Dolar')

plt.legend()
plt.show()


# In[ ]:



plt.title('Petrol Fiyatları')

plt.plot(gas.Year, gas.USA, 'b-', label='USA')
plt.plot(gas.Year, gas['Canada'], 'r-', label="Kanada")
plt.plot(gas.Year, gas['South Korea'], 'g.-', label='Güney Kore')
plt.plot(gas.Year, gas['France'], 'y.-', label='Fransa')
plt.plot(gas['Year'], gas.Germany, color='orange', label='Germany')

plt.xlabel('Yıl')
plt.ylabel('Dolar')

plt.legend()

plt.show()


# <H3> Figure Size </H3>
# Tablonuzun büyüklüğünü değiştirebilirsiniz:  
# 
# plt.figure(figsize=(XWidth,Ywidth))

# In[ ]:


plt.figure(figsize=(14,5))
plt.title('Petrol Fiyatları')

plt.plot(gas.Year, gas.USA, 'b-', label='USA')
plt.plot(gas.Year, gas['Canada'], 'r-', label="Kanada")
plt.plot(gas.Year, gas['South Korea'], 'g.-', label='Güney Kore')
plt.plot(gas.Year, gas['France'], 'y.-', label='Fransa')


plt.xlabel('Yıl')
plt.ylabel('Dolar')

plt.legend()
plt.savefig('ikincigrafigim.png', dpi=300)
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




