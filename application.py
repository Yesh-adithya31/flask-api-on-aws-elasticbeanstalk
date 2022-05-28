from flask import Flask
from flask import jsonify,make_response
from flask import Blueprint, request
import json
import pyodbc


conn = pyodbc.connect('Driver={SQL Server};Server=tcp:finalresearchdbserver.database.windows.net,1433;Database=SuperMarket;Uid=imesha;Pwd=Mitb@1018;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
 

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Test"

@app.route('/viewExample')
def createExample():
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM product')
        rows = [x for x in cursor]
        cols = [x[0] for x in cursor.description]
        songs = []
        for row in rows:
            song = {}
            for prop, val in zip(cols, row):
                song[prop] = val
            songs.append(song)
        # Create a string representation of your array of songs.
        songsJSON = json.dumps(songs)
        return songsJSON
    except Exception as e:
        return f"An Error Occured: {e}"
