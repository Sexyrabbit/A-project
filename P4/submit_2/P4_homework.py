
# coding: utf-8

# # 问题： 有哪些因素会让船上的人生还率更高？

# ## 简介：
# #### 项目数据来自[titanic-data.csv](https://github.com/ShiChJ/DAND-Basic-Materials/blob/master/P2/Project_Files/titanic-data.csv)，通过已有数据分析出泰坦尼克号上哪一类群体的生还几率更高
# 

# ## 数据整理：
# #### 由于数据中出现了空值，现将年龄列用年龄均值填充，由于cabin确实值太多，将cabin列删除
# #### 以下代码部分为加载数据并除去空值

# In[591]:



# 加载样本数据,加载第三方库

import pandas as pd
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import seaborn as sns

get_ipython().magic(u'matplotlib inline')

raw_data = pd.read_csv('titanic-data.csv')


# 去掉空值, 年龄按均值填充, cabin
def remove_empty_cells(dataframe, list_of_columns, replace):
    for column in list_of_columns:
      dataframe[column] = dataframe[column].fillna(replace)
    return dataframe

lists = ['Age']

raw_data.Age.fillna(raw_data.Age.mean(),inplace=True)

new_data = remove_empty_cells(raw_data,lists,raw_data.Age.mean())

del raw_data['Cabin']

raw_data[0:10]


# ## 数据分析 part 1： 皮尔逊相关系数
# #### 以下代码将根据数据呈现出来的相关性，利用皮尔逊积矩等方法来分析数据。

# In[592]:


#相关数据，可进行数学计算，用于皮尔逊相关系数的计算
raw_data.describe()


# ##### 以下为皮尔逊相关系数的数据和可视化图像

# In[593]:


# 皮尔逊积矩
raw_data.corr()


# In[594]:


# 图形化皮尔逊积矩表
def correlation_matrix(df,labels):

    fig = plt.figure()
    fig.set_figheight(9)
    fig.set_figwidth(9)
    ax1 = fig.add_subplot(111) #一行一列的第一个
    cmap = cm.get_cmap('jet', 999)
    cax = ax1.imshow(df.corr(), interpolation="nearest", cmap=cmap)
    ax1.grid(True)
    plt.title('table 1-1 data correlation')
    #ax1.set_xticks(range(len(labels)))
    ax1.set_xticklabels(labels,fontsize=11)
    ax1.set_yticklabels(labels,fontsize=11)
    # Add colorbar, make sure to specify tick locations to match desired ticklabels
    fig.colorbar(cax, ticks=[.01,.05,.10,.50,.95,1])
    plt.show()

labels=['','PasngerId','Survived','Pclass','Age','SibSp','Parch','Fare']
correlation_matrix(raw_data,labels)


# #### 从图1-1我们可以观察到，颜色对应越深，代表相关系数越高，从Survived列上观察，可得Survived和PClass的颜色最显著，
# #### 而PClass于Age，Survived，Fare相关性比较显著。

# ### Part 1总结：
# 
# #### 由皮尔逊积矩得出相关系数，几个强关联的数据为Fare和Pclass（-0.549500）为强负相关，
# #### 即Fare（票价）越高，船仓等级越低（Pclass，等级越低越豪华，1最豪华）。
# #### 由于票价包含了多人组团购买船票的因素，我们利用船舱等级来分析其与生还概率的关系。
# #### 值得注意的是，这个相关系数只能反映两个变量的线性相关性。所以哪怕相关系数接近于0，不表示两个变量没有相关性。

# ## 数据分析 part 2： PClass于生还概率的关系
# #### 由皮尔逊相关系数的结果，我们先观察PClass与生还概率的关系，以下代码将分析生还率与Pclass相关的数据分布。
# #### 先计算每个PClass分类下的人数总量和生还者总量，然后将他们用可视化的图表展示出来观察其与生还率的关系。

# In[595]:


#get unique survived_ppl set of passenger id
survived_ppl = set()
for indexs in raw_data.index:
    if raw_data.loc[indexs].values[1] == 1:
        survived_ppl.add(raw_data.loc[indexs].values[0])
        
raw_data.groupby('Survived').size()


# In[596]:


# 每个Pclass的总人数
raw_data.groupby('Pclass').size()


# In[597]:


# 每个Pclass的遇难者和生还者人数
raw_data.groupby(['Pclass', 'Survived']).size()


# In[598]:



# 绘制分组条形图
ind = np.arange(3) 

grouped_data = raw_data.groupby(['Pclass', 'Survived']).size().unstack()
grouped_data.plot(kind='bar', stacked=False, width = 0.35)
plt.xticks(ind, ('Pclass 1', 'Pclass 2', 'Pclass 3'), rotation=0)
plt.title('chart 2-1 ppl number groupby Pclass')
plt.ylabel('ppl number count')
plt.show()



