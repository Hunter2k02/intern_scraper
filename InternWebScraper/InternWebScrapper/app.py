import sys
from flask import Flask, render_template
from Scrapper import Scrapper
import json

sys.path.append("C:/Users/Szymon/Desktop/scrapper")

app = Flask(__name__)

@app.route("/")
def Scrapper_main():

    scrap = Scrapper()
    scrap.json()
    with open("plik.json", 'r', encoding = "UTF-8") as file:
        content = json.load(file)
        
    return render_template("index.html", content=content)

if __name__ == "__main__":
    app.run(debug=True) 