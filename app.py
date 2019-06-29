from flask import Flask, render_template, request
import mlpC
import numpy as np

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])

def send():
    if request.method == 'POST':
        age = float(request.form['age'])
        preg = float(request.form['preg'])
        glu = float(request.form['glu'])
        bp = float(request.form['bp'])
        st = float(request.form['st'])
        ins = float(request.form['ins'])
        bmi = float(request.form['bmi'])
        dpf = float(request.form['dpf'])
        w = np.array([age,preg,glu,bp,st,ins,bmi,dpf]).reshape(-1,1).T
        res = mlpC.mlp.predict(w)
        
        if res[0] == 1:
            result = "Positive"
        else:
            result = "Negative"
        
        return render_template("out.html", outcome=result)
    
    return render_template("index.html")


if __name__ == "__main__":
    app.run()