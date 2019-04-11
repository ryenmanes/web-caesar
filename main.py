from flask import Flask, request
from caesar import rotate_character

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
                }}
                textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
                }}
        </style>
    </head>
    <body>
        <form method="post">
            <label for="text">Rotate by:</label>
            <input  label="" name="rot" type="text" />
            <textarea value="0" name="text">{0}</textarea>
            <input type="submit" value="Submit!" />
        </form>
    </body>
</html>
"""

@app.route("/words", methods=['POST'])
def encrypt():
    rotate = int(request.form['rot'])
    maintext = request.form['text']
    returnrotation = rotate_character(maintext, rotate)
    return form.format(returnrotation)

@app.route("/")
def index():
    return form.format('')


app.run()