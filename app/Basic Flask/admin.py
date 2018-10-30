from flask import Flask, redirect, url_for,render_template
app = Flask(__name__)

@app.route('/')
def index():
       return render_template("temp.html")

@app.route('/admin')
def hello_admin():
       return 'Administrator Area, guest not allowed'

@app.route('/guest/<guest>')
def hello_guest(guest):
       return 'Guest User %s not having admin rights' %guest

@app.route('/user/<name>')
def hello_user(name):
       if name == 'admin':
              return redirect(url_for('hello_admin'))
       else:
              return redirect(url_for('hello_guest' , guest = name))

if __name__ == '__main__':
       app.run(debug = True)

       
