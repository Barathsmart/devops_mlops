from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hello/<user>')
def hello_name(user):
   return render_template('hello_01.html', name = user)

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=1234, debug = True)


# Ref: 
#   https://www.tutorialspoint.com/