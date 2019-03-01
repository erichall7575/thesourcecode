import requests,json
import os

reponame=input("Please Enter Your New Repo Name. Must be at least 5 characters long: ")
repodescription=input("Please Enter Your New Repo Description. Must be at least 5 characters long: ")

if len(reponame)>5 and len(repodescription)>5: 
    github_url = "https://api.github.com/user/repos"
    data = json.dumps({'name':reponame, 'description':repodescription})
    cred=[]
    with open('githubcredentials.txt','r') as myfile:
        for line in myfile: 
            cred.append(line.rstrip())

            
    r = requests.post(github_url, data, auth=(cred[0], cred[1]))

    print(r.json)
print("Invalid Repository Name or Description.")
