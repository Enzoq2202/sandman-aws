from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return "1Berto, 2berto, 3berto, 4berto, 5berto"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000) 
