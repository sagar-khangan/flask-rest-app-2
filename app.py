from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import ConfigParser

import json
import os
from db_ops import  *

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
config = ConfigParser.ConfigParser()
config.read(basedir+'\\api.cfg')


@app.route("/", methods=['GET', 'POST','DELETE','PUT'])
def fun():
    db = connect(config)
    if request.method == 'GET':
       return json.dumps(fetch_data(db))

    elif request.method == 'POST':
        return json.dumps(insert_data(db,request))

    elif request.method == 'DELETE':
        if request.form['name']:
            return json.dumps(delete_data(db,request))
        else:
            return json.dumps({'message':'please provide name'})

    elif request.method =='PUT':
        if request.form['name']:
            return json.dumps(update_data(db,request))
        else:
            return json.dumps({'message':'please provide name'})

if __name__ == "__main__":
    app.run(debug= True)



