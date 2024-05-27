from flask import Flask, render_template, request
from summary import summarizer

app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/submit', methods=['POST'])
def welcomes():
    # Get data from form
    name = request.form['username']
    return render_template('Login.html', name=name)



@app.route('/Login')
def login():
    return render_template('Login.html')

@app.route('/login', methods=['POST'])
def logins():
    # Get data from form
    name = request.form['username']
    return render_template('index.html', name=name)


@app.route('/signup')
def signup():
    return render_template('Login.html')

@app.route('/signup', methods=['POST'])
def signups():
    # Get data from form
    name = request.form['username']
    return render_template('signup.html', name=name)


@app.route('/signups')
def index1():
    return render_template('signup.html')

@app.route('/signups', methods=['POST'])
def indexs():
    # Get data from form
    name = request.form['username']
    return render_template('index.html', name=name)


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/analyze', methods=['GET','POST'])
def analyze():
    if request.method == 'POST':
        rawtext = request.form['rawtext']
        summary, original_text, len_orig_txt, len_summary = summarizer(rawtext)
    
    return render_template('summary.html', summary=summary, original_text=original_text, len_orig_txt=len_orig_txt, len_summary=len_summary)

if __name__ == "__main__":
    app.run(debug = True)