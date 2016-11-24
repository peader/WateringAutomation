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
    #dbn = CharField(primary_key=True) # primary key = unique id
    date = DateField()
    time = TimeField()
    volWater = DoubleField()
    #grade_span_max = IntegerField()
    #total_students = IntegerField()
    
    class Meta:
        database = mysql_db
        db_table = 'WateringLog'
        
    def logWateringInfo(self, todaysDate, currentTime, waterVolume):
        try:
            with mysql_db.transaction():
                 WateringLog.create(date=todaysDate, time=currentTime, volWater=waterVolume)
            print('watering information successfully saved to database')
        except IntegrityError:
            print('failed to save watering information to database')
            
    def getSelectedDayWaterLogs(self, SelectedDate):
        return WateringLog.select().where(WateringLog.date==SelectedDate)
        
        
class MoistureContentLog(Model):
      # These are all the fields it has
    # match up CharField/IntegerField/etc with correct type
    dbn = CharField(primary_key=True) # primary key = unique id
    date = DateField()
    time = TimeField()
    moistureContent = DoubleField()
    #grade_span_max = IntegerField()
    #total_students = IntegerField()
    
    class Meta:
        database = mysql_db
        db_table = 'MoistureContentLog'


   