from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired, Email
from flask import Flask, render_template, request, flash, get_flashed_messages


import menu

app = Flask(__name__)
app.config['SECRET_KEY'] = 'QsEkgTF8Kk89ugF7KCV6Kv4VVb3llj3vkg3'


# class FeedbackForm(FlaskForm):
#     username = StringField(validators=[InputRequired()])
#     email = StringField(validators=[InputRequired(), Email()])
#     message = StringField(validators=[InputRequired()])


@app.route('/')
def index():
    return render_template('main.html', menu=menu.main_menu)


@app.errorhandler(404)
def pageNotFound(error):
    return render_template('page404.html', title='Страница не найдена', menu=menu.main_menu)


@app.route('/feedback', methods=['POST', 'GET'])
def feed_back():
    form = FeedbackForm()

    if request.method == 'POST':
        if len(request.form['username']) > 2:
            flash(message='Message sent.', category='success')
        else:
            flash(message='Sending error.', category='error')
    return render_template('feedback.html', menu=menu)


@app.route('/rules')
def rules():
    return render_template('rules.html', menu=menu.main_menu)


@app.route('/gran_pri')
def gran_pri():
    return render_template('gran_pri.html', menu=menu.main_menu)


@app.route('/teams')
def teams():
    return render_template('teams.html', menu=menu.main_menu)


if __name__ == '__main__':
    app.run(debug=True)
