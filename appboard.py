from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHMEY_DATABASE_URI'] = 'sqlite:///appt.db'
app.secret_key = 'null' # change on deployment


db = SQLAlchemy(app)


@app.route('/')

def public():
    return render_template('public_display.html')

@app.route('/add')

def add():
    return render_template('add_appt.html')

if __name__ =="__main__":
    app.run(host="0.0.0.0")