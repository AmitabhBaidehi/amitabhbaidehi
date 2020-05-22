from flask import Flask # importing Flask class from flask library 

app=Flask(__name__)

@app.route('/') ##url of the website (using decorator)
def home():
    return "Home Page !"
    
@app.route('/about/') ##url of the website (using decorator)
def about(): ##fuction name
    return "Website Content goes here !" ## content

if __name__ =="__main__":
    app.run(debug=True)