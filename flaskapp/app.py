from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
   return render_template('index.html')


@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))



if __name__ == '__main__':
   app.run(host='0.0.0.0',port='3000',debug=False)
