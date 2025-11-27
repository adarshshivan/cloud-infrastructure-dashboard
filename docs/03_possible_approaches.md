# Project Approaches — What Options Exist & Why i Chose This One

When building a cloud infrastructure dashboard, there are multiple ways to architect the system.  
Different companies use different approaches depending on:

- Complexity  
- Budget  
- Real-time needs  
- Security requirements  
- Hosting choices  

Below are the **most common industry approaches**:

---

#  1. Fully Dynamic API-Based Approach (Most Common in Industry)

In this approach:

- The backend periodically calls AWS SDK (`boto3`)
- It fetches EC2, S3, IAM info dynamically
- It exposes REST endpoints:  
  `/api/ec2`, `/api/s3`, etc.
- The frontend fetches data from these APIs in real-time
- The dashboard automatically updates

###  Pros  
- Real-time data  
- Most realistic enterprise model  
- True DevOps monitoring workflow  

###  Cons  
- Requires EC2/Lambda hosting (not free on Vercel)  
- Requires backend maintenance  
- Not suitable for free-tier

---

#  2. Serverless Real-Time Dashboard (Modern Cloud-Native Approach)

In this approach:

- Scheduled Lambda every X minutes  
- Lambda → AWS SDK → DynamoDB  
- API Gateway → Frontend  
- Frontend calls live APIs  
- Deployed entirely serverless

###  Pros  
- Scalable  
- Zero maintenance  
- Pure cloud-native  

###  Cons  
- Complex  
- Cannot be shown live on Vercel without paid plans  
- Requires many AWS services (Lambda, API Gateway, DynamoDB)  

---


#  3. Snapshot-Based Static Dashboard (My Approach)

**This is the approach which i used**:

In this approach:

- I used AWS CLI to fetch real data  
- Convert the real AWS output into `real_dashboard_data.json`  
- Place this JSON inside the frontend repo  
- Frontend loads the JSON using JavaScript  
- Dashboard displays *real* AWS data but in a static, stable format  
- No backend/API required  
- Deploy frontend on Vercel easily

###  Why  
- Zero cost  
- Easy Vercel deployment  
- Real AWS data  
- Beginner-friendly  
- No backend hosting required  
- Gives full cloud experience without complexity  
