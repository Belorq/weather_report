from flask import Flask, render_template, request
import requests
app = Flask(__name__)
html_data = ['display: block; height: 590px;', 'static\clear2.svg', 'static\\rain2.svg', 'static\snow2.svg', 'static\clouds2.svg', 'static\mist2.svg']
background = ['static\clear.mp4', 'static\\rain.mp4', 'static\snow.mp4', 'static\clouds.mp4', 'static\mist.mp4']

@app.route('/', methods=['POST', 'GET'])
def form():
    if request.method == 'POST':
        city = request.form['text']
        r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=9d00c08572aab5f4eb0ce065afde136a').json()
        try:
            main = str(r['weather'][0]['main'])
        except KeyError:
            return render_template('404.html', city = city)
        data = {'temp': str(round(int(r['main']['temp']))), 'description':str(r['weather'][0]['description']), 
                'humidity':str(r['main']['humidity']), 'wind':str(round(int(r['wind']['speed'])))}
        
        if main == 'Clear':
            return render_template('index_data.html', data = data, city = city, style = html_data[0], img = html_data[1], background = background[0])
        elif main == 'Rain' or main == 'Drizzle':
            return render_template('index_data.html', data = data, city = city, style = html_data[0], img = html_data[2], background = background[1])
        elif main == 'Snow':
            return render_template('index_data.html', data = data, city = city, style = html_data[0], img = html_data[3], background = background[2])
        elif main == 'Clouds':
            return render_template('index_data.html', data = data, city = city, style = html_data[0], img = html_data[4], background = background[3])
        elif main in ['Haze', 'Mist', 'Smoke', 'Haze', 'Dust', 'Fog', 'Sand', 'Dust', 'Ash', 'Squall', 'Tornado']:
            return render_template('index_data.html', data = data, city = city, style = html_data[0], img = html_data[5], background = background[4])
    return render_template('index.html')
    

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
