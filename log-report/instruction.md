Read the Apache access log located at /app/access.log.

Generate a JSON report and save it to:

/app/report.json

Success criteria:

1. Read every request from the access log.
2. Calculate the total number of requests.
3. Calculate the number of unique client IP addresses.
4. Determine the most frequently requested path.
5. Write a JSON object to /app/report.json with exactly these keys:

- total_requests
- unique_ips
- top_path

The output must be valid JSON.