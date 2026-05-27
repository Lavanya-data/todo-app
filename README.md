# To-Do App — Python Flask

A clean, responsive To-Do web application built with Python and Flask.

**Developer:** Setti Lavanya  
**Branch:** B.Tech CSDS, QIS College of Engineering & Technology  
**Tech Stack:** Python · Flask · HTML · CSS · Jinja2

---

##  Features

-  Add new tasks
-  Mark tasks as Done / Undo
-  Delete individual tasks
-  Clear all completed tasks at once
-  Live stats: Total / Done / Pending count
-  Responsive design — works on mobile too

---

##  How to Run Locally

### Step 1 — Install Python
Make sure Python 3 is installed. Check with:
```bash
python --version
```

### Step 2 — Install Flask
```bash
pip install flask
```

### Step 3 — Run the App
```bash
python app.py
```

### Step 4 — Open in Browser
Go to: **http://127.0.0.1:5000**

---

##  Project Structure

```
todo-app/
│
├── app.py              # Main Flask application (routes, logic)
└── templates/
    └── index.html      # Frontend (HTML + CSS + Jinja2 template)
```

---

##  Concepts Used

| Concept | Where Used |
|---|---|
| Flask routing (`@app.route`) | All pages |
| Jinja2 templating (`{% for %}`, `{% if %}`) | index.html |
| HTTP methods (GET / POST) | Add task form |
| Python lists & dicts | Task storage |
| URL parameters (`<int:task_id>`) | Toggle & Delete routes |
| CSS Flexbox | Layout |
| Gradient styling | UI design |

---

##  Future Improvements

- [ ] Save tasks to a database (SQLite)
- [ ] User login / multiple users
- [ ] Due dates and priority levels
- [ ] Deploy to Render.com (free hosting)

---

