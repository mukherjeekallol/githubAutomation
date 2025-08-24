import os
import json
import requests

def create_audit_document(pr_data):
    audit_info = {
        "pull_request_id": pr_data['id'],
        "title": pr_data['title'],
        "created_by": pr_data['user']['login'],
        "created_at": pr_data['created_at'],
        "url": pr_data['html_url']
    }

    audit_file_path = os.path.join(os.getcwd(), 'audit', 'audit_document.json')
    
    with open(audit_file_path, 'w') as audit_file:
        json.dump(audit_info, audit_file, indent=4)
 
def main():
    # GitHub API token and repository details should be set as environment variables
    token = os.getenv('GITHUB_TOKEN')
    repo = os.getenv('GITHUB_REPOSITORY')
    pr_number = os.getenv('PR_NUMBER')

    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }

    print(f"Fetching pull request data...with credentials: token {token}, repo: {repo}, pr: {pr_number}")

    pr_url = f'https://api.github.com/repos/{repo}/pulls/{pr_number}'
    response = requests.get(pr_url, headers=headers)

    if response.status_code == 200:
        pr_data = response.json()
        create_audit_document(pr_data)
    else:
        print(f"Failed to retrieve pull request data: {response.status_code}")

if __name__ == "__main__":
    main()