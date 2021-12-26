from flask import Flask, Response
from consts import HOSTNAME, PORT
from flask_cors import CORS

app = Flask("__name__")
CORS(app)


@app.route("/v1/test", methods=["GET"])
def test():
    return Response("this is Salt security", 200)


@app.route("/v1/health", methods=["GET"])
def health():
    return Response("Healthy", 200)


app.run(host=HOSTNAME, port=PORT)
