import flask
app = flask.Flask(__name__)

# model goes here
import numpy as np
import pandas as pd
import sklearn

#MODEL GOES HERER

# df = pd.read_csv('/Users/HudsonCavanagh/Documents/titanic.csv') #training data

# # Create dummies and drop NaNs
# df['Sex'] = df['Sex'].apply(lambda x: 0 if x == 'male' else 1)
# df = df[include].dropna()
#
# X = df[['Pclass', 'Sex', 'Age', 'Fare', 'SibSp']]
# y = df['Survived']

# PREDICTOR = .75


#
# routes go here
@app.route('/predict', methods=["POST", "GET"]) #, methods=['GET']
def predict():
    return "hello"
    #mvp input below - commented out future inputs

    #
    hood_id = int(flask.request.args['hood_id'])
    day_period = flask.request.args['day_period']
    day_of_week = flask.request.args['day_of_week']

    # address = inputs['address'][0]
    # time_of_day = inputs['time_of_day'][0]


    item_mvp = np.array([day_period, hood_id,day_of_week])


    # item = np.array([address, time_of_day, fare, sibsp])
    # score_mvp = PREDICTOR.predict_proba(item_mvp)
    # score = PREDICTOR.predict_proba(item)
    # results_mvp = {'survival chances': score_mvp[0,1]}


    fake_results = {'taxi_prob':list(item_mvp)}
    return flask.jsonify(fake_results)

# alternate routes

@app.route('/page')
def page():
    with open("uber_page.html", 'r') as viz_file:
        return viz_file.read()


@app.route('/result', methods=['POST', 'GET'])
def result():
    '''Gets prediction using HTML form'''
    if flask.request.method == 'POST':
        inputs = flask.request.form
        #mvp input below - commented out future inputs
        hood_id = inputs['hood_id'][0]
        day_period = inputs['day_period'][0]
        # address = inputs['address'][0]
        # time_of_day = inputs['time_of_day'][0]
        item_mvp = np.array([day_period, hood_id])
        # item = np.array([address, time_of_day, fare, sibsp])
        score_mvp = PREDICTOR.predict_proba(item_mvp)
        # score = PREDICTOR.predict_proba(item)
        results_mvp = {'survival chances': score_mvp[0,1]}
        fake_results = {'taxi_prob':.7}
        return flask.jsonify(fake_results)


if __name__ == '__main__':
    HOST = '127.0.0.1'
    PORT = '4000'
    app.run(HOST, PORT)
