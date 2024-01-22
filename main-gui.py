from flask import Flask, render_template
from main import generateTab, groupeur

# flask --app main-gui run

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/search')
def searchCenter():
    return render_template('search.html')

@app.route('/search/<item>')
def search(item: str):
    item.replace("%20", ' ')
    tab = generateTab(item)
    tab = groupeur(tab)
    return render_template('list.html',item=item, tab=tab)