"""@author: Yash Dani Student Id: 1001707349"""

import flask
from flask import Flask, render_template, request, jsonify
application = Flask(__name__)
application.debug = True
@application.route('/')
def first():
    # print("Index Page")
    return render_template('index.html')

@application.route('/search/', methods=['GET', 'POST'])
def search():
    text_input = request.args.get('query','')
    # print(text_input)
    import search_query
    res, highlight_query = search_query.get_results(text_input)
    # print(res[0:10])
    return render_template('display.html', result=res[0:10], highlight_q=highlight_query)

@application.route('/classify/', methods=['GET', 'POST'])
def classify():
    text_input = request.args.get('query','')
    import genre_classify
    perc, sorted_score_map = genre_classify.get_results(text_input)
    # data = {'results': query_classifier.get_results(classify_query)}
    # data = jsonify(data)
    # print(result[0:10])
    return render_template('display_classify.html', score=perc[0:6], result=sorted_score_map[0:6])

@application.route('/imgcap/', methods=['GET', 'POST'])
def caption():
    text_input = request.args.get('query','')
    # print(text_input)
    import img_query
    res, highlight_query = img_query.get_results(text_input)
    # print(res[0:10])
    return render_template('img_display.html', result=res[0:10], highlight_q=highlight_query)

if __name__ == '__main__':
#    flask run
    #application.run(host='0.0.0.0',port=int()use_reloader=False)
   application.run(use_reloader=False)