from flask import Flask
from flask import json
import logging

app = Flask(__name__)

# log configuration
logging.basicConfig(filename="logs/app.log", level=logging.DEBUG, format="%(asctime)s %(levelname)s %(message)s")

@app.route("/")
def hello():
    logging.info("Hello world called")
    response  = app.response_class(
        response = "Hello World"
    )
    return response

@app.route("/status")
def status():
    finalResponse = app.response_class(
        response = json.dumps({"result": "OK - Healthy"}),
        status = 200,
        mimetype = "application/json"
    )
    logging.error("%s is the response being sent", finalResponse)
    return finalResponse

@app.route("/metrics")
def metrics():
    finalResponse = app.response_class(
        response = json.dumps({
            "user": "admin",
            "data": {
                "UserCount": 140,
                "UserCountActive": 23
            }
        }),
        status = 200,
        mimetype = "application/json"
    )
    return finalResponse

if __name__ == "__main__":
    app.run(host='0.0.0.0')
