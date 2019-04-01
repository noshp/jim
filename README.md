# Jim

Jim is a slackbot that responds when a user messages him to say that they have missed going to the gym.
It records the the day missed and adds $5 to the truancy pot.

## Development

This project is using the spanking python development workflow `pipenv`.
`pipenv` is here to combine the whole `requirements.txt`, `virtualenv` rituals we've been doing to
setup a python project.

[Install](https://pipenv.readthedocs.io/en/latest/) `pipenv` specific to your OS

### Install dependencies

`pipenv` automatically installs the packages defined in the `pipfile` and starts a virtualenv for you.
To install the dependecies just run:

```shell
pipenv install
```

To specify a certain version of `python` when using pipenv run:

```shell
pipenv install --python 3.7
```

Then to activate your `pipenv` just run:

```shell
pipenv shell
```

The following environment variables must be set for local testing
- `APP_ENV` - set to "DEV" on local machine

To spin up local Postgres, required for local testing, run project's docker script.

Install docker and docker-compose specific to your [OS](https://docs.docker.com/install/)
Then in the project root folder run:
```shell
# build and run the postgres container
docker-compose -f docker-compose.yml up -d --build

# to stop the container
docker-compose -f docker-compose.yml down
```

## Running

Once you have your pipenv shell, just export the flask app to your environment variable in the project's root folder:

*Shell*
```shell
export FLASK_APP=application.py
export FLASK_DEBUG=True

*Windows Powershell*
```shell
$env:APP_ENV="DEV"
$env:FLASK_APP=".\application.py"
$env:FLASK_DEBUG="True"
```
#run flask app
flask run

```

*Command Prompt*
```shell
SET FLASK_APP=application.py
SET FLASK_DEBUG=True

# First time running of the app 
flask db init
# migrate and upgrade your database
flask db migrate

flask db upgrade

#run flask app
flask run

```

## Slack App Use
Jim responds to the /jim command by sending a request to to http://noshp-jim.herokuapp.com/slack . The JSON payload of the request differs based on the text after the /jim command

User types `/jim stats`:
1. Jim runs `GROUP BY` query on Logs model
2. Jim responds with the number of records each user has in the Logs, and 200 code

User types `/jim 5$` 
1. Jim runs `INSERT` query into database with userid and timestamp
2. Jim returns angry message chastizing the user, and 200 code

User types `/jim` and something not above, and jim responds with 500
