from flask import Flask, render_template
import requests
from datetime import datetime
MY_APIKEY="868c5469fc5add3122d3e7e8313c8f3e"
URL="https://api.openweathermap.org/data/2.5/weather"
app = Flask(__name__)
weather_params={
    "lat":"30.457677",
    "lon":"31.183214",
    "appid":MY_APIKEY,
}
@app.route('/')
def get_weather():
    response = requests.get(url=URL, params=weather_params)
    data = response.json()
    description = data["weather"][0]["description"]
    temp_infeh = int(data["main"]["temp"])
    temp = int(temp_infeh - 273.15)
    today = datetime.now()
    month = today.strftime("%b")
    day_num=today.day
    return render_template("index.html",tempereture=temp,description_text=description,mon=month,day=day_num)
if __name__ == "__main__":
    app.run(debug=True)
