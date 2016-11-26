'''
Created on 15Nov.,2016

@author: kilta
'''
from datetime import datetime
import unittest

from Src.DbConnection.Models import WateringLog, MoistureContentLog


d = datetime.now()
temp =  WateringLog()
temp2 = MoistureContentLog()

class DatabaseTesting(unittest.TestCase):
    
    def setUp(self):
        if not temp.table_exists():
            temp.create_table()
        if not temp2.table_exists():
            temp2.create_table()    

    #WaterinLog table class testing
    def test_WateringLogNewRow(self):
        temp.logWateringInfo(d.date() , d.time(), 200)
        pass
        
    def test_WateringLogQueryRow(self):
        test = temp.getSelectedDayWaterLogs('2016-11-23')
        waterVolume = 0;
        for val in test:
            waterVolume += val.volWater
        self.assertTrue(waterVolume == 400, 'Querys working')
        
    def test_WateringLogGetTodaysSum(self):
        test = temp.sumSelectedDayWaterVol('2016-11-23')
        self.assertTrue(test == 400, "test good")
    
    #MoistureContentLog table testing    
    def test_MoistureContentLogNewRow(self):
        temp2.logMoistureContentInfo(d.date() , d.time(), 50)
        pass
    
    def test_MoistureContentQueryRow(self):
        test = temp2.getLatestWaterContent()
        self.assertEqual(test.time.strftime("%H:%M:%S"), d.strftime("%H:%M:%S"), 'time equal')
        self.assertEqual(test.date.strftime("%d/%m/%y"), d.strftime("%d/%m/%y"), 'date equal')

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'DatabaseTesting.QueryTest1']
    unittest.main()