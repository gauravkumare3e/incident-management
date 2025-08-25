# 🛠️ Incident Management System

A **web-based Incident Management System** built using **Flask**, **SQLite**, and **Bootstrap**.  

It allows users to **create, assign, and resolve incidents** and sends **email notifications** for all actions.

---

## ✨ Features

- 🆕 Create incidents with a title and description  
- 👤 Assign incidents to team members via the UI  
- ✅ Mark incidents as resolved  
- 📧 Email notifications for creation, assignment, and resolution  
- 💻 Responsive UI using Bootstrap  
- 🗄️ SQLite database to store incidents  
- 🐳 Docker support for easy deployment  

---

## 🚀 Run Locally (Without Docker)

1. **Activate virtual environment**  
   ```bash
   venv\Scripts\activate
2.Install dependencies
pip install -r requirements.txt

3.Run the Flask app
flask run
or
python app.py

4.Open in browser
http://127.0.0.1:5000

🐳 Run Using Docker
1.Build Docker image
docker build -t incident-management .

2.Run container
docker run -p 5000:5000 incident-management

3.Open in browser
http://127.0.0.1:5000

📝 Usage
1.Fill the form to create a new incident

2.View all incidents in the table

3.Assign an incident by typing a name and clicking Assign

4.Resolve an incident by clicking Resolve

5.Check your email for notifications

📂 Folder Structure

incident-management/
├─ app.py             # Main Flask app
├─ requirements.txt   # Python dependencies
├─ Dockerfile         # Docker configuration
├─ templates/
│  └─ index.html      # UI template
├─ .gitignore         # Git ignore file
├─ incidents.db       # SQLite database
└─ venv/              # Virtual environment

⚠️ Notes
✉️ Email Setup: Add valid SMTP credentials in app.py. For Gmail, use an App Password.

🗄️ Database: incidents.db is created automatically when you run the app.

🐳 Docker: Optional. The app runs fine without Docker, but Docker helps with portability.



