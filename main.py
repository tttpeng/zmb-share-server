from flask import Flask, render_template, request,jsonify,Response
from flask_sqlalchemy import SQLAlchemy
import json
# import  logging
# logging.basicConfig()
# logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)



import logging
# 创建一个logger
logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)
# 创建一个handler，用于写入日志文件
fh = logging.FileHandler('/Users/tpeng/Desktop/test.log')
fh.setLevel(logging.DEBUG)
# 再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# 定义handler的输出格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# 给logger添加handler
logger.addHandler(fh)
logger.addHandler(ch)
# 记录一条日志


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/zmb'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://zhongmeban_share:Zhongmeban123@rds9i2oey14eccx3h4qh.mysql.rds.aliyuncs.com/zhongmeban_release3'

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
    row = result.fetchall()[0]

    jsonDict = dict(row.items())

    for k, v in jsonDict.items():
        if type(v) != type(""):
            jsonDict[k] = str(v)


    # print(json.dumps(jsonDict))

    print('------')
    return jsonDict






@app.route('/')
def hello_world():
    return 'asd1'
    # result = getNews()
    # abl = result
    # return json.dump(getNews())


@app.route('/new/<int:new_id>')
def new(new_id):
    title = getNews(new_id)
    # return 'asd'
    return Response(json.dumps(title), mimetype='application/json')

@app.route('/notify_url',methods=['POST'])
def notify():
    logger.info('heiheie----')
    logger.info(request.form)
    logger.info('heiheie----')
    print(request.form)



if __name__ == '__main__':

    getNews(1)
    # users = Product.query.all()
    # result = db.session.execute('SELECT * From t_info_news;')
    # for row in result:
        # print(row[3])
    # print(users)

    app.run()
