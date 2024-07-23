from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///names.db'
db = SQLAlchemy(app)

class Name(db.Model):
    id   = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        new_name = request.form['name']
        new_entry = Name(name=new_name)
        db.session.add(new_entry)
        db.session.commit()
        return redirect('/')
    
    all_names = Name.query.all()
    return render_template('index.html', names=all_names)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)