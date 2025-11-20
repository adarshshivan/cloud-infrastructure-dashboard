# Project Overview — Cloud Infrastructure Dashboard

The **Cloud Infrastructure Dashboard** is a practical, DevOps project designed to simulate how cloud operations teams monitor AWS resources.  
Instead of relying on live backend APIs or complex cloud integrations, this project focuses on **extracting real AWS data manually**, converting it into a user-friendly format, and visualizing it through a polished frontend dashboard.

The main goal is to build a **static dashboard** that displays real AWS resource information, such as:

- EC2 Instances  
- S3 Buckets  

This dashboard:
- Uses real AWS CLI output  
- Stores the data in JSON format  
- Visualizes the data in the frontend  
- Requires **no live backend / no APIs**   

---

## What This Project Demonstrates

###  1. Cloud Knowledge  
Extracting AWS resource information via AWS CLI:
- Listing EC2 instances  
- Describing S3 buckets  
- Formatting JSON outputs  

###  2. Backend Processing  
Converting real AWS data into a clean, standardized JSON file for frontend consumption.

###  3. Frontend Visualization  
Creating a modern, responsive dashboard that:
- Loads JSON dynamically  
- Displays structured cloud data  

---

## Workflow

AWS Console / AWS CLI 

→ Extract Real Data 
→ Convert to JSON 
→ Use JSON in Frontend 
→ Visual Visualization


1. create AWS resources (EC2 + S3).  
2. Using AWS CLI, fetch their details.  
3. The data is saved locally as `real_dashboard_data.json`.  
4. The frontend reads this file and renders the dashboard.


---
