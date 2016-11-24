'''
Created on 15Nov.,2016

@author: kilta
'''
from datetime import datetime
import unittest

from Src.DbConnection import Models
from Src.DbConnection.Models import WateringLog


d = datetime.now()
temp =  WateringLog()

class Test(unittest.TestCase):
    
    def setUp(self):
        if not temp.table_exists():
            temp.create_table()
        #temp = WateringLog.create()

    def test_Query1(self):
        temp.logWateringInfo(d.date() , d.time(), 200)
        
    def test_Query2(self):
        test = temp.getSelectedDayWaterLogs('2016-11-23')
        waterVolume = 0;
        for val in test:
            waterVolume += val.volWater
        self.assertTrue(waterVolume == 400, 'Querys working')

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.QueryTest1']
    unittest.main()