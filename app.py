from chatbot import chatbot
from flask import Flask, render_template, request, session, redirect
from flask_sitemap import Sitemap

app = Flask(__name__)
ext = Sitemap(app=app)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/')
def index():
    pass

@ext.register_generator
def index():
    # Not needed if you set SITEMAP_INCLUDE_RULES_WITHOUT_PARAMS=True
    yield 'index', {}

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(chatbot.get_response(userText))

if __name__ == "__main__":
    app.run(debug=True) 