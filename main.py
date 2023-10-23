from flask import Flask, render_template, request
import numpy as np
import joblib as jb
import pickle

app = Flask(__name__)
with open('rf.pkl', 'rb') as file:
        model = pickle.load(file)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get the user input from the form
        input_data = np.array([float(request.form['Status']), 
                               float(request.form['Province']), float(request.form['Degree']), float(request.form['Diploma']), 
                               float(request.form['Home_lang']), float(request.form['Science']), float(request.form['Female']), 
                               float(request.form['Birthyear']), float(request.form['Tenure_log'])])
        # input_data = np.log(input_data)
        # Use the model to make a prediction
        prediction = model.predict([input_data])
        # prediction = np.exp(prediction)
        prediction = np.around(prediction,2)


        # Return the prediction to the user
        return render_template('results.html', prediction=prediction[0])

if __name__ == '__main__':
    app.run(debug=True)
