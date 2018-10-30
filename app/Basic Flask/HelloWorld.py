from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
       return 'Hello World'

@app.route('/hi/<name>')
def hello1_name(name):
       return 'Hello %s!' %name

@app.route('/hi/<int:name>')
def hello2_name(name):
       return 'Hello %f!' %name

@app.route('/hi/<int:name>')
def hello3_name(name):
       return 'Hello %d!' %name


if __name__ == '__main__':
       app.run(debug = True)
