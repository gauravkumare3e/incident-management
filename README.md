🛠️ Incident Management System

A web-based Incident Management System built with Flask, SQLite, and Bootstrap that allows teams to create, assign, and resolve incidents with real-time email notifications.

✅ Now includes User Authentication (Signup, Login, Logout) and a Single Dashboard Entry Point for a smooth experience.

✨ Features
🔑 Authentication System (Signup, Login, Logout)
🆕 Create Incidents with a title and description
👤 Assign Incidents to team members via the UI
✅ Mark Incidents as Resolved
📧 Email Notifications for creation, assignment, and resolution
💻 Responsive UI with Bootstrap 5
🗄️ SQLite Database for storing users and incidents
🐳 Docker Support for easy deployment

🚀 Getting Started

1️⃣ Clone Repository
git clone https://github.com/gauravkumare3e/incident-management.git
cd incident-management

2️⃣ Run Locally (Without Docker)
1.Create and activate virtual environment:
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate # Linux/Mac

2.Install dependencies:
pip install -r requirements.txt

3.Run Flask app:
flask run

4.Open in browser:
👉 http://127.0.0.1:5000

3️⃣ Run with Docker
1.Build image:
docker build -t incident-management .

2.Run container:
docker run -p 5000:5000 incident-management

3.Open in browser:
👉 http://127.0.0.1:5000

📝 Usage
1.Open app at: http://127.0.0.1:5000
If not logged in → redirected to Login/Signup Page
If logged in → redirected to Dashboard

2.Authentication
🔐 Signup with a new account
🔑 Login to access the system
🚪 Logout when done

3.Incidents
🆕 Create a new incident (Title + Description)
👤 Assign to a user
✅ Resolve when fixed
📧 Email notifications sent on every action

📂 Folder Structure
incident-management/
├── app.py             # Main Flask app
├── requirements.txt   # Python dependencies
├── Dockerfile         # Docker config
├── templates/         # HTML templates
│   ├── index.html     # Dashboard
│   ├── login.html     # Login page
│   └── signup.html    # Signup page
├── incidents.db       # SQLite database
├── .gitignore         # Ignore unnecessary files
└── venv/              # Virtual environment

⚠️ Notes

✉️ Email Setup: Add your Gmail & App Password in app.py:
app.config['MAIL_USERNAME'] = "your-email@gmail.com"
app.config['MAIL_PASSWORD'] = "your-app-password"

👉 For Gmail, use App Passwords
.
🗄️ Database: incidents.db is auto-created when the app runs.
🐳 Docker: Optional but recommended for consistent deployments.

🌐 Live Links
🚀 App Dashboard (local run) → http://127.0.0.1:5000
👉 http://127.0.0.1:5000
 will only work when your Flask app (or Docker container) is running, because that’s my local development server.
🔑 Single Entry Point → Redirects to Login/Signup if not logged in

👨‍💻 Author
Gaurav Kumar
🔗 GitHub

