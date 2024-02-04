import json
import requests

# GitHub API endpoint
url = 'https://api.github.com/repos/rails/rails/issues'

# Parameters to fetch 500 most recent issues
params = {'per_page': 100, 'page': 1}
issues = []

# Fetching issues
for _ in range(5):
    response = requests.get(url, params=params)
    issues += response.json()
    if 'next' in response.links.keys():
        url = response.links['next']['url']
    else:
        break

# Specify the file name to store the issues
file_name = 'github_issues.json'

# Write the issues to the JSON file
with open(file_name, 'w') as file:
    json.dump(issues, file, indent=4)

print(f"Issues have been written to {file_name}")