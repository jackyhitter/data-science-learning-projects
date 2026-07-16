import pickle
from flask import Flask , render_template , jsonify , request , redirect 
import numpy 
import pandas
# from sklearn.preprocessing import StandardScaler

application = Flask(__name__)
app = application 

## Importing models
ridgeModel = pickle.load(open('models/ridge.pkl', 'rb'))
stdScaler = pickle.load(open("models/scaler.pkl", 'rb'))

print("Scaler expects:", stdScaler.feature_names_in_)

@app.route('/')
def index():
    return "hip hip hurray"

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/predict/", methods=["GET", "POST"])
def predict():
        if request.method == 'POST':
            Temperature = float(request.form["Temperature"])
            RH = float(request.form["RH"])
            Ws = float(request.form["Ws"])
            Rain = float(request.form["Rain"])
            FFMC = float(request.form["FFMC"])
            DMC = float(request.form["DMC"])
            ISI = float(request.form["ISI"])
            Classes = float(request.form["Classes"])
            Region = float(request.form["Region"])
            
            NewDataScaled= stdScaler.transform([[Temperature,RH,Ws,Rain,FFMC,DMC,ISI,Classes,Region]])
            result = ridgeModel.predict(NewDataScaled)
            return render_template('home.html', result=result[0])
        else:
            return render_template('home.html')

    










if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)