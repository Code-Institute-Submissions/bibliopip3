
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


#LINK TO BOOKX_TEMPLATEX.html
@app.route('/Quiet_T1')
def Quiet_T1():
    return render_template("Quiet_T1.html")
    
@app.route('/Time_T2')
def Time_T2():
    return render_template("Time_T2.html")
    
@app.route('/Garden_T3')
def Garden_T3():
    return render_template("Garden_T3.html")    
    
    
#FORM USER INPUT
@app.route('/', methods=['POST'])
def getvalue():
    searchbox = request.form['searchbox']
    bookTitle=['Quiet','A Brief History of Time', 'The Secret Garden']
    if searchbox == bookTitle[0]:
        return render_template('searchResults.html', userinput=searchbox, searchResult1=bookTitle[0], searchResult2="", searchResult3=bookTitle[2])
    return render_template('searchResults.html', userinput=searchbox, )



#DEBUGGING
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)

