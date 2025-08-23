\# 🛠️ Incident Management System



A simple \*\*web-based Incident Management System\*\* built with \*\*Flask\*\*, \*\*SQLite\*\*, and \*\*Bootstrap\*\*.  

It allows users to \*\*create, assign, and resolve incidents\*\* and sends \*\*email notifications\*\* for all actions.



---



\## ✨ Features



\- 🆕 Create new incidents with a title and description  

\- 👤 Assign incidents to team members via the UI  

\- ✅ Mark incidents as resolved  

\- 📧 Email notifications for creation, assignment, and resolution  

\- 💻 Simple and responsive UI using Bootstrap  

\- 🗄️ SQLite database for storing incidents  



---



\## 🚀 How to Run Locally

1\. \*\*Activate the virtual environment\*\*

```bash

venv\\Scripts\\activate



2.Install dependencies



pip install -r requirements.txt



3.Run the Flask app



flask run



or



python app.py



4.Open the app in your browser



http://127.0.0.1:5000



📝 Usage



1.Fill the form to create a new incident.



2.Use the table to view all incidents.



3.Assign an incident by typing a name and clicking Assign.



4.Resolve an incident by clicking Resolve.



5.Check your email for notifications of all actions.



📂 Folder Structure

incident-management/

├─ app.py             # Main Flask app

├─ requirements.txt   # Python dependencies

├─ templates/

│  └─ index.html      # UI template

├─ .gitignore         # Git ignore file

├─ incidents.db       # SQLite database

└─ venv/              # Virtual environment



⚠️ Notes



1.Email Setup: Use valid SMTP credentials in app.py. For Gmail, you may need an App Password.



2.Database: SQLite file (incidents.db) is created automatically.



3.Docker: Optional. You can run the app locally without Docker



