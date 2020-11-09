import sklearn.external.joblib as extjoblib
import joblib
from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')







if __name__ == "__main__":
    model=joblib.load('ModelRF')
    app.run(debug=True)