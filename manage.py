# manage.py

from flask.cli import FlaskGroup
from jim import create_app, db
from jim.models import Log
import os, json

app = create_app()
cli = FlaskGroup(create_app=create_app)

#SEED DATA
seedData = [
 {
    "user_id": "U18V2LAAJ",
    "date": "8/9/2018"
  },
  {
    "user_id": "U18VAQPB9",
    "date": "8/14/2018"
  },
  {
    "user_id": "U1908M6PL",
    "date": "8/16/2018"
  },
  {
    "user_id": "U9APJ3XKN",
    "date": "8/21/2018"
  },
  {
    "user_id": "U9APJ3XKN",
    "date": "8/23/2018"
  },
  {
    "user_id": "U18VAQPB9",
    "date": "9/3/2018"
  },
  {
    "user_id": "U18V2LAAJ",
    "date": "9/5/2018"
  },
  {
    "user_id": "U1908M6PL",
    "date": "9/5/2018"
  },
  {
    "user_id": "U18VAQPB9",
    "date": "9/7/2018"
  },
  {

    "user_id": "U1908M6PL",
    "date": "9/7/2018"
  },
  {

    "user_id": "U18VAQPB9",
    "date": "9/21/2018"
  },
  {

    "user_id": "U18VAQPB9",
    "date": "9/24/2018"
  },
  {

    "user_id": "U1XRS5MCM",
    "date": "9/28/2018"
  },
  {

    "user_id": "U1XRS5MCM",
    "date": "10/3/2018"
  },
  {

    "user_id": "U9APJ3XKN",
    "date": "10/3/2018"
  },
  {

    "user_id": "U18VAQPB9",
    "date": "10/3/2018"
  },
  {

    "user_id": "U1908M6PL",
    "date": "10/5/2018"
  },
  {

    "user_id": "U9APJ3XKN",
    "date": "10/8/2018"
  },
  {

    "user_id": "U1XRS5MCM",
    "date": "10/8/2018"
  },
  {

    "user_id": "U9APJ3XKN",
    "date": "10/10/2018"
  },
  {

    "user_id": "U9APJ3XKN",
    "date": "10/12/2018"
  },
  {

    "user_id": "U9APJ3XKN",
    "date": "10/15/2018"
  },
  {

    "user_id": "U9APJ3XKN",
    "date": "10/19/2018"
  },
  {

    "user_id": "U9APJ3XKN",
    "date": "10/24/2018"
  },
  {

    "user_id": "U9APJ3XKN",
    "date": "10/26/2018"
  }
 ]
# run in shell as recreate-db
@cli.command()
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command()
def test():
    pass

@cli.command()
def seed_db():
    """Seeds the database"""
    for data in seedData:
        db.session.add(Log(user_id=data['user_id'], date=data['date']))
        db.session.commit()

@cli.command()
def cov():
    pass

if __name__ == "__main__":
    cli()