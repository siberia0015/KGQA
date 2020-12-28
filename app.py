from flask import Flask, render_template, request, jsonify
from neo_db.query_graph import query,get_KGQA_answer,get_answer_profile
from KGQA.ltp import get_target_array
app = Flask(__name__)

# 路由
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
# 进入主页
def index(name=None):
    return render_template('index.html', name = name)
# 进入检索人物关系页
@app.route('/search', methods=['GET', 'POST'])
def search():
    return render_template('search.html')
# 进入问答系统页
@app.route('/KGQA', methods=['GET', 'POST'])
def KGQA():
    return render_template('KGQA.html')
# 获取详细信息
@app.route('/get_profile',methods=['GET','POST'])
def get_profile():
    # name是前端传来的人物名
    name = request.args.get('character_name')
    json_data = get_answer_profile(name)
    return jsonify(json_data)
# 运行KGQA
@app.route('/KGQA_answer', methods=['GET', 'POST'])
def KGQA_answer():
    # question 是搜索框中输入的语句
    question = request.args.get('name')
    # json_data 是KGQA返回的结果
    # str() 将对象转化为适于人阅读的形式
    # get_target_array() 得到有关实体和关系的数组，如['贾珠','母亲','贾珠']
    # get_KGQA_answer() 返回一个数组，包含查出来的所有路径上的实体，查出实体的详细信息，查出实体的图片
    json_data = get_KGQA_answer(get_target_array(str(question)))
    return jsonify(json_data)
# 按名字搜索
@app.route('/search_name', methods=['GET', 'POST'])
def search_name():
    method = request.args.get('method')
    name = request.args.get('name')
    json_data=query(str(name), method)
    # print(json_data)
    return jsonify(json_data)
# 进入人物关系全貌页
@app.route('/get_all_relation', methods=['GET', 'POST'])
def get_all_relation():
    return render_template('all_relation.html')

if __name__ == '__main__':
    app.debug=True
    app.run()
