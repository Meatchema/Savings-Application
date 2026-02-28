from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)
DATA_FILE = "data.json"

def load_goals():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_goals(goals):
    with open(DATA_FILE, "w") as f:
        json.dump(goals, f, indent=2)

@app.route("/")
def index():
    goals = load_goals()
    return render_template("index.html", goals=goals)

@app.route("/add", methods=["POST"])
def add_goal():
    goals = load_goals()
    name = request.form["name"]
    target = float(request.form["target"])
    goals.append({"name": name, "target": target, "saved": 0})
    save_goals(goals) # Save updated goals 
    return redirect(url_for("index")) # Redirect to the main page after adding a goal

@app.route("/deposit", methods=["POST"])
def deposit():
    goals = load_goals()
    name = request.form["name"]
    amount = float(request.form["amount"])
    for goal in goals:
        if goal["name"] == name:
            goal["saved"] += amount
            break
    save_goals(goals) # Save updated goals after deposit
    return redirect(url_for("index")) # Redirect to the main page after depositing



if __name__ == "__main__":
    app.run(debug=True)