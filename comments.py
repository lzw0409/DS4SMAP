import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from wordcloud import WordCloud
from pyecharts.charts import Pie
from pyecharts import options as opts
import os



def getText2():
    txt = open("all.txt", "r").read()
    txt = txt.lower()
    txt = txt.replace('\n', ',')
    txt = txt.replace(' ', ',')
    #for ch in '\n':
    #    txt = txt.replace(ch, " ")
    return txt


def outPutCount2():
    hamletTxt = getText2()          #得到原始数据
    words = hamletTxt.split(',')    #根据‘，’将作者名分开

    counts = {}                     #定义存储词频的字典
    #进行计数
    remove_words = ['critical','there','some','28/04/20','23','time','20','will','md.','30','26','dr.','r.verified','b.verified','would','k.verified','t.','g.','8','14','moreread','w.','o.','15','5','but','13','16','p.','be','are','jul','25','so','much','s.verified','n.','dr','learning','3','27','m.verified','that','a.verified','as','me','1','17','an','28','h.','for', 'and', 'with', 'a', 'of', 'in', 'from', 'to', 'the', 'using', 'by',',','share','2020','5.0','2020review','on','star','may','0','learner','review','this','rating','2020was','helpful?','very','course',"'",'i','was','apr','is','it','stating','covid','covid-19','jun','care','r.','a.','k.','care:','S.','19','12','18','c.','really','s.','b.','m.','my','4.0','you','all','about','','course.','have'] 
    for word in words:
        if word in remove_words:
            continue
        else:
            counts[word] = counts.get(word, 0) + 1
    # 将字典存储到csv文件中
    pd.DataFrame(counts,index=[0]).to_csv('hotauthor.csv')

    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)
    for i in range(10):
        word, count = items[i]
        print("{0:<10}{1:>5}".format(word, count))
    for i in range(50):
        word, count = items[i]
        print("{0:<50}{1:>0}".format(word, count))
    # create a figure and axis
    fig, ax = plt.subplots()

    # get x and y data
    x=[]
    height=[]
    width = 0.5
    for i in range(20):
        a,b =items[i]
        x.append(a)
        height.append(b)
    # create bar chart
    ax.barh(x,height,width,linewidth=2,edgecolor="blue",color="yellow")
    # set title and labels
    ax.set_title('hot words in all comments')
    ax.set_ylabel('author')
    ax.set_xlabel('count')

    for i in range(15):
        plt.text(height[i]+0.2,i-0.2,height[i])

    plt.show()

    # 词云图
    #hamletTxt=hamletTxt.replace(" ",'')
    wordcloud = WordCloud(
        background_color="white",  # 设置背景为白色，默认为黑色
        width=1500,  # 设置图片的宽度
        height=960,  # 设置图片的高度
        margin=10 , # 设置图片的边缘
        min_font_size =10,
        max_font_size=220,
        max_words=20,

    ).fit_words(counts)
    # 绘制图片
    plt.imshow(wordcloud,interpolation='bilinear')
    # 消除坐标轴
    plt.axis("off")
    # 展示图片
    plt.show()

if __name__ == '__main__':
    outPutCount2()

