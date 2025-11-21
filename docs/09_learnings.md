# Learnings

Building the Cloud Infrastructure Dashboard from scratch provided multiple real-world learnings that are directly applicable to cloud engineering, DevOps workflows, frontend development, and backend automation.
This project intentionally used a hands-on, manual, AWS-CLI-driven approach — and this created practical learning experiences.

###  1. Understanding AWS Infrastructure at a Resource Level

By manually fetching EC2 and S3 resource details:

- How AWS CLI works
- How AWS resources are structured
- Regions, instances, buckets, permissions
- The difference between infrastructure view vs dashboard-level view

### 2. Working With AWS CLI Instead of Fully Automated Tools

Instead of Terraform/IaC, i used CLI + Python scripting.

- Running AWS commands
- Parsing CLI outputs
- Authenticating using access keys
- Understanding real AWS workflows

### 3. Converting Raw AWS Output Into Structured JSON

The backend script (fetch_resources.py) was a practical exercise in:

- Extracting fields
- Cleaning AWS CLI output
- Structuring JSON
- Storing results reliably

### 4. Linking Backend Output With Frontend UI

Instead of a database or API, i used a static JSON file.

- data flows from backend → JSON → frontend
- Fetching local JSON in JavaScript
- Updating DOM based on JSON
- Maintaining folder-level consistency

### 5. Deploying a Zero-Backend Frontend to Vercel

By deploying static files to Vercel:

- How static hosting works
- How Vercel builds, optimizes and serves assets
- Repo connection → auto deploy
- Updating live dashboard via new JSON

### 6. Understanding Cloud Architecture Design Choices

This project taught how real dashboards are built:

- How a pull-based data pipeline works
- When to use static vs dynamic frontend
- Why JSON-based dashboards are simple but effective
- Differences between multiple architectural approaches

### 7. Using GitHub for Version Control and Repo Structuring

I worked with:

- Git commits
- Branch updates
- Organized repository layout
- Separation of backend/frontend/images/docs

### 8. Debugging & Problem Solving

**During the build, i faced issues like:**

- JSON path errors
- CLI output mismatches
- Vercel path rewriting
- Image not loading in markdown
- Folder structure fixes

solving these above issues i learned:

- Systematic debugging
- Breaking down errors
- Cross-checking relative paths
- Making documentation preview work

---