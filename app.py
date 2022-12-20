from flask import Flask, render_template, request
app = Flask(__name__)

import requests

# url = "https://weather-by-api-ninjas.p.rapidapi.com/v1/weather"

# querystring = {"city":"Seattle"}

# headers = {
# 	"X-RapidAPI-Key": "1932b0b216msh56e009c8dbf031bp156e3ejsn285cfa68e6a9",
# 	"X-RapidAPI-Host": "air-quality-by-api-ninjas.p.rapidapi.com"
# }

# response = requests.request("GET", url, headers=headers, params=querystring)

# print(response.text)

@app.route('/', methods=['GET', 'POST'])
def weather():
    if request.method=='POST':
        city_name = (request.form['city'])


        r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=98ee41518e78515937eb4616f2460916')

		# read the json object
        Json_object = r.json()
        temprature = float(Json_object['main']['temp'])
        temp_min = float(Json_object['main']['temp_min'])
        temp_max = float(Json_object['main']['temp_max'])
        humidity = float(Json_object['main']['humidity'])
        sunrise = float(Json_object['sys']['sunrise'])
        sunset = float(Json_object['sys']['sunset'])
        pressure = float(Json_object['main']['pressure'])
		
        return render_template('index.html',sunrise=sunrise,sunset=sunset, temprature=temprature, humidity=humidity, pressure=pressure, city_name=city_name,temp_min=temp_min,temp_max=temp_max )

    # return "hello world"




if __name__ == "__main__":
    app.run(debug=True)    