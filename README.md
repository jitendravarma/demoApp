# demoApp
This is a demo application to show file upload via json and display.

# Installation

1. Git clone this repo
1. You might need to install nodejs
    1. sudo apt-get install nodejs
1. Install all the requirements in the virtualenv of your choice
    1. pip install -r requirements.txt
1. Install node modules and build files, from base dir of the repo.
    1. cd frontend
    1. npm install
    1. npm build
1. You might need to install [postgres](https://www.enterprisedb.com/postgres-tutorials/how-install-postgres-ubuntu) as well
1. Edit local.py as per your postgres database, port no and database name
1. Create migration directory in core app at the base directory
    1. cd core
    2. mkdir migrations
    3. cd migrations
    4. touch __init.py__
1. Migrate the app
    1. ./manage.py makemigrations
    1.  ./ manage.py migrate

For production setup, you might need to add the server's ip address in ALLOWED_HOSTS in settings/base.py

Also, you might need to change the BASE_URL in frontend/src/utils/constants.js (Currently points to 127.0.0.1:8000).

You will also need to update base.py to set email credentials for sending mails. Set smtp ports, from email and password in base.py

Running the test cases, cd tests/pytest. This is a simple login test to check login, edit this file as per your user name
```sh
    pytest
```

After setting up all the dependencies, you can start the server
```sh
./manage.py runserver 0.0.0.0:8000
```
And visit http://0.0.0.0:8000

# Issues
If your build for npm fails, then please delete the node_modules folder and do `npm install`

