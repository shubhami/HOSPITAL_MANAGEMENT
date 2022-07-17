import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///patient_record.db")

#to load entire details table
df=pd.read_sql("details",engine)

print(df.head())
