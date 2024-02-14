from flask import Flask,render_template,request
from werkzeug import secure_filename


app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/success',methods=['POST','GET'])
def success():
    if request.method=='POST':
        result=request.form
        f = request.files['file']
        f.save(secure_filename(f.filename))
        print(result)
    return render_template('success.html',result=result)
    
    

app.run(debug=True)
