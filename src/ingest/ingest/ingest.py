import os
import pandas as pd
from database import Database


# Replace with download scripts
DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))))
train = pd.read_csv(os.path.join(DIR, 'data/raw/train.csv'))
test = pd.read_csv(os.path.join(DIR, 'data/raw/test.csv'))

# Save data to database
db = Database.from_defaults()
db.save(train, 'raw_train', 'dev')
db.save(test, 'raw_test', 'dev')