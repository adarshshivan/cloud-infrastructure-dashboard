# How to Run This Project

This guide explains how to run both the backend and frontend of the CloudOps Resource Dashboard.
Follow the steps in order for a smooth setup.

### 1. Clone the Repository
```bash
git clone https://github.com/adarshshivan/cloud-infrastruture-dashboard.git
cd cloudops-dashboard
```

### 2. Navigate to the Backend Folder
```bash
cd backend
```

### 3. Install Python Dependencies

The backend mainly uses:

- boto3 – AWS SDK
- json – to create JSON export
- python-dotenv (if you use environment variables)

Install requirements:
```bash
pip install -r requirements.txt
```

### 4. Configure AWS Credentials

1. Option A — Use AWS CLI (recommended earlier)
aws configure

2. Option B — Use .env file inside backend/

AWS_ACCESS_KEY_ID=your_key

AWS_SECRET_ACCESS_KEY=your_secret

AWS_DEFAULT_REGION=ap-south-1

### 5. Run the Backend Script

This script fetches your AWS data and exports it to:

`frontend/public/data/aws_resources.json`


Run:
```bash
python export_resources.py
```

After running successfully, you will see:

AWS Data Exported Successfully → /frontend/public/data/aws_resources.json

### 6. Start the Frontend
Navigate to frontend folder:
```bash
cd ../frontend
```

Install dependencies:
```bash
npm install
```

Run local development server:
```bash
npm run dev
```


The app will be available at:
```bash
http://localhost:3000
```

### 7. Deploy the Frontend to Vercel

Since your frontend is a static project:

vercel


Once deployed, Vercel will automatically serve:

`/public/data/aws_resources.json`

### 8. Updating Live Data

Whenever you want fresh AWS data:

```bash
cd backend
python export_resources.py
git add .
git commit -m "Updated AWS data"
git push
```


**Vercel automatically updates because it serves the JSON file from your repo.**

Cloud infrastructure Dashboard is now live:

**Backend:** Python-based AWS exporter

**Frontend:** Static HTML/CSS/JS deployed on Vercel

**Data Pipeline:** JSON file updated manually on each export

---
