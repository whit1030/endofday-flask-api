#Using SQLite3
import sqlite3
import random
import datetime
from databaseCreate import c, conn
from classes import Cashbox


#Program to update cashbox to database, returns cashbox ID
def UpdateCashbox(cashbox: Cashbox):
    date = datetime.datetime.now()
    dateStr = date.strftime("%y-%m-%d")
    randID = (random.randint(0,1000000000))
    c.execute('INSERT INTO cashbox(cashbox_ID, hundred_Value, fifty_Value, twenty_Value, ten_Value, five_Value, two_Value, one_Value, quarter_Value, dime_Value, nickel_Value, date) VALUES (?,?,?,?,?,?,?,?,?,?,?,?);',(randID,cashbox.hundred, cashbox.fifty,cashbox.twenty,cashbox.ten,cashbox.five,cashbox.two,cashbox.one,cashbox.quarter,cashbox.dime,cashbox.nickel,dateStr))
    conn.commit()
    conn.close()
    return randID