fetch("data/real_dashboard_data.json")
  .then(res => res.json())
  .then(data => {
    document.getElementById("content").innerHTML = `
      <h2>EC2 Instances: ${data.ec2.length}</h2>
      <ul>
        ${data.ec2.map(i => `
          <li>ID: ${i.InstanceId} | Type: ${i.InstanceType} | State: ${i.State} | IP: ${i.PublicIP}</li>
        `).join('')}
      </ul>

      <h2>S3 Buckets: ${data.s3.length}</h2>
      <ul>
        ${data.s3.map(b => `
          <li>Name: ${b.BucketName} | Region: ${b.Region}</li>
        `).join('')}
      </ul>
    `;
  })
  .catch(err => console.error("Error loading data:", err));
