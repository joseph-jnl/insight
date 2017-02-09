from flask import Flask
from flask import render_template
# from sklearn.externals import joblib
# import xgboost as xgb
# from xgboost.sklearn import XGBClassifier
import pandas as pd
from flask import request

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html",
                           test='')


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    champ = request.args.get('champ', '')
    nerfs = pd.read_csv('./static/data/graph_nerfs_all.csv')
    dfn = nerfs[['dates', str.lower(champ)]]
    dfn.to_csv('./static/data/champn.csv', index=False)
    buffs = pd.read_csv('./static/data/graph_buffs_all.csv')
    dfb = buffs[['dates', str.lower(champ)]]
    dfb.to_csv('./static/data/champb.csv', index=False)

    return render_template('predict.html', champ=champ)

    # df = pd.read_csv('lolcurrent.csv')
    # xgbc = joblib.load('xgbc.dat') 
    # p_xgb_o = xgbc.predict(df[['popularity', 'winrate', 'banrate',
    #                             'tsr', 'ts_buff', 'ts_nerf', 'vpop', 'vbr', 'vwr']].as_matrix())
    # prob_xgb_o = xgbc.predict_proba(df[['popularity', 'winrate', 'banrate', 'tsr', 'ts_buff', 'ts_nerf', 'vpop','vbr', 'vwr']].as_matrix())
    # dfp = pd.DataFrame(p_xgb_o, columns=['changes'])

    # dfn = pd.DataFrame(df.iloc[dfp[dfp['changes'] == 'nerf'].index]['name'])
    # nerfs_html = dfn.transpose().to_html(index=False)

    # dfb = pd.DataFrame(df.iloc[dfp[dfp['changes'] == 'buff'].index]['name'])
    # buffs_html = dfb.transpose().to_html(index=False)

    # # Format probabilities for predicted nerfs
    # df_nerf_probs = pd.read_csv('lolcurrent_nerf_probs.csv')
    # champs_nerf = list(dfn['name'].values)
    # champs_nerf.append('dates')
    # df_nerf_probs = df_nerf_probs[champs_nerf]
    # df_nerf_probs.to_csv('graph_nerfs.csv', index=False)

    # # Format probabilities for predicted buffs
    # df_buff_probs = pd.read_csv('lolcurrent_buff_probs.csv')
    # champs_buff = list(dfb['name'].values)
    # champs_buff.append('dates')
    # df_buff_probs = df_buff_probs[champs_buff]
    # df_buff_probs.to_csv('graph_buffs.csv', index=False)



    # pickled_rfc = joblib.load('rfc_o.pkl')
    # p_current_prob = pickled_rfc.predict_proba(df[['popularity', 'winrate','banrate', 'tsr']])
    # p_current = pickled_rfc.predict(df[['popularity', 'winrate','banrate', 'tsr']])
    # df['changes'] = p_current
    # df['buffp'] = p_current_prob[:,0]
    # df['nochangep'] = p_current_prob[:,2]
    # df['nerfp'] = p_current_prob[:,1]
    # df['nochangep'] = p_current_prob[:,2]
    # nerfs = df[df['changes']=='nerf']
    # nerfs_html = nerfs.to_html()
    # data = '<table border="1" class="dataframe">\n  <thead>\n    <tr style="text-align: right;">\n      <th></th>\n      <th>name</th>\n      <th>popularity</th>\n      <th>winrate</th>\n      <th>banrate</th>\n      <th>release</th>\n      <th>tsr</th>\n      <th>changes</th>\n      <th>buffp</th>\n      <th>nochangep</th>\n      <th>nerfp</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>36</th>\n      <td>darius</td>\n      <td>9.7</td>\n      <td>51.7</td>\n      <td>9.8</td>\n      <td>1.335830e+09</td>\n      <td>149651831.0</td>\n      <td>nerf</td>\n      <td>0.03125</td>\n      <td>0.453125</td>\n      <td>0.515625</td>\n    </tr>\n  </tbody>\n</table>'


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)