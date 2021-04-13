import flask
import json
from flask import request
app = flask.Flask(__name__)
todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
] 
   

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text=flask.jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body=request.data
    return "request"

json.loads = json.loads(original_string)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)