# In[599]:


# 绘制堆栈条形图
grouped_data.plot(kind='bar', stacked=True)
plt.xticks(ind, ('Pclass 1', 'Pclass 2', 'Pclass 3'), rotation=0)
plt.title('chart 2-2 ppl number groupby Pclass-stacked')
plt.ylabel('ppl number count')
plt.show()




# ### Part 2 总结：
# 
# #### 由chart 2-1 可以得出，PClass1的生还者数量显著大于死亡者数量，为3个Class中最高的。
# #### 由chart 2-2 同样可以得出Pclass1点生还者数量最多，但Pclass1的总人数少于Pclass3稍多于Pclass2
# #### 由上可以得出，在PClass1上有助于提高生还率。

# ## 数据分析 Part 3：生还率于其他数据的相关性
# 
# #### 我们注意到年龄是最易区别个体的变量，而且年龄与PClass也有一定相关性，所以接下来分析年龄是否与生还率有一定联系
# #### 首先我们按照生还与否以及年龄进行分类，为了减少数据和可视化图像的复杂度，我们将年龄分类的bin size设为10，
# #### 下面代码为不同年龄段段人数
# 

# In[600]:


bins=np.arange(0,90,10)
raw_data['Age_group'] = pd.cut(raw_data['Age'], bins)
raw_data.groupby('Age_group').size()


# #### 下面代码为不同年龄段和生还与否的人数

# In[601]:


raw_data.groupby(['Age_group', 'Survived']).size()


# #### 下面代码为生还者在不同年龄段段分布数量

# In[602]:


raw_data['Surviver_Age_group'] = pd.cut(raw_data.loc[raw_data.Survived == 1]['Age'], bins)

raw_data.groupby('Surviver_Age_group').size()


# #### 下面我们按照年龄分组，画出生还者与死亡人数的柱状图

# In[603]:


# 对年龄分组
bins=np.arange(0,90,10)
raw_data['Age_group'] = pd.cut(raw_data['Age'], bins)

# 绘制不同分组的生还者和遇难者条形图
grouped = raw_data.groupby(['Age_group', 'Survived']).size()
grouped.unstack().plot(kind='bar', stacked=False)
plt.ylabel('ppl number count')
plt.title('chart 3-1 survived ppl number groupby Age_group')
plt.show()


# #### 下面代码求不同年龄段的生还率，由于死亡者为0，生还者为1，每个年龄组的survived列的均值即为生还率。

# In[604]:



raw_data.groupby('Age_group')['Survived'].mean()


# In[605]:


raw_data.groupby('Age_group')['Survived'].mean().plot(kind='bar', stacked=False)
plt.ylabel('Survival rate')
plt.title('chart 3-2 survival rate groupby Age_group')
plt.show()


# ### Part 3 总结：
# 
# #### 由3-1可以分析得出，年龄在20-30岁人数最多，虽然生还者最多，但是死亡人数也是最多的，而年龄在0-10岁，
# #### 生还人数比死亡人数要多，由3-2更可以看出，0-10岁分组多生还率为0.59（取两位小数），是最高的，所以结论为，
# #### 年龄在0-10岁的生还概率最高。

# ## 结论
# 
# 
# #### 本报告的结论为，当乘客在PClass为1的情况下生还概率比其他PClass高，年龄段在0-10之间的获救概率大于其他年龄层。
# #### 报告中使用的数据是乘客总体数据，数据中缺失的部分如年龄，按照均值填充，Cabin由于缺失部分太多将其删除，
# #### 缺失的数据会对总体造成相应的影响，但由于数目不大，而且按照均值填充，对结论的产生影响不大。
# #### 数据中Fare的数据应当与Pclass成正相关，但有些数据不符，据观察是由于其中包含了多人的票价。
# #### 报告并没有讨论的所有变量，只讨论了几个相关性比较显著的变量，其他变量比如性别，家属或许会有一定相关性。

# ## 参考文献：
# [Calculation and Visualization of Correlation Matrix with Pandas](https://datascience.stackexchange.com/questions/10459/calculation-and-visualization-of-correlation-matrix-with-pandas)
# 
# [Matplotlib Color map](https://matplotlib.org/api/cm_api.html)
# 
# [matplotlib add_subplot](http://www.codeweblog.com/matplotlib-pyplot中add_subplot方法参数111的含义/)
# 
# [matplotlib imshow](https://matplotlib.org/devdocs/api/_as_gen/matplotlib.pyplot.imshow.html)
# 
# [What does matplotlib `imshow(interpolation='nearest')` do?](https://stackoverflow.com/questions/12473511/what-does-matplotlib-imshowinterpolation-nearest-do)
# 
# [matplotlib绘图常见设置](https://www.cnblogs.com/nju2014/p/5707980.html)
