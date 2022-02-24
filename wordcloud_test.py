# -*- coding = utf-8 -*-
# @Time : 2022/2/23 14:52
# @Author : Hzj
# @File : wordcloud_test.py
# @Software : PyCharm

import jieba  # 分词
from matplotlib import pyplot as plt  # 绘图，数据可视化
from wordcloud import WordCloud  # 词云
from PIL import Image  # 图片处理
import numpy as np  # 矩阵运算
import sqlite3  # 数据库


# 准备词云所需的文字（词）
text = ""
con = sqlite3.connect('venv/db/movie.db')
cur = con.cursor()
sql = 'select introduction from movie250'

for item in cur.execute(sql):
    text = text + item[0]

cur.close()
con.close()

# 切词
cut = jieba.cut(text)
string = '/'.join(cut)

# wordcloud运用
img = Image.open('venv/static/assets/img/wordcloud.png')
img_array = np.array(img)    # 将图片转换为数组
wc = WordCloud(
    background_color='white',
    mask=img_array,
    font_path='STSONG.TTF'
)
wc.generate_from_text(string)

# 绘制图片
fig = plt.figure(1)
plt.imshow(wc)
plt.axis('off')    # 是否显示坐标轴

# plt.show()
plt.savefig('wordcloud_test.jpg')
print('finish')
Image.open('wordcloud_test.jpg').show()
