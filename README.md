# 🛠️ Incident Management System

A **web-based Incident Management System** built with **Flask**, **SQLite**, and **Bootstrap**.  

It allows users to **create, assign, and resolve incidents**, and sends **email notifications** for all actions.

## ✨ Features

- 🆕 Create incidents with a title and description  
- 👤 Assign incidents to team members via the UI  
- ✅ Mark incidents as resolved  
- 📧 Email notifications for creation, assignment, and resolution  
- 💻 Responsive UI using Bootstrap  
- 🗄️ SQLite database for storing incidents  
- 🐳 Docker support for easy deployment  
- 🔐 User authentication: Signup, Login, Logout  

---

## 🌐 Live Demo

Access the live app (hosted on Render):  

[**Incident Management Live App**](https://incident-management-yse8.onrender.com)  

> 🔑 Use the Signup/Login links on the homepage to start using the app.
---
## 🚀 Run Locally (Without Docker)

1. **Activate virtual environment**  
venv\Scripts\activate

2.Install dependencies
pip install -r requirements.txt

3.Set environment variables (for email and secret key)

set SECRET_KEY=secretkey123

set MAIL_SERVER=smtp.gmail.com

set MAIL_PORT=587

set MAIL_USE_TLS=True

set MAIL_USERNAME=your-email@gmail.com

set MAIL_PASSWORD=your-app-password

4.Run the Flask app

flask run
or
python app.py

5.Open in browser
http://127.0.0.1:5000

⚠️ Note: The local link only works while the app is running.

🐳 Run Using Docker

1.Build Docker image
docker build -t incident-management .

2.Run container
docker run -p 5000:5000 incident-management

3.Open in browser
http://127.0.0.1:5000

📝 Usage

1.Signup or login to access the app.
2.Fill the form to create a new incident.
3.View all incidents in the table.
4.Assign an incident by typing a name and clicking Assign.
5.Resolve an incident by clicking Resolve.
6.Check your email for notifications of all actions.

📂 Folder Structure

incident-management/
├─ app.py             # Main Flask app
├─ requirements.txt   # Python dependencies
├─ Dockerfile         # Docker configuration
├─ templates/
│  ├─ index.html      # Home page UI
│  ├─ login.html      # Login page
│  └─ signup.html     # Signup page
├─ .gitignore         # Git ignore file
├─ incidents.db       # SQLite database
└─ venv/              # Virtual environment

⚠️ Notes
✉️ Email Setup: Add valid SMTP credentials in environment variables (MAIL_USERNAME and MAIL_PASSWORD). For Gmail, use an App Password.
🗄️ Database: SQLite file (incidents.db) is created automatically.
🐳 Docker: Optional. App works locally without Docker, but Docker makes it portable.
🔑 Authentication: Signup, Login, Logout implemented. Homepage redirects to login if user not logged in.

👨‍💻 Author
Gaurav Kumar
🔗 GitHub

