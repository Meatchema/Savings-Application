Hello! This project is a personal savings  goal tracker built with Python and Flask. This project was built as a personal learning exercise in full-stack web development and project creation.

About
This app allows you to create and manage personal savings goals, track deposits, and visualize your progress. It is being actively built from scratch as an independent project, using Python on the backend and HTML/CSS on the frontend.
As I progress further in this project I intend on learning more advance features to integrate into it.

Features
- Create savings goals with a target amount
- Set a starter amount for existing savings
- Log deposits toward any goal
- Track progress with a visual progress bar
- Delete goals when completed or no longer needed
- Data persists between sessions via local JSON storage

Tech Stack

Backend: Python, Flask
Frontend: HTML, CSS
Storage: JSON file



Running the App
Clone or download this repository
Navigate to the project folder in your terminal
Run the app:
   py app.py

Open your browser and go to http://127.0.0.1:5000

Project Structure
Savings Application/
│
├── app.py              # Flask backend and routes
├── data.json           # Local data storage
├── templates/
│   └── index.html      # Main page
└── static/
    └── style.css       # Styling

What I Learned so Far:

- Setting up and routing a Flask web application
- Connecting a Python backend to an HTML frontend
- Persisting data using JSON file storage
- Applying existing HTML/CSS/JS knowledge to a new framework
- Debugging and problem solving in a real project environment

Future Features

- Multiple pages (goal history, completed goals)
- Charts to visualize savings progress
- Edit existing goals
- Goal completion celebrations 🎉
- Monthly deposit calculations (date till completed)
