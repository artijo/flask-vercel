from flask import Flask,render_template,request,session


app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello Flask!</h1>"



if __name__ == "__main__":
    app.run()