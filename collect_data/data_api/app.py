from distutils.log import debug
from flask import Flask

"""
The purpose of this flask app is to create an api in the localhost to exchange information 
with the front end that was built in React.
"""

app = Flask(__name__)

@app.route('/')
def test():
    return 'Some text'

if __name__ == "__main__":
    app.run(debug=True)