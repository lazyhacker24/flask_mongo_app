# flask_mongo_app

# Flask + MongoDB Atlas App

This project demonstrates a simple Flask web application that:
- Returns JSON data from a backend file via an API route (`/api`)
- Submits form data to MongoDB Atlas using a frontend form (`/submit`)
- Redirects to a success page (`/success`) after successful data insertion
- Displays errors on the same page if submission fails

---

## 📁 Project Structure

flask_mongo_app/
│
├── app.py
├── data.json
├── requirements.txt
└── templates/
├── form.html
└── success.html


---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/lazyhacker24/flask_mongo_app.git
cd flask_mongo_app


2️⃣ Create Virtual Environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Configure MongoDB Atlas

Go to MongoDB Atlas
Create a cluster and a database (e.g., flaskdb)
Create a collection (e.g., users)
Get your connection string and replace it in app.py:
MONGO_URI = "your_mongodb_atlas_connection_string"

▶️ Run the Application
python app.py

Then open your browser and visit:
Form page → http://127.0.0.1:5000/submit
API endpoint → http://127.0.0.1:5000/api


📦 API Route
GET /api
Returns JSON data from the data.json file.

Example Response:

[
  {"id": 1, "name": "Alice", "age": 25},
  {"id": 2, "name": "Bob", "age": 30}
]

🖊️ Form Submission Flow

User visits /submit
Enters name and age
Data is inserted into MongoDB Atlas
Redirects to /success page on success
Displays error on same page if insertion fails

✅ Success Page

Displays:      Data submitted successfully!


📸 Screenshots:-
Check Screenshot Names Folder


/submit form page
/success confirmation page
/api output in browser
MongoDB Atlas data view


🧠 Technologies Used

Flask (Python web framework)
MongoDB Atlas (cloud database)
HTML (for frontend templates)
PyMongo (MongoDB driver)

🧰 Requirements
Flask
pymongo

📚 Author
Pardeep Kumar
