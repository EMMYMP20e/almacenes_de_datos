
# Méndez Pérez Emmanuel
# I5906 D07
# ETL

import petl as etl
from petl import select
table = (etl
         .fromcsv('MOCK_DATA.csv')
         .convert('first_name', 'upper')
         .convert('last_name', 'upper')
         .convert('email', 'upper')
         .convert('gender', 'upper')
         .convert('money', 'upper')
         )
table = select(table, lambda clean: clean['first_name'] != '')
table = select(table, lambda clean: clean['last_name'] != '')
table = select(table, lambda clean: clean['email'] != '')
table = select(table, lambda clean: clean['gender'] != '')
table = select(table, lambda clean: clean['money'] != '')
print(table)
etl.tocsv(table, 'new.csv')
