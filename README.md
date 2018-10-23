# Jim

Jim is a slackbot that responds when a user messages him to say that they have missed going to the gym.
It records the the day missed and adds $5 to the truancy pot.

## Development

This project is using new spanking new python development workflow `pipenv`.
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

## Running

Once you have your pipenv shell, just export the flask app to your environment variable in the project's root folder:

```shell
export FLASK_APP=application.py
export FLASK_DEBUG=True

#run flask app
flask run

```