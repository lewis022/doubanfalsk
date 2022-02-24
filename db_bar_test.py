# -*- coding = utf-8 -*-
# @Time : 2022/2/22 17:53
# @Author : Hzj
# @File : db_bar_test.py
# @Software : PyCharm

import sqlite3
from datetime import datetime

count = []
score = []

con = sqlite3.connect('venv/db/movie.db')
cur = con.cursor()

sql = '''
        SELECT score, COUNT(*) AS "Number Of Movies"  
        FROM movie250  
        GROUP BY score;
      '''

data = cur.execute(sql)

for item in data:
    count.append(item[0])
    score.append(item[1])
    print('count =', item[1])
    print("score= ", item[0], end="\n\n")
cur.close()
con.close()
print('finish')
print('---------------分隔符-------------------')
print(count)
print(score)



# for i in range(80, 99):
#     i = i / 10
#     print(i)
#     print("sql = 'select * from movie250 where score = %s'" % i)
