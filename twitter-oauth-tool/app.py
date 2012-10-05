#!/usr/bin/env python

from flask import Flask, redirect, request
app = Flask(__name__)

import oauth_utils

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def api(path):
    url = "https://api.twitter.com/{path}".format(path=path)
    params = dict(zip(request.args.keys(), request.args.values()))
    return redirect(oauth_utils.signed_request_url(url, **params))

if __name__ == "__main__":
    app.run()
