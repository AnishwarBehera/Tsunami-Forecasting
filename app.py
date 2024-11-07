from flask import Flask, render_template, request,url_for
import pandas as pd
import pickle
from functions import map_function, drop_columns
app = Flask(__name__, template_folder='templates')
app.static_folder = 'static'
app.static_url_path = '/static'

model = pickle.load(open('pipeline.pkl','rb'))

map_function=model['map_function']
drop_columns=model['drop_columns']
pipeline=model['pipeline']

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')



@app.route('/predict', methods=['POST'])
def predict():
    magType=request.form['algorithm']
    magnitude = float(request.form['magnitude'])
    cdi = float(request.form['cdi'])
    mmi = float(request.form['mmi'])
    sig = float(request.form['sig'])
    nst = float(request.form['nst'])
    dmin = float(request.form['dmin'])
    gap = float(request.form['gap'])
    depth = float(request.form['depth'])
    latitude = float(request.form['latitude'])
    longitude = float(request.form['longitude'])

    dd= pd.DataFrame([['M 7.0 - 18 km SW of Malango, Solomon Islands', magnitude, '22-11-2022 02:03', cdi, mmi, 'green', sig, 'us', nst, dmin, gap, magType, depth, latitude, longitude, 'Malango, Solomon Islands', 'Oceania', 'Solomon Islands']], 
                     columns=['title', 'magnitude', 'date_time', 'cdi', 'mmi', 'alert','sig', 'net', 'nst', 'dmin', 'gap', 'magType', 'depth', 'latitude','longitude', 'location', 'continent', 'country'])
     
    result = pipeline.predict(dd)
    if(result>0.5):
        result="There is a high likelihood that this site will be hit by a tsunami"
    else:
        result="There is a low probability that this area will be affected by a tsunami"

    return render_template('result.html',result=result)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8080)
