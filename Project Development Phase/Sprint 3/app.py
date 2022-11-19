
from flask import Flask, request, render_template

import joblib

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
        research = float(request.form['Research'])
        x = [[gre, toefl, ur, sop, lor, Cgpa, research]]
        model = joblib.load('University.pkl')
        chances = model.predict(x)[0]
    return render_template('predict.html', predict=chances)

@app.route('/second_page',methods=['GET','POST'])
def second_page():
    return render_template('second_page.html')


@app.route('/third_page',methods=['GET','POST'])
def third_page():
    return render_template('third_page1.html')


if __name__ == '__main__':
    app.run(debug=True)


