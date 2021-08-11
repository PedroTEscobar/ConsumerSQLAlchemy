# Kafka Consumer inserting to PostgreSQL

## Table of contents
* [Install requirements](#install-requirements)
* [Adding tables](#adding-tables)
* [Run](#run)

## Install requirements

### Linux
```
cd ConsumerSQLAlchemy &&
python3.7 -m venv env &&
source env/bin/activate &&
python3.7 -m pip install -r requirements.txt
```

### Windows(cmd)
```
cd ConsumerSQLAlchemy &&
python -m venv env &&
.\env\Scripts\activate &&
python -m pip install -r requirements.txt
```

## Adding tables
> :warning: **Inside `Tables` can be only one table!**

For example we want to add new table 'Task004' which contains:
- id (Primary Key)
- date, 
- number of cars (Int)
- number of motorbikes (Int)
- direction (String)


Follow steps bellow:
1. Create the file such as `task004_table.py` inside `/Tables` folder.
2. Content of the file should look like below:
   ```
   from sqlalchemy import *
   from .utils import db


   class Task004(db.Base):
      __tablename__ = 'task004'
      id = Column(Integer, primary_key=True, autoincrement=True)
      date = Column(DateTime, nullable=False)
      number_of_cars = Column(Integer, nullable=False)
      number_of_motorbikes = Column(Integer, nullable=True)
      direction = Column(String, nullable=False)
   ```

Note:
   1. File name must end with `_table` e.g `foo_table.py`.
   2. Imports are necessary.
   3. Class name is identical with table name we want to add but in CamelCase.
   4. Inherit from MainClass to make sure your api endpoints are complete.
   5. Define `__tablename__` to set table name in postgres database.


More info : https://docs.sqlalchemy.org/en/14/orm/tutorial.html#declare-a-mapping

## Run
Parameters:

| Shortcut 	| Full           	| Default       	|
|----------	|----------------	|---------------	|
| b_ip     	| bootstrap_ip   	| localhost     	|
| b_p      	| bootstrap_port 	| 9092          	|
| t        	| topic          	| sql-insert    	|
| db_ip    	| database_ip    	| localhost     	|
| db_p     	| database_port  	| 5432          	|
| db       	| database_name  	| kafkaConsumer 	|
| user     	| username       	| postgres      	|
| pass     	| password       	|               	|
```
python run.py --topic sql-insert -db kafkaConsumer
```