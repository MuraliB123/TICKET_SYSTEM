from flask import Flask, render_template, request, session
app = Flask(__name__)
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker

app = Flask(__name__, static_folder='static')
app.secret_key = 'mykey'


from sqlalchemy import URL, create_engine

connection_string = URL.create(
    'postgresql',
    username='muralibabu1729',
    password='k8YoTmpfr1BG',
    host='ep-round-lab-18399406.us-east-2.aws.neon.tech',
    database='ticket_system'
)

engine = create_engine(connection_string, connect_args={'sslmode': 'require'})



engine = create_engine(connection_string)
Session = sessionmaker(bind=engine)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://muralibabu1729:k8YoTmpfr1BG@ep-round-lab-18399406.us-east-2.aws.neon.tech/ticket_system'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


from models import  db, UserLogin,Ticket
db.init_app(app)
assign_id = 0

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        userid = request.form['userid']
        password = request.form['password']
        user = UserLogin.query.filter_by(id=userid, password=password).first()

        if user:
            data = "success"
            session['user_id'] = user.id
            return render_template('user_login.html',data=data)
            
        else:
            data = "Login Failed"
            return render_template('user_login.html',data = data)

    return render_template('user_login.html')

@app.route('/raise',methods=['GET','POST'])
def assign():
    if request.method == 'POST':
        raised_by = session['user_id']
        issue = request.form['issue']
        assign_to = get_assign_id()
        new_ticket = Ticket(issue_description=issue, raised_by=raised_by, assigned_to=assign_to)
        db.session.add(new_ticket)
        db.session.commit()
        message   = "your ticket has been raised"
        return render_template('ticket_raise.html',data = message)
    return render_template('ticket_raise.html')




def get_assign_id():
    global assign_id
    assign_id += 1
    if assign_id > 5:
        assign_id = 1
    return assign_id

if __name__ == '__main__':
    app.run(debug=True)