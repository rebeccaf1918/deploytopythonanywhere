from flask import Flask, url_for, request, redirect, abort
import songDAO


app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World"

if __name__ == "__main__":
    app.run(debug=True)


@app.route('/TaylorSwiftSongs', methods=['GET']) #Defining route to retieve all Taylor Swift songs from the database
def getAll():
    return 'taylor'

@app.route('/TaylorSwiftSongs', methods=['GET']) #Defining route to retieve all Taylor Swift songs from the database
def getAll():
    return songDAO.getall()
    return jsonify(results) # converts the result from the database to a JSON format

@app.route('/TaylorSwiftSongs/<int:id>', methods=['GET'])
def findbyID(id):
    foundSong = songDAO.findbyID(id)
    return jsonify(foundSong)


