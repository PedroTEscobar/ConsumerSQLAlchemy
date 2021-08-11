import os

sql_tables = []
dir_tables = os.path.dirname(__file__)
for file in os.listdir(dir_tables):
    sfile = str(file)
    if sfile.endswith('table.py'):
        sql_tables.append(sfile.split('.')[0])

__all__ = sql_tables

from . import *
