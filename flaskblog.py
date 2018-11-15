from flask import Flask, render_template, url_for, flash, redirect
from forms import RegristrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '9e88cbb84d21b4716b87a2c26fc85f12'

posts = [
    {
        'author': 'Seth Larkin',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'November 14, 2018'
    },
    {
        'author': 'James Dean',
        'title': 'Blog Post 2',
        'content': 'James\' post content',
        'date_posted': 'November 15, 2018'
    }
]


@app.route('/')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegristrationForm()
    if form.validate_on_submit():
        flash(f'Account Created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)
