from flask import Flask, session, render_template
import os
import swimclub

app = Flask(__name__)
app.secret_key = "You will never guess..."

@app.get("/")
def index():
    return render_template("index.html")

def populate_data():
    if "swimmers" not in session:
        swim_files = os.listdir(swimclub.FOLDER)
        session["swimmers"] = {}
        for f in swim_files:
            name, *_ = swimclub.read_swim_data(f)
            if name not in session["swimmers"]:
                session["swimmers"][name] = []
            session["swimmers"][name].append(f)


@app.get("/swimmers")
def display_swimmers():
    populate_data()
    return str(sorted(session["swimmers"]))

@app.get("/files/<swimmer>")
def get_swimmers_files(swimmer):
    populate_data()
    return str(session["swimmers"][swimmer])

if __name__ == "__main__":
    app.run(debug=True)