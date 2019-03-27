import subprocess
import os
import sys
import requests
from shutil import copyfile, rmtree

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
    url = 'https://api.github.com/repos/' + repo + '/issues'
    createTicket(url, token, "Add long point support", "Please add a support for long isTriangle.")
    createTicket(url, token, "Add float support", "Please add a support for float isTriangle.")
    createTicket(url, token, "Add BigInteger support", "Please add a support for BigInteger isTriangle.")
    createTicket(url, token, "Add BigDecimal point support", "Please add a support for BigDecimal isTriangle.")
    createTicket(url, token, "Unit tests for MathUtils are missing", "Please add unit tests for MathUtils.")
    createTicket(url, token, "Readme file is missing", "Please add a Readme file with project description.")
    createTicket(url, token, "Javadoc for MathUtils class is missing", "Please add Javadoc for MathUtils class.")
    
def cloneRepo(repo):
    os.chdir('/tmp')
    rmtree('/tmp/shipkit-w', ignore_errors=True)
    subprocess.check_output('git clone git@github.com:' + repo + '.git shipkit-w', shell=True)
    os.chdir('/tmp/shipkit-w')

def changeGitEmail():
    subprocess.check_output('git config user.email mstachniuk@gmail.com', shell=True)

def addLongSupport(repo, scriptDir):
    subprocess.check_output('git checkout -b long-support', shell=True)
    copyfile(scriptDir + '/MathUtils.java.v1', '/tmp/shipkit-w/src/main/java/com/example/shipkitworkshop/MathUtils.java')
    subprocess.check_output('git add -A', shell=True)
    subprocess.check_output('git commit -m "Add long support"', shell=True)
    subprocess.check_output('git push --set-upstream origin long-support', shell=True)

def addFloatSupport(repo, scriptDir):
    subprocess.check_output('git checkout -b float-support', shell=True)
    copyfile(scriptDir + '/MathUtils.java.v2', '/tmp/shipkit-w/src/main/java/com/example/shipkitworkshop/MathUtils.java')
    subprocess.check_output('git add -A', shell=True)
    subprocess.check_output('git commit -m "Add float support"', shell=True)
    subprocess.check_output('git push --set-upstream origin float-support', shell=True)

def addBigDecimalSupport(repo, scriptDir):
    subprocess.check_output('git checkout -b big-decimal-support', shell=True)
    copyfile(scriptDir + '/MathUtils.java.v3', '/tmp/shipkit-w/src/main/java/com/example/shipkitworkshop/MathUtils.java')
    subprocess.check_output('git add -A', shell=True)
    subprocess.check_output('git commit -m "Add BigDecimal support"', shell=True)
    subprocess.check_output('git push --set-upstream origin big-decimal-support', shell=True)

def addBigIntegerSupport(repo, scriptDir):
    subprocess.check_output('git checkout -b big-integer-support', shell=True)
    copyfile(scriptDir + '/MathUtils.java.v4', '/tmp/shipkit-w/src/main/java/com/example/shipkitworkshop/MathUtils.java')
    subprocess.check_output('git add -A', shell=True)
    subprocess.check_output('git commit -m "Add BigInteger support"', shell=True)
    subprocess.check_output('git push --set-upstream origin big-integer-support', shell=True)

def createThings(repo, token, scriptDir):
    createTickets(repo, token)
    cloneRepo(repo)
    changeGitEmail()
    addLongSupport(repo, scriptDir)
    addFloatSupport(repo, scriptDir)
    addBigDecimalSupport(repo, scriptDir)
    addBigIntegerSupport(repo, scriptDir)
    

if __name__ == "__main__":
    if 'GITHUB_WRITE_TOKEN' in os.environ:
        token = os.environ['GITHUB_WRITE_TOKEN']
    else:
        print "Please set GITHUB_WRITE_TOKEN env variable"
        sys.exit()

    scriptDir = os.getcwd()
    print 'script dir: ' + scriptDir

    with open('repos.txt') as f:
        repos = f.readlines()
        repos = [x.strip() for x in repos] 

        for repo in repos:
            print repo
            createThings(repo, token, scriptDir)
            
            