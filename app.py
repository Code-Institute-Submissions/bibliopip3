
import os
from flask import Flask, render_template, url_for, request

app = Flask(__name__)



# NAVIGATION
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/searchResults')
def searchResults():
    return render_template("searchResults.html")

IMAGES_FOLDER = os.path.join('static', 'images')
app.config['UPLOAD_FOLDER'] = IMAGES_FOLDER

@app.route('/catalogue')
def catalogue():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'Quiet.png')
    return render_template("catalogue.html", user_image = full_filename)
    
    
#FORM USER INPUT
@app.route('/', methods=['POST'])
def getvalue():
    searchbox = request.form['searchbox']
    return render_template('searchResults.html', searchbox=searchbox)

#DEBUGGING
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)

