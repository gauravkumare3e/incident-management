from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message   # <-- added this
from flask import render_template, request, redirect


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///incidents.db'
db = SQLAlchemy(app)

# Gmail config
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USERNAME='gauravk5732@gmail.com',
    MAIL_PASSWORD='tijk jxze hfxi fxar'
)
mail = Mail(app)

# DB model
class Incident(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(200))
    status = db.Column(db.String(20), default="Open")
    assignee = db.Column(db.String(50))

# Email helper
def send_email(subject, recipient, body):
    msg = Message(subject, recipients=[recipient], body=body, sender=app.config['MAIL_USERNAME'])
    mail.send(msg)
# UI Home Page
@app.route("/")
def home():
    incidents = Incident.query.all()
    return render_template("index.html", incidents=incidents)

# Handle form submission for new incident
@app.route("/create-ui", methods=["POST"])
def create_ui_incident():
    title = request.form["title"]
    description = request.form["description"]
    new_incident = Incident(title=title, description=description)
    db.session.add(new_incident)
    db.session.commit()
    
    # send email too
    send_email(
        "New Incident Created",
        app.config['MAIL_USERNAME'],
        f"Incident: {title}\nDescription: {description}"
    )
    
    return redirect("/")


# Create incident
@app.route("/incidents", methods=["POST"])
def create_incident():
    data = request.json
    incident = Incident(title=data["title"], description=data["description"])
    db.session.add(incident)
    db.session.commit()
    
    # Send email
    send_email("New Incident Created", "gauravk5732@gmail.com", f"Incident: {data['title']}\nDescription: {data['description']}")
    
    return jsonify({"message": "Incident created"})
# Assign incident from UI
@app.route("/assign/<int:id>", methods=["POST"])
def assign_incident(id):
    assignee = request.form["assignee"]
    incident = Incident.query.get_or_404(id)
    incident.assignee = assignee
    db.session.commit()
    
    # send email
    send_email(
        "Incident Assigned",
        app.config['MAIL_USERNAME'],
        f"Incident {id} assigned to {assignee}"
    )
    
    return redirect("/")

# Resolve incident from UI
@app.route("/resolve/<int:id>", methods=["POST"])
def resolve_incident(id):
    incident = Incident.query.get_or_404(id)
    incident.status = "resolved"
    db.session.commit()
    
    # send email
    send_email(
        "Incident Resolved",
        app.config['MAIL_USERNAME'],
        f"Incident {id} resolved ✅"
    )
    
    return redirect("/")


# Update incident
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
@app.route("/test-email", methods=["GET"])
def test_email_route():
    try:
        send_email(
            "IMS: Test Email",
            "gauravk5732@gmail.com",   # <-- replace with your Gmail
            "If you’re reading this, Gmail SMTP is working 🎉"
        )
        return {"message": "Test email sent. Check your inbox/spam."}
    except Exception as e:
        return {"error": str(e)}, 500

    
    # Send email
    send_email("Incident Updated", "gauravk5732@gmail.com", f"Incident {incident.id} updated.\nStatus: {incident.status}\nAssignee: {incident.assignee}")
    
    return jsonify({"message": "Incident updated"})
if __name__ == "__main__":
    app.run(debug=True)


