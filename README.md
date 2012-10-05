# Twitter OAuth Tool

Make OAuth'd requests to version 1.1 of Twitter's API.
Supports JSON-P.

## Installation

Clone:

    $ git clone git@github.com:swinton/twitter-oauth-tool.git .

Install requirements:

    $ pip install -r requirements.txt

## Usage

Create a settings.py, containing your OAuth details, e.g.

```python
ACCESS_TOKEN = "{{ACCESS_TOKEN}}"
ACCESS_TOKEN_SECRET = "{{ACCESS_TOKEN_SECRET}}"
CONSUMER_KEY = "{{CONSUMER_KEY}}"
CONSUMER_SECRET = "{{CONSUMER_SECRET}}"
```

Run the app:

    $ ./twitter-oauth-tool/app.py 
     * Running on http://127.0.0.1:5000/

Make OAuth'd requests to the Twitter API:

    $ curl -L "http://127.0.0.1:5000/1.1/users/show.json?screen_name=steveWINton"
    {"id":9685602,"id_str":"9685602","name":"Steve Winton","screen_name":"steveWINton", ... }

The tool also supports JSON-P:

    curl -L "http://127.0.0.1:5000/1.1/users/show.json?screen_name=steveWINton&callback=my_callback"
    my_callback({"id":9685602,"id_str":"9685602","name":"Steve Winton","screen_name":"steveWINton", ... }

## Contact

@[steveWINton](https://twitter.com/steveWINton).