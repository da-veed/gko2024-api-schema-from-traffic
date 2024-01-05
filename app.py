from logging.config import dictConfig

import requests
import os
from dotenv import load_dotenv
from flask import Flask, Response, request
from flask_cors import CORS

from src.consts.directories import ROOT_DIR

load_dotenv(ROOT_DIR / ".env")
API_HOST = os.getenv("PROXY__API_HOST")

app = Flask(__name__)
CORS(app)

dictConfig(
    {
        "version": 1,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
            }
        },
        "handlers": {
            "wsgi": {
                "class": "logging.StreamHandler",
                "stream": "ext://flask.logging.wsgi_errors_stream",
                "formatter": "default",
            }
        },
        "root": {"level": "INFO", "handlers": ["wsgi"]},
    }
)


@app.route("/<path:path>", methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"])
def redirect_to_host(path):
    global API_HOST
    final_url = request.url.replace(request.host_url, API_HOST)
    res = requests.request(
        method=request.method,
        url=final_url,
        headers={k: v for k, v in request.headers if k.lower() != "host"},
        data=request.get_data(),
        allow_redirects=False,
    )

    excluded_headers = ["content-encoding", "content-length", "transfer-encoding", "connection"]
    headers = [(k, v) for k, v in res.raw.headers.items() if k.lower() not in excluded_headers]

    response = Response(res.content, res.status_code, headers)

    return response


if __name__ == "__main__":
    app.run(debug=False)
