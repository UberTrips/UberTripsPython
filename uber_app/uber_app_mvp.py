import flask
app = flask.Flask(__name__)

# model goes here
import numpy as np
import pandas as pd
import sklearn

#MODEL GOES HERE

from sklearn.linear_model import LogisticRegression, LogisticRegressionCV


trips = pd.read_csv('/Users/HudsonCavanagh/GA_dsi-projects/UberTripPython/uber_app/non_uber_trips.csv')
trips = trips.iloc[:,1:]
trips.columns = ['weekday', 'hour', 'taxi-cs_avg_trips', 'uber_avg_trips','lyft_avg_trips', 'total_trips', 'uber_prob', 'uber_taxi_bin']
lr_basic = LogisticRegression(solver='liblinear', penalty='l2', C=0.75)

X = trips.iloc[:,0:2]

y = trips['uber_taxi_bin']
PREDICTOR =lr_basic.fit(X, y)


#http://127.0.0.1:4000/predict?hour=3&day_of_week=2
# routes go here
@app.route('/predict', methods=["POST", "GET"]) #, methods=['GET']
def predict():
    # hood_id = int(flask.request.args['hood_id'])
    hour = int(flask.request.args['hour'])
    day_of_week = int(flask.request.args['day_of_week'])

    # address = inputs['address'][0]
    # time_of_day = inputs['time_of_day'][0]

    item_basic = [hour, day_of_week]
    # item_more = np.array([day_period, hood_id,day_of_week])


    score_mvp = PREDICTOR.predict_proba(item_basic)
    results_mvp = {'Chances of an Uber': score_mvp[0][0], 'Chances of Taxi or Car Service':score_mvp[0][1]} #[0,1]
    # results_test = {'Chances of an Uber': item_basic} #[0,1]

    return flask.jsonify(results_mvp)

# alternate routes

@app.route('/page')
def page():
    with open("uber_page.html", 'r') as viz_file:
        return viz_file.read()


if __name__ == '__main__':
    HOST = '127.0.0.1'
    PORT = '4000'
    app.run(HOST, PORT)
