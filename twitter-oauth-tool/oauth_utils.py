#!/usr/bin/env python

import oauth2 as oauth
import time

import settings

def sign_request(url, **kwargs):
    # Set the base oauth_* parameters along with any other parameters required
    # for the API call.
    params = kwargs
    params.update({
        'oauth_version': "1.0",
        'oauth_nonce': oauth.generate_nonce(),
        'oauth_timestamp': int(time.time()),
    })

    # Set up instances of our Token and Consumer. The Consumer.key and 
    # Consumer.secret are given to you by the API provider. The Token.key and
    # Token.secret is given to you after a three-legged authentication.
    token = oauth.Token(key=settings.ACCESS_TOKEN, secret=settings.ACCESS_TOKEN_SECRET)
    consumer = oauth.Consumer(key=settings.CONSUMER_KEY, secret=settings.CONSUMER_SECRET)

    # Set our token/key parameters
    params['oauth_token'] = token.key
    params['oauth_consumer_key'] = consumer.key

    # Create our request. Change method, etc. accordingly.
    req = oauth.Request(method="GET", url=url, parameters=params)

    # Sign the request.
    signature_method = oauth.SignatureMethod_HMAC_SHA1()
    req.sign_request(signature_method, consumer, token)

    return req

def signed_request_url(url, **kwargs):
    return sign_request(url, **kwargs).to_url()

if __name__ == "__main__":
    print signed_request_url("https://api.twitter.com/1.1/users/show.json", screen_name="steveWINton")
