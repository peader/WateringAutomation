'''
Created on 15Nov.,2016

@author: kilta
'''
import unittest
from Src.DbConnection import Models
from Src.DbConnection.Models import WateringLog
from datetime import datetime

d = datetime.now()
temp =  WateringLog()

class Test(unittest.TestCase):
    
    def setUp(self):
        if not temp.table_exists():
            temp.create_table()
        #temp = WateringLog.create()

    def test_Query1(self):
        temp.logWateringInfo(d.date() , d.time(), 200)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.QueryTest1']
    unittest.main()