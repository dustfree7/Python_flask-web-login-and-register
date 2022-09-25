from flask import Flask,render_template,request

app = Flask(__name__)

#网站路由
@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('/login.html')
    else:
        print(request.form)         #接收用户通过GET形式发送的数据。
        return  '登录成功！'

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        print(request.form)         #打印用户通过表单提交的所有数据。
        user = request.form.get('username')
        passwd = request.form.get('password')
        print(user,passwd)          #可将用户信息写入文件、Excel或数据库中，实现注册功能。此处仅作打印。
        return '注册成功!'


if __name__ == '__main__':
    app.run()