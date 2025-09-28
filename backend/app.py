from flask import Flask,jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/getMyInfo')
def getMyInfo():
    value = {
        "name": "Lizbeth",
        "lastname": "Grisales",
        "socialMedia":
        {
            "facebookUser": "lizbethgricasc",
            "instagramUser": "lizgrisalesc",
            "xUser": "LIZGRICAS",
            "linkedin": "lizbeth-grisales-castro",
            "githubUser": "LIZGRICAS"
        },
        "blog": "https://lizcreative.netlify.app/",
        "author": "Liz Gricas"
    }

    return jsonify(value)

if __name__ == '__main__':
    app.run(port=5000)