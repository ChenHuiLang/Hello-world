from flask import Flask, request, Response
import requests
'19.134.193.63:8080/app/index.html#/HomePage'
app = Flask(__name__)

r'''‪C:\Users\CHL\Desktop\timg.jpg'''


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        b = request.form['name']
        return '<h1>hi, %s</h1>' % b
    a = request.args.get('name')
    return '<h1>Hello %s!</h1>' % a


@app.route('/images/<name>')
def user(name):
    path = 'C:/Users/CHL/Desktop/picture/' + name

    with open(path, 'rb') as f:
        img = f.read()
        print(type(img))
    return Response(img, mimetype='mimetype')


if __name__ == '__main__':
    app.run(debug=True)
