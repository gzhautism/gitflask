from flask import Flask, render_template

app = Flask(__name__)

book = {
    'name': '斗破苍穹',
    'author': '土豆',
    'articles': [
        {
            'id': 1,
            'title': '第一章:新手村',
            'content': '正在发育中'
        },
        {
            'id': 2,
            'title': '第二章:乱张刚',
            'content': '主角正在发育中'
        },
        {
            'id': 3,
            'title': '第三章:废物',
            'content': '主角还在发育中'
        },
    ]
}


@app.route("/")
def index():
    articles = book['articles']
    return render_template('index.html', **locals())


@app.route("/<int:pk>")
def detail(pk):
    article = None
    for a in book["articles"]:
        if a["id"] == pk:
            article = a

    return render_template('detail.html', **locals())


if __name__ == "__main__":
    app.run(debug=True)
