import json, subprocess, sys, urllib.request

# Get token from config
with open('/root/.hermes/config.yaml') as f:
    for line in f:
        if 'Authorization' in line and 'Bearer' in line:
            token = line.split('Bearer ')[1].strip()
            break
    else:
        print("ERROR: token not found")
        sys.exit(1)

# Trigger deployment via Vercel API
import urllib.request

data = json.dumps({
    "name": "personal-projects",
    "project": "prj_4lUEq6sB1mN7vj4f6QsOw2jgVmVa",
    "gitSource": {
        "type": "github",
        "repoId": 1250676750,
        "ref": "main"
    }
}).encode()

req = urllib.request.Request(
    "https://api.vercel.com/v13/deployments",
    data=data,
    headers={
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
)

try:
    resp = urllib.request.urlopen(req)
    body = json.loads(resp.read())
    print(f"Deployment ID: {body.get('id', 'N/A')}")
    print(f"State: {body.get('readyState', 'N/A')}")
    print(f"URL: {body.get('url', 'N/A')}")
    print(f"Full response: {json.dumps(body, indent=2)[:800]}")
except urllib.error.HTTPError as e:
    print(f"HTTP {e.code}: {e.read().decode()[:500]}")