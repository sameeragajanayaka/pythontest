from flask import Flask,jsonify,request
from nrclex import NRCLex as ns
import pandas as pd
import nltk
nltk.download('punkt')
from textblob import TextBlob

app=Flask(__name__)


@app.route('/api')
def get():
#     d={}
#     result=str("sameera")
#     emotion = ns(result)
#     analysis = TextBlob(result);
#     d={}
#     m={}
#     m['fear']=str(emotion.affect_frequencies['fear'])
#     m['anger']=str(emotion.affect_frequencies['anger'])
#     m['anticip']=str(emotion.affect_frequencies['anticip'])
#     m['trust']=str(emotion.affect_frequencies['trust'])
#     m['surprise']=str(emotion.affect_frequencies['surprise'])
#     m['sadness']=str(emotion.affect_frequencies['sadness'])
#     m['disgust']=str(emotion.affect_frequencies['disgust'])
#     m['joy']=str(emotion.affect_frequencies['joy'])
#     d['Query']=str(m)
#     d['Senti']=str(analysis.polarity)+","+str(analysis.subjectivity)
#     cr = csv.reader(open('https://ai4covid.lk/analysisdata.csv',"rb"))
    df=pd.read_csv('http://ai4covid.lk/analysisdata.csv')
    a=df.to_string();
    return a



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('love')
    app.run()
