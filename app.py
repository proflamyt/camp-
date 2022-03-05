from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/post', methods=['GET', 'POST'])
def index():
    data = request.form['input_name'] 
    password = request.form['password'] # pass the form field name as key
    print(data)
    return "Hacked"
 
