'''
flask app to host my bio

Develop -> test -> deply -> test
'''

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index_page():
    "The search page"
    return "Hello..it's Nilaya"

#----START OF SCRIPT
if __name__=='__main__':
    app.run(host='0.0.0.0',port=6464)