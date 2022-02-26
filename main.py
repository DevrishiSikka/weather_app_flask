from flask import Flask, request, render_template
import requests

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("index.html")


@app.route('/response', methods=['POST'])
def response():
    c_name = request.form.get("c_name")
    API_KEY = 'MY_API_KEY'

    url = f'http://api.openweathermap.org/data/2.5/weather?q={c_name}&APPID={API_KEY}'
    response = requests.get(url).json()

    if response.get('cod') != 200:
        message = response.get('message', '')
        responsed = f'Error getting temperature for {c_name.title()}. Error message = {message}'
    current_temperature = response.get('main', {}).get('temp')

    if current_temperature:
        current_temperature_celsius = round(current_temperature - 273.15, 2)
        responsed = f'Current temperature of {c_name.title()} is {current_temperature_celsius} °'
    else:
        responsed = f'Error getting temperature for {c_name.title()}'
    return render_template("index.html", name=responsed)


if __name__ == '__main__':
    app.run(debug=True)
