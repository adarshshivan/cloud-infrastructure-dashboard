# Challenges Faced & How i Solved Them

Throughout the development of the Cloud Infrastructure Dashboard, several real-world challenges appeared — both technical and architectural.
Each challenge helped me to improve understanding of cloud workflows, frontend-backend integration, and deployment behavior.

Below are the challenges and the clear solutions that was implemented:

### 1. Challenge: Fetching AWS Data Without Using Environment Variables

**Problem:**
AWS datasets are normally fetched using:

- environment variables
- IAM roles
- SDK-based authentication (like boto3)

**Solution:**

- Used AWS CLI with manually configured access keys
- Wrote a Python script that runs CLI commands
- Parsed the raw output into structured JSON

**Result:**

Eliminated the need for a backend server and learned how raw AWS data actually looks.

---
### 2. Challenge: Converting AWS CLI Output Into Clean JSON

**Problem:**
AWS CLI output is:

- verbose
- nested
- inconsistent across services

Parsing it into UI-friendly JSON was required.

**Solution:**

- Wrote a Python script that extracts only needed fields
- Formatted a new JSON file containing clean, minimal data
- Ensured correct mapping to frontend keys

**Result:**

The frontend received a simple, predictable JSON file every time.

---

### 3. Challenge: Linking Backend JSON to a Static Frontend
**Problem:**
The project has no API server, so there is no active backend to fetch from.
Static sites cannot use dynamic server code.

**Solution:**

- Stored the JSON file inside /frontend/data/aws_resources.json
- Used JavaScript fetch() to load it locally
- Mapped JSON → DOM update

**Result:**

Frontend remained fully static, still displaying dynamic AWS data.

---

### 4. Challenge: Vercel Deployment Didn’t Load JSON File
**Problem:**
Vercel blocks JSON loading if:

- the file path is incorrect
- file is not inside the public root

**Solution:**

- Moved the JSON file inside the correct relative path
- Ensured fetch path matches deployment structure
- Re-deployed using Git push

**Result:**

The dashboard loaded data perfectly on Vercel.

---

### 5. Challenge: Keeping Data Updated Without a Backend Server
**Problem:**
i needed updated AWS data, but didn’t have:

- a backend service
- database
- cron system

**Solution:**

- Manually run the Python fetch script
- Auto-generate the new JSON
- Commit & push → Vercel rebuilds automatically

**Result:**

A simple but effective update pipeline without maintaining any server.

---

**Every challenge improved the clarity of the architecture and helped me build a clean, understandable, real-world cloud dashboard.**

---