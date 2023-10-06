from flask import Flask,render_template,request,jsonify,request,make_response
from flask_cors import CORS,cross_origin
from text_summary import summarizer

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'application/json'
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/')
@cross_origin()
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['GET','POST'])
@cross_origin()
def analyze():
    if request.method == 'POST':
        rawtext_1 = request.get_json(force=False, silent=False, cache=True)
        rawtext = rawtext_1 ['text']
        # new_todo = Todo(content=todo_data['content'])
        summary,original_txt,len_orig_text,len_summary = summarizer(rawtext)
        
    # return jsonify(
    #     {
    #         'summary':summary,
    #         'original_txt':original_txt,
    #         'len_orig_text':len_orig_text,
    #         'len_summary':len_summary
    #     }
    # )
    return jsonify({'summary':summary})

# @app.route('/analyze', methods=['GET','POST'])
# def analyze():
#     if request.method == 'POST':
#         rawtext =request.form['rawtext']
#         summary,original_txt,len_orig_text,len_summary = summarizer(rawtext)

#     return render_template('summary.html',summary=summary,original_txt=original_txt,len_orig_text=len_orig_text,len_summary=len_summary)


if __name__ == "__main__":
    app.run(debug=True,port=8000)


def _build_cors_preflight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response

def _corsify_actual_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response