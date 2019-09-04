# manage.py

from flask.cli import FlaskGroup
from jim import create_app, db
from jim.models import Log
import os, json
from jim.utils import UploadSeedData

app = create_app()
cli = FlaskGroup(create_app=create_app)

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
    """Seeds the database
    """
    seedDataUploader = UploadSeedData.UploadSeedData('seed_data.json')

@cli.command()
def cov():
    pass

if __name__ == "__main__":
    cli()