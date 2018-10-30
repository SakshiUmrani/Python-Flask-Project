from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
       user = {'username': 'Daneil'}
       posts = [
              {
                     'author': {'username': 'Daniel'},
                     'body': 'Beautiful day in Srilanka!'
              },
              {
                     'author': {'username': 'Amar'},
                     'body': 'Tiger Zinda Hai movie was so cool!'
              }
       ]
       return render_template('post.html', user = user , posts = posts)

if __name__ == '__main__':
       app.run(debug = True)
