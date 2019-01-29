import subprocess
import os
import sys
import requests

# This script create tickets on GitHub. It's useful for Shipkit workshop:
# https://github.com/mstachniuk/shipkit-workshop

def createTicket(url, token, title, description):
    data = '''{ "title": "aa", "body": "bb" }'''.replace("aa", title).replace("bb", description)
    headers = {'Authorization': 'token ' + token}
    print 'POST ' + url
    response = requests.post(url, data=data, headers = headers)
    if response.status_code == 201:
        print "Created"
    else:
        print response
        print response.text

def createTickets(repo, token):
    begin = len("https://github.com/")
    ownerRepo = repo[begin:]
    print 'found ' + ownerRepo
    url = 'https://api.github.com/repos/' + ownerRepo + '/issues'
    createTicket(url, token, "Floating point support", "Please add a support for floating point opperations. \\nPlease add 'new feature' label to the PR for this issue. \\nThis feature should be implemented by repo owner.")
    createTicket(url, token, "Unit tests for MathUtils are missing", "Please add unit tests for MathUtils. \\nPlease add 'quality' label to the PR for this issue. \\nThis feature should be implemented by NOT a repo owner.")
    createTicket(url, token, "Readme file is missing", "Please add a Readme file with project description.")
    createTicket(url, token, "Javadoc for MathUtils class is missing", "Please add Javadoc for MathUtils class.")
    

if __name__ == "__main__":
    if 'GITHUB_WRITE_TOKEN' in os.environ:
        token = os.environ['GITHUB_WRITE_TOKEN']
    else:
        print "Please set GITHUB_WRITE_TOKEN env variable"
        sys.exit()
    
    with open('repos.txt') as f:
        repos = f.readlines()
        repos = [x.strip() for x in repos] 

        for repo in repos:
            print repo
            createTickets(repo, token)
            
            