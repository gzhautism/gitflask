from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '欢迎来到Flask'


@app.route('/<int:pk>')
def detail(pk):
    return f'欢迎来到{pk}'


if __name__ == "__main__":
    # debug=True可以启动热更新 代码发生变化不用重启服务器
    app.run(host='192.168.11.48', port=6897, debug=True)
