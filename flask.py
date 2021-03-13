mport tempfile
import requests
from werkzeug.utils import secure_filename
from flask import Flask
from flask import request 
from flask import redirect

# list of cors urls needed because of google amp caching 

whitelist = ['http://www.vivlaw.ca','https://www.vivlaw.ca', 'http://www.vivlaw.ca.cdn.ampproject.org', 'https://www.vivlaw.ca.cdn.ampproject.org', 'http://www.vivlaw.ca.amp.cloudflare.com', 'https://www.vivlaw.ca.amp.cloudflare.com','https://cdn.ampproject.org']

def send Email(request): 
    def add_cors_headers(response):
        r = request.referrer[:-1]
        if r in whitelist:
            response.headers.add('Access-Control-Allow-Origin', r)
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
            response.headers.add('Access-Control-Allow-Headers', 'Cache-Control')
            response.headers.add('Access-Control-Allow-Headers', 'X-Requested-With')
            response.headers.add('Access-Control-Allow-Headers', 'Authorization')
            response.headers.add('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, DELETE')
        return response

# processing form fields     
    fields = {}
    data = request.form.to_dict()
    for x in data:
        fields[x] = data[x]

    for name in data: 
        name = data["name"]
   
    requests.post("https://api.mailgun.net/v3/www.vivlaw.ca/messages",
    auth=("api", "your mailgun api"),
    data={"from": "New Contact Form <mailgun@vivlaw.ca>",
    "to": ["vivekdavidv@gmail.com", "cteleshlaw@gmail.com",],
    "subject": "Hello",
    "text": fields[x] + name })

    return "ok" 
