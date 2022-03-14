from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

# 加载项目配置
class Config(object):
    # 开启debug 模式
    Debug = True

app.config.from_object(Config)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
