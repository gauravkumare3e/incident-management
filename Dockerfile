# -------------------------------
# Use a lightweight Python 3.9 image as the base
# It already has Python installed, slim version = smaller size
# -------------------------------
FROM python:3.9-slim

# -------------------------------
# Set the working directory inside the container
# All following commands will run in /app
# -------------------------------
WORKDIR /app

# -------------------------------
# Copy all files from your project folder into /app in the container
# -------------------------------
COPY . .

# -------------------------------
# Install all Python dependencies from requirements.txt
# --no-cache-dir keeps the image small by not storing temporary files
# -------------------------------
RUN pip install --no-cache-dir -r requirements.txt

# -------------------------------
# Tell Docker that this container uses port 5000
# -------------------------------
EXPOSE 5000

# -------------------------------
# Run the Flask app when the container starts
# CMD is the default command to execute
# -------------------------------
CMD ["python", "app.py"]

