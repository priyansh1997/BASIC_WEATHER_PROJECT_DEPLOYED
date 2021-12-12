
from flask import Flask, request, jsonify, render_template
#import pickle 
import weather
import numpy as np


app=Flask(__name__)

@app.route('/')
def form():
    return render_template('index.html')

@app.route("/",methods=["POST","Get"])
def hello():
    if request.method=="POST":
        m=request.form["Morning"]
        n=request.form["Noon"]
        e=request.form["Evening"]
        ni=request.form["Night"]
        final_features=list(map(int, [m,n,e,ni]))
        wp=weather.weather_pred(final_features)
        
    return render_template("index.html",prediction=wp)


if __name__=="__main__":
         from werkzeug.serving import run_simple
         run_simple('localhost', 9000, app, use_debugger=True)



# =============================================================================
# 
# @app.route('/predict',methods=["POST"])
# def predict():
#     #for rendering results on HTML GUI
#     int_feature=[int(x) for x in request.form.values()]
#     final_features=[np.array(int_feature)]
#     prediction=model.predict(final_features)
#     output=round(prediction[0], 2)
#     
#     return render_template('index_html', prediction_text="Car_unacc {}".format(output))
# =============================================================================


