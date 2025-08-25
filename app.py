from flask import Flask, request, jsonify, render_template, redirect, session, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
import sqlite3
import os

app = Flask(__name__)

# 🔑 Secret key (sessions)
app.secret_key = os.environ.get("SECRET_KEY", "secretkey123")

# 📂 Database setup (SQLite local file)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///incidents.db'
db = SQLAlchemy(app)

# 📧 Gmail SMTP config (from environment variables)
app.config.update(
    MAIL_SERVER=os.environ.get("MAIL_SERVER", "smtp.gmail.com"),
    MAIL_PORT=int(os.environ.get("MAIL_PORT", 587)),
    MAIL_USE_TLS=os.environ.get("MAIL_USE_TLS", "True") == "True",
    MAIL_USERNAME=os.environ.get("MAIL_USERNAME"),
    MAIL_PASSWORD=os.environ.get("MAIL_PASSWORD")
)
mail = Mail(app)


# 🗄️ Incident DB Model
class Incident(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(200))
    status = db.Column(db.String(20), default="Open")
    assignee = db.Column(db.String(50))


# 📧 Email helper
def send_email(subject, recipient, body):
    if app.config["MAIL_USERNAME"]:  # only send if email configured
        msg = Message(subject, recipients=[recipient], body=body, sender=app.config['MAIL_USERNAME'])
        mail.send(msg)


# ✅ Authentication Routes

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("incidents.db")
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
        cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        existing_user = cursor.fetchone()

        if existing_user:
            conn.close()
            return "❌ Username already exists!"

        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()
        return redirect("/login")

    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("incidents.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            session["username"] = username
            return redirect(url_for("home"))
        else:
            return "❌ Invalid username or password!"

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect("/login")


# ✅ Incident Routes
@app.route("/")
def home():
    if "username" in session:
        incidents = Incident.query.all()
        return render_template("index.html", incidents=incidents)
    else:
        return redirect(url_for("login"))


@app.route("/create-ui", methods=["POST"])
def create_ui_incident():
    title = request.form["title"]
    description = request.form["description"]
    new_incident = Incident(title=title, description=description)
    db.session.add(new_incident)
    db.session.commit()

    send_email(
        "New Incident Created",
        app.config['MAIL_USERNAME'],
        f"Incident: {title}\nDescription: {description}"
    )
    return redirect("/")


@app.route("/incidents", methods=["POST"])
def create_incident():
    data = request.json
    incident = Incident(title=data["title"], description=data["description"])
    db.session.add(incident)
    db.session.commit()

    send_email(
        "New Incident Created",
        app.config['MAIL_USERNAME'],
        f"Incident: {data['title']}\nDescription: {data['description']}"
    )
    return jsonify({"message": "Incident created"})


@app.route("/assign/<int:id>", methods=["POST"])
def assign_incident(id):
    assignee = request.form["assignee"]
    incident = Incident.query.get_or_404(id)
    incident.assignee = assignee
    db.session.commit()

    send_email(
        "Incident Assigned",
        app.config['MAIL_USERNAME'],
        f"Incident {id} assigned to {assignee}"
    )
    return redirect("/")


@app.route("/resolve/<int:id>", methods=["POST"])
def resolve_incident(id):
    incident = Incident.query.get_or_404(id)
    incident.status = "resolved"
    db.session.commit()

    send_email(
        "Incident Resolved",
        app.config['MAIL_USERNAME'],
        f"Incident {id} resolved ✅"
    )
    return redirect("/")


@app.route("/incidents/<int:id>", methods=["PUT"])
def update_incident(id):
    data = request.json
    incident = Incident.query.get(id)
    if not incident:
        return jsonify({"error": "Incident not found"}), 404

    if "status" in data:
        incident.status = data["status"]
    if "assignee" in data:
        incident.assignee = data["assignee"]

    db.session.commit()
    send_email(
        "Incident Updated",
        app.config['MAIL_USERNAME'],
        f"Incident {incident.id} updated.\nStatus: {incident.status}\nAssignee: {incident.assignee}"
    )
    return jsonify({"message": "Incident updated"})


@app.route("/test-email", methods=["GET"])
def test_email_route():
    try:
        send_email(
            "IMS: Test Email",
            app.config['MAIL_USERNAME'],
            "If you’re reading this, Gmail SMTP is working 🎉"
        )
        return {"message": "Test email sent. Check your inbox/spam."}
    except Exception as e:
        return {"error": str(e)}, 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)


