#  Tech Stack — Tools & Technologies Used

This project combines multiple technologies across **cloud**, **backend**, **frontend**, and **DevOps-style workflows**.  
Each component is intentionally chosen to keep the project simple, scalable, cost-efficient, and portfolio-friendly.

---

#  1. Cloud Technologies (AWS)

## **Amazon EC2**
Used for:
- Listing existing compute instances  
- Fetching metadata like IP, type, state  
- Understanding instance lifecycle  

## **Amazon S3**
Used for:
- Inspecting bucket names  
- Understanding region distribution  
- Simulating storage audit dashboards  

## **AWS IAM**
Used for:
- Creating a limited-access IAM user  
- Applying policies for EC2 and S3 read access  
- Configuring AWS credentials locally  

## **AWS CLI**
Used for:
- Fetching real AWS data in JSON format  
- Converting cloud metadata into dashboard-ready files  
- Verifying credentials and cloud access  
- Running all compute & storage queries  


---

#  2. Backend & Data Extraction

## **Python 3**
Used for:
- Processing AWS CLI output  
- Cleaning and formatting JSON  
- Preparing `real_dashboard_data.json`  

Although no backend server is deployed, Python plays a key role as a **local processing layer**.

## **JSON**
Used for:
- Storing cloud resource data  
- Feeding the dashboard  
- Decoupling data from UI  

---

#  3. Frontend Technologies

## **HTML5**
Used to structure the dashboard layout:
- Summary cards  
- Tables  
- Containers  
- UI sections  

## **CSS3**
Used to create a modern, visually appealing dashboard:
- Smooth gradients  
- Shadows & spacing  
- Responsive design  
- Card UI and layout grid  

## **JavaScript**
Used for:
- Fetching `real_dashboard_data.json`  
- Injecting values into DOM  
- Rendering dynamic sections  

No frameworks were used, keeping it lightweight and deployable on Vercel.

---

#  4. Deployment & Hosting

## **Vercel**
Used for:
- Hosting the dashboard frontend  
- Serving static assets (HTML/CSS/JS/JSON)  
- Providing fast CDN delivery  
- Offering a clean, shareable live demo link  

This avoids backend costs and keeps hosting simple.

## **Git & GitHub**
Used for:
- Version control  
- Clean repository structure  
- Documentation hosting  
- Source code transparency  

---
