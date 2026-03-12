Steps to operate the git 
1.install git from web browser
2.Open command prompt 
    1) git --version
    2) git config --global user.name "User Name"
    3) git config --global user.email "Email"
    4) git clone copied link of repo paste here
    5) cd repo_name
    6) cd project_folder_name
    7)code . (To open code in VS code)
3. In Opened Vs code project >> Open New Terminal
    Type:
    git status
        Check what changed.
        "On branch main
        Your branch is up to date with 'origin/main'"
        [If it is like this then everything is connected to github]

4. git pull 
        Get the latest updates from GitHub.
5. git add .
        Git collects all changed files in your project.
6. git commit -m "message"
        Save a version of your changes locally.
7. git push
        Upload changes to GitHub.
8. before leaving lab:
        git credential-manager reject https://github.com
