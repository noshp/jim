import json, os
from pprint import pprint
from jim import db
from jim.models import Log

class UploadSeedData:
    rootdir = os.path.dirname(os.path.abspath(__file__))
    datadir = rootdir + '/seed-data/'
    def __init__(self, filename):
        self.filename = filename
        self.datadir = UploadSeedData.datadir
        self.read_and_upload_json(self.datadir + self.filename)
        
    def read_and_upload_json(self, filename):
        Dictionary = {}

        with open(filename, encoding='utf-8') as data_file:
            data = json.loads(data_file.read())
        
        for i, entry in enumerate(data):
            Dictionary[i] = entry
            print(entry)
            data_to_insert = Log(user_id=entry['user_id'], date=entry['date'])
            
            try:
                db.session.add(data_to_insert)
                db.session.commit()
                db.session.close()
            except Exception as e:
                print(e)
                db.session.rollback()

def main():
    for filename in os.listdir(UploadSeedData.datadir):
        print("Working on " + filename)
        UploadSeedData(filename)

if __name__ == "__main__":
    main()