# app.py
from flask import Flask, render_template, url_for, flash, redirect
from config import Config
from forms import ContactForm

app = Flask(__name__, static_url_path='/static')
app.config.from_object(Config)


@app.route('/', methods=['POST','GET'])
@app.route('/index', methods=['GET','POST'])
def index():
    form = ContactForm()
    if form.validate_on_submit():
        flash('Message Sent, I will be in touch shortly.')
        return redirect('/index')
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run()