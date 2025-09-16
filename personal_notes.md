“What this does exactly: TBD.”	
`Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

Initialize virtual environment 
`.venv/Scripts/Activate.ps1`

### used git commands 

Copy files from another repository to my working directory
`git clone url`

Add files to index, for now I am using only `*` to add **everything**
`git add * // to add everything`

Commit files = Record changes to the repository (local)
`git commit -m "Description message"`

Updating the remote repository

`git push origin master`

### Docker 

build docker image
`docker build .`
