from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
  return("Hello World. - A & S.")


if __name__ == '__main__':
    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
    app.run() 
