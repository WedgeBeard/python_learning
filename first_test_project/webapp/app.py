from flask import Flask
import os
import swimclub

app = Flask(__name__)


@app.get("/")
def index():
    return "This is a placeholder for your webpage's opening page"

if __name__ == "__main__":
    app.run()


@app.get("/swimmers")
def display_swimmers():
    swim_files = os.listdir(swimclub.FOLDER)
    swimmers = {}
    for f in swim_files:
        name, *_ = swimclub.read_swim_data(f)
        if name not in swimmers:
            swimmers[name] = []
        swimmers[name].append(f)
    return str(sorted(swimmers))