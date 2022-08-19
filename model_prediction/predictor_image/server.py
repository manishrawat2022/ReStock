from flask import Flask
from flask import jsonify, request

app = Flask(__name__)
 
@app.route('/predict', methods = ['POST'])
def predict():
    instances = request.json["instances"]

    predictions = []
    for instance in instances:
        predictions.append(0.0)
    
    response = {"predictions": predictions}
    return jsonify(response)

@app.route('/health', methods = ['GET'])
def health():
    return 'Success'

# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(host="0.0.0.0", port = 8080)