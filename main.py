import json
from flask import Flask


app = Flask(__name__)
@app.route('/')
def index():
    return json.dumps({'name': 'Defi Nugraheni','email': 'defingrhni23@gmail.com'})
app.run()