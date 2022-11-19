
from flask import Flask, request, render_template

import joblib
import requests

API_KEY = "<0NOqYz1mrPwYmf1q4QEKbH0n-tw5n_FihO7ISriqD4-D>"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

app = Flask(__name__)


# CORS(app)

@app.route('/', methods=['GET'])
def sendHomePage():
    return render_template('index.html')


@app.route('/predict', methods=['POST', 'GET'])
def predictchances():
    chances = 0

    if request.method=="POST":
        gre = int(request.form.get('GREScore'))
        toefl =int(request.form['TOEFL'])
        ur = float(request.form['Ratings'])
        sop = float(request.form['SOP'])
        lor = float(request.form['LOR'])
        Cgpa = float(request.form['CGPA'])
        research = int(request.form['Research'])
        x = [[gre, toefl, ur, sop, lor, Cgpa, research]]
        payload_scoring = {"input_data": [{"fields": [array_of_input_fields], "values": [array_of_values_to_be_scored, another_array_of_values_to_be_scored]}]}
        response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/e4c4d937-60b0-432f-a6b2-3559275dc58d/predictions?version=2022-11-19', 
        json=payload_scoring,
        headers={'Authorization': 'Bearer ' + mltoken})
        print("Scoring response")
        print(response_scoring.json())
        prediction = response_scoring.json()
        predict = round(prediction['prediction'][0]['values'][0][0]*100,3)
        print("final prediction: ",predict)
        
    return render_template('predict.html', predict = predict)

@app.route('/second_page',methods=['GET','POST'])
def second_page():
    return render_template('second_page.html')


@app.route('/third_page',methods=['GET','POST'])
def third_page():
    return render_template('third_page1.html')


if __name__ == '__main__':
    app.run(debug=True)


