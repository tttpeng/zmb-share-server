from flask import Flask, render_template, request,jsonify

from flask.ext.sqlalchemy import SQLAlchemy
import json
import  logging
# logging.basicConfig()
# logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/zmb'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://zhongmeban_share:Zhongmeban123@rds9i2oey14eccx3h4qh.mysql.rds.aliyuncs.com/zhongmeban_release3'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
db.init_app(app)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)


    def __repr__(self):
        return '<Product %r>' % self.name

def getNews(new_id):
    result = db.session.execute('SELECT * From t_info_news WHERE NEWS_ID = %d;' % new_id)
    print('------')
    # results = result.fetchall()
    # dict = []
    # for row in results:
    #     dict.append(row.items())
    #     print(type(row.items()))


    title = result.fetchall()[0].items()[1][1]
    print(type(title))
    print(title)

    # print(json.dumps(dict))
    print('------')
    return title




@app.route('/')
def hello_world():
    return 'asd1'
    # result = getNews()
    # abl = result
    # return json.dump(getNews())


@app.route('/new/<int:new_id>')
def new(new_id):
    title = getNews(new_id)
    return 'New %s' % title




if __name__ == '__main__':

    getNews(2)
    # users = Product.query.all()
    # result = db.session.execute('SELECT * From t_info_news;')
    # for row in result:
        # print(row[3])
    # print(users)

    app.run()
