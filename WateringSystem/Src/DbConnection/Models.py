'''
Created on 14Nov.,2016

@author: Peter
'''
#!/usr/bin/env python
# coding=utf-8
from peewee import *
from Src.Settings.Config import *

mysql_db = MySQLDatabase(databaseName,host=hostName,port=portNumber,user=userName, passwd=password)

class WateringLog(Model):
      # These are all the fields it has
    # match up CharField/IntegerField/etc with correct type
    dbn = CharField(primary_key=True) # primary key = unique id
    date = DateTimeField()
    time = TimeField()
    volWater = DoubleField()
    #grade_span_max = IntegerField()
    #total_students = IntegerField()
    
    class Meta:
        database = mysql_db
        db_table = 'WateringLog'

   