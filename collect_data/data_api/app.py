from distutils.log import debug
from flask import Flask
from controllers import safety_data
import json
from flask_sqlalchemy import SQLAlchemy

"""
The purpose of this flask app is to create an api in the localhost to exchange information 
with the front end that was built in React.
"""

app = Flask(__name__)

def return_app():
    """
    Helper method that returns the app global variable for use in other files
    """
    return app

@app.route('/')
def test():
    safety_index = safety_data.return_safety_data()

    return json.dumps(safety_index)

if __name__ == "__main__":
    app.run(debug=True)