from flask import Flask, json,jsonify, request
from flask_sqlalchemy import SQLAlchemy
import datetime, requests
from flask_cors import CORS

db=SQLAlchemy()
app = Flask(__name__)
CORS(app)
app.config['JSON_SORT_KEYS']=False

POSTGRES = {
    'user' : 'postgres',
    'pw'   : 'musafirakhirzaman',
    'db'   : 'avere',
    'host' : 'localhost',
    'port' : '5432'
}

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

db.init_app(app)

from src.routes.employee import createEmployee, getProfil, login
from src.routes.leave_request import approveLeaveRequest, getLeave_history, getLeave_request
from src.routes.etc import addHoliday

@app.route('/')
def main():
    return 'tes koneksi'