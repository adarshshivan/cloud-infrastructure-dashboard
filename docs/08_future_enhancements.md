# Future Enhancements

The current version of the Cloud Infrastructure Dashboard displays EC2 and S3 information fetched through AWS CLI and exposed via a JSON file. While this works efficiently, several enhancements can make the dashboard more scalable, automated, secure, and visually powerful.

Below are the most impactful future improvements:

### 1. Automate JSON Generation (Cron Job / Lambda Execution)

Right now, the backend script (fetch_resources.py) must be executed manually.

**Enhancement:**

Automate the script using a cron job, Windows Task Scheduler, or an AWS Lambda function.

**Benefits:**

- JSON updates automatically every X minutes
- Always live data
- Zero manual work

### 2. Replace Local JSON With an API Endpoint

Currently, the frontend reads data from a static aws_resources.json.

**Enhancement:**

- Create a lightweight API using:
- AWS Lambda + API Gateway
- Flask FastAPI server
- Node.js serverless functions

**Benefits:**

- Real-time API calls
- Faster updates
- More scalable architecture

### 3. Add More AWS Services (Extend Dashboard Coverage)

**Currently tracking:**
- EC2
- S3

**Add next:**

- IAM Users & Roles
- VPC information
- Subnets & Gateways
- RDS Databases
- CloudWatch metrics
- Lambda functions
- DynamoDB

**Benefits:**

- More complete cloud observability
- Looks more impressive in portfolio

### 4. Add Graphs and Visualizations

Instead of plain text and tables, use charts.

**Enhancement:**

**Integrate:**

- Chart.js
- ApexCharts
- D3.js

**Show:**

- Cost trends
- Instance distribution
- Storage usage
- Service counts

**Benefits:**

- Makes dashboard EPIC
- Visual appeal increases drastically
- Much better for presentations/interviews

### 5. Full CI/CD Pipeline (GitHub → Vercel → Live Dashboard)

Currently data is being pushed manually.

**Enhancement:**

- Setup CI/CD:
- GitHub Actions
- Auto build + deploy on push

**Benefits:**

- Automatic builds
- Professional workflow
- Production-grade project

---