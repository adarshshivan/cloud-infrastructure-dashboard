fetch("data/mock_data.json")
  .then(res => res.json())
  .then(data => {
    document.getElementById("content").innerHTML = `
      <h2>EC2 Instances: ${data.EC2_Instances.length}</h2>
      <h2>S3 Buckets: ${data.S3_Buckets.length}</h2>
    `;
  });
