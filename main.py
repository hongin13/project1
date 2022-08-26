from ensurepip import bootstrap
import os

# flask
import flask
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, Response
import argparse
from flask_bootstrap import Bootstrap

# data
# import facemesh
# import preprocess
# import classify

DEFAULT_PORT = 5000
DEFAULT_HOST = '0.0.0.0'

def parse_args():
    parser = argparse.ArgumentParser(description='Tensorflow object detection API')

    parser.add_argument('--debug', dest='debug',
                        help='Run in debug mode.',
                        required=False, action='store_true', default=True)

    parser.add_argument('--port', dest='port',
                        help='Port to run on.', type=int,
                        required=False, default=DEFAULT_PORT)

    parser.add_argument('--host', dest='host',
                        help='Host to run on, set to 0.0.0.0 for remote access', type=str,
                        required=False, default=DEFAULT_HOST)

    args = parser.parse_args()
    return args

app = Flask(__name__)
Bootstrap(app)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jpeg'])

# facemesh.run()
# preprocess.run()
# classify.run()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/service')
def service():
    return render_template('service.html')

# from keras.models import load_model
# m3 = load_model('best_model.h')

def main():
    args = parse_args()
    app.run(host=args.host, port=args.port, debug=args.debug)
    # app.run(debug=True)
    
if __name__ == "__main__":
    main()