# -*- coding = utf-8 -*-
# @Time : 2022/2/21 11:41
# @Author : Hzj
# @File : app.py
# @Software : PyCharm

from flask import Flask,render_template
import sqlite3

app = Flask(__name__)
#app.config['SECRET_KEY'] = '123456'

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/movie')
def movie():
    datalist = []
    con = sqlite3.connect('db/movie.db')
    cur = con.cursor()
    sql = "select * from movie250"
    data = cur.execute(sql)
    for item in data:
        datalist.append(item)
    cur.close()
    con.close()
    return render_template('movie.html',movies = datalist)

@app.route('/score')
def score():
    count = []
    score = []
    con = sqlite3.connect('db/movie.db')
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
    cur.close()
    con.close()
    return render_template('score.html',count = count,score = score)

@app.route('/cloud')
def cloud():
    return render_template('cloud.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/temp')
def temp():
    return render_template('temp.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')
