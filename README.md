# Deploying Machine Learning Models 
This is a project to help me memorize and implement learned material about how ML Models are deployed in production using Flask API.

The project uses scikit-learn Boston house prices toy dataset. The dataset that do require to download any file from some external website. Read more about it [here](https://scikit-learn.org/stable/datasets/toy_dataset.html#boston-dataset)

## Project Structure
This project has three major parts :
1. `model.py` contains code for the machine learning model to predict Boston city house prices.
2. `app.py` contains Flask APIs that receive attrubute details through GUI or API calls, computes the precited value based on the model and returns it.
3. `templates` contains the HTML template to allow user to enter attribute values for one house.

## Running the project
The project is hosted by Heroku and the model can be accessed via HTML GUI and via direct API calls.
1. To visit the website simply go to [/predict](https://aqueous-journey-74715.herokuapp.com/predict) and enter atrribute values to get a price prediction for one house. The input fields accept only float or int values and will and the website will crash if anything else is entered.
4. You can also send direct POST requests to [/api_predict](https://aqueous-journey-74715.herokuapp.com/api_predict) FLask API using Python's inbuilt request module. <br>
Below are some examples of how to run a command to send the request with some pre-popuated values. <br>
Python code:
```
import requests
import json

BASE = 'http://127.0.0.1:5000/api_predict'

data = [[0.55778, 0.0, 21.89, 0.0, 0.624,
         6.335, 98.2, 2.1107, 4.0, 437.0, 21.2, 394.67, 16.96],
        [6.1510, 0.0, 5.1900, 0.0, 5.1500, 5.9680, 5.8500,
            4.8122, 5.0000, 2.2400, 2.0200, 3.9690, 9.2900],
        [1.3554, 1.2500, 6.0700, 0.0000, 4.0900, 5.5940, 3.6800,
            6.4980, 4.0000, 3.4500, 1.8900, 3.9690, 1.3090]]

response = requests.post(BASE,  data=json.dumps({"inputs": data}))
print(json.loads(response.text))
```
Result:
```
>> {'predicted_class': [17.105408522367703, 26.040893257381757, 24.930181831843417]}
```
Postmam POST request:
```
{"inputs": [[0.55778, 0.0, 21.89, 0.0, 0.624,
         6.335, 98.2, 2.1107, 4.0, 437.0, 21.2, 394.67, 16.96],
        [6.1510, 0.0, 5.1900, 0.0, 5.1500, 5.9680, 5.8500,
            4.8122, 5.0000, 2.2400, 2.0200, 3.9690, 9.2900],
        [1.3554, 1.2500, 6.0700, 0.0000, 4.0900, 5.5940, 3.6800,
            6.4980, 4.0000, 3.4500, 1.8900, 3.9690, 1.3090]]}
```
Result:
``` 
{"Predicted house prices": [17.105408522367703, 26.040893257381757, 24.930181831843417]}
```
