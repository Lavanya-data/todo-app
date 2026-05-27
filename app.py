# ============================================================
#  TO-DO APP  —  Built with Python Flask
#  Developer : Setti Lavanya
#  Tech Stack: Python, Flask, HTML, CSS, Jinja2
# ============================================================

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# ── In-memory storage (list of task dictionaries) ──
# Each task = { 'id': int, 'title': str, 'done': bool }
tasks = []
next_id = 1  # Auto-incrementing ID for each task


# ── HOME PAGE — Show all tasks ──
@app.route("/")
def index():
    total = len(tasks)
    completed = sum(1 for t in tasks if t["done"])
    pending = total - completed
    return render_template("index.html", tasks=tasks, total=total,
                           completed=completed, pending=pending)


# ── ADD a new task ──
@app.route("/add", methods=["POST"])
def add():
    global next_id
    title = request.form.get("title", "").strip()

    # Validation: don't allow empty task
    if title:
        tasks.append({
            "id": next_id,
            "title": title,
            "done": False
        })
        next_id += 1

    return redirect(url_for("index"))


# ── MARK DONE / UNDO a task ──
@app.route("/toggle/<int:task_id>")
def toggle(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = not task["done"]  # Flip True <-> False
            break
    return redirect(url_for("index"))


# ── DELETE a task ──
@app.route("/delete/<int:task_id>")
def delete(task_id):
    global tasks
    tasks = [t for t in tasks if t["id"] != task_id]
    return redirect(url_for("index"))


# ── DELETE ALL completed tasks ──
@app.route("/clear-completed")
def clear_completed():
    global tasks
    tasks = [t for t in tasks if not t["done"]]
    return redirect(url_for("index"))


# ── Run the app ──
if __name__ == "__main__":
    app.run(debug=True)
