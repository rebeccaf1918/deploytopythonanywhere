from flask import Flask, url_for, request, redirect, abort

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World"

if __name__ == "__main__":
    app.run(debug=True)



@app.route('/TaylorSwiftSongs', methods=['GET']) #Defining route to retieve all Taylor Swift songs from the database
def getAll():
    return songDAO.getall()
    return jsonify(results) # converts the result from the database to a JSON format

@app.route('/TaylorSwiftSongs/<int:id>', methods=['GET'])
def findbyID(id):
    foundSong = songDAO.findbyID(id)
    return jsonify(foundSong)

@app.route('/TaylorSwiftSongs', methods=['POST'])
def create():
    
    if not request.json: #if the request doesn't have JSON data, it aborts and shows a 400 Bad Request error
        abort(400) 

    song = {
        "Title": request.json['Title'],
        "Album": request.json['Album'],
        "Genre": request.json['Genre'],
        "Chart Position": request.json['Chart Position']

    }                     

    addedSong = songDAO.create(song)
    return jsonify(addedSong)
       




