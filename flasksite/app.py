from flask import Flask


app=Flask(__name__)

@app.route('/')
def home():
    return "<h1>hello guyssss</h1>"



@app.route('/about/<name>')
def about(name):
    return "<h1>name is: "+name+"</h1>"
    


@app.route('/contact/<int:num>')
def contact(num):
    return "<h1>number is :%d</h1>"%num


    

app.run(debug=True)