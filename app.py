from flask import *
from Model import prediction
import pandas as pd

app = Flask(__name__)

@app.route('/')

def home():
    return render_template("index.html")

@app.route('/',methods = ['POST', 'GET'])
def pred():
   if request.method == 'POST':
       jy_date = request.form["j_date"]
       jy_time = request.form["j_time"]
       sour = request.form["s"]
       dest = request.form["d"]
       comp = request.form["a"]
       stps = int(request.form["st"])
       jy_dur = request.form["j_d"]
       adps = request.form["adp"]

       x = int(prediction(jy_dur , jy_date , jy_time , stps , comp , sour , dest , adps)[0])
       x  = round(x , 2)
       return render_template("index.html" , prediction_value =  f"Approximate Cost of ₹{x}" , text_output = f"For {comp.upper()} flight from {sour.upper()} to {dest.upper()} on {jy_date} at {jy_time} Hrs with {stps} stops and additional pakage of {adps.capitalize()}  with total flight time of {jy_dur} Hrs")


if __name__ =='__main__':
    app.run(debug = True)
