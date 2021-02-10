import numpy as np
from flask import Flask, request, render_template
import json
import pickle

app = Flask(__name__)

# Loading prediction model
model = pickle.load(open('classifier.pkl', 'rb'))


def __process_gui_input(request_form_values):
    ''' Processes input for /api_predict
    '''
    return [np.array([float(x) for x in request_form_values])]


def __process_input(request_data: str) -> np.array:
    ''' Processes input for /api_predict
    '''
    return np.asarray(json.loads(request_data)['inputs'])


@app.route('/')
def home():
    ''' Shows the HTML GUI where a user can start entering input for prediction
    '''
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''

    input_params = __process_gui_input(request.form.values())

    prediction = model.predict(input_params)

    output = round(prediction[0], 3)

    return render_template('index.html', prediction_text='The house price should be $ {}'.format(output))


@ app.route('/api_predict', methods=['POST'])
def api_predict() -> str:
    ''' For direct API calls through request
    '''
    input_params = __process_input(request.data)
    try:
        prediction = model.predict(input_params)
        print(prediction)
    except:
        return json.dumps({'error': 'PREDICTION FAILED'}), 400

    return json.dumps({"Predicted house prices": list(prediction.tolist())})


if __name__ == '__main__':
    app.run(debug=False)
