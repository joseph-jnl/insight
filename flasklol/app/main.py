from flask import Flask
from flask import render_template
from sklearn.externals import joblib
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html",
                           test='')

@app.route('/predict')
def predict():
    df = pd.read_csv('lolcurrent.csv')
    pickled_rfc = joblib.load('rfc_o.pkl')
    p_current_prob = pickled_rfc.predict_proba(df[['popularity', 'winrate','banrate', 'tsr']])
    p_current = pickled_rfc.predict(df[['popularity', 'winrate','banrate', 'tsr']])
    df['changes'] = p_current
    df['buffp'] = p_current_prob[:,0]
    df['nochangep'] = p_current_prob[:,2]
    df['nerfp'] = p_current_prob[:,1]
    df['nochangep'] = p_current_prob[:,2]
    nerfs = df[df['changes']=='nerf']
    nerfs_html = nerfs.to_html()
    # data = '<table border="1" class="dataframe">\n  <thead>\n    <tr style="text-align: right;">\n      <th></th>\n      <th>name</th>\n      <th>popularity</th>\n      <th>winrate</th>\n      <th>banrate</th>\n      <th>release</th>\n      <th>tsr</th>\n      <th>changes</th>\n      <th>buffp</th>\n      <th>nochangep</th>\n      <th>nerfp</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>36</th>\n      <td>darius</td>\n      <td>9.7</td>\n      <td>51.7</td>\n      <td>9.8</td>\n      <td>1.335830e+09</td>\n      <td>149651831.0</td>\n      <td>nerf</td>\n      <td>0.03125</td>\n      <td>0.453125</td>\n      <td>0.515625</td>\n    </tr>\n  </tbody>\n</table>'

    return render_template("predict.html",
                           test='Button!!!!!!!!!', 
                           p_nerfs=nerfs_html,
                           titles = ['Nerfs'])

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)