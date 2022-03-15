#Using SQLite3
import sqlite3
import json
import random
import datetime
from databaseCreate import c, conn
from classes import Cashbox
import itertools


#Program to update cashbox to database, returns cashbox ID
def UpdateCashbox(cashbox: Cashbox):
    date = datetime.datetime.now()
    dateStr = date.strftime("%y-%m-%d")
    randID = (random.randint(0,1000000000))
    c.execute('INSERT INTO cashbox(cashbox_ID, hundred_Value, fifty_Value, twenty_Value, ten_Value, five_Value, two_Value, one_Value, quarter_Value, dime_Value, nickel_Value, date) VALUES (?,?,?,?,?,?,?,?,?,?,?,?);',(randID,cashbox.hundred, cashbox.fifty,cashbox.twenty,cashbox.ten,cashbox.five,cashbox.two,cashbox.one,cashbox.quarter,cashbox.dime,cashbox.nickel,dateStr))
    conn.commit()
    # conn.close()
    return randID
#Program to update tips and deposit cashbox to database, returns tipbox Id and Deposit Id
def UpdateTipsDeposit(tipsCashboxId, depositCashboxId):
    randId1 = (random.randint(0,1000000000))
    randId2 = (random.randint(0,1000000000))
    c.execute('INSERT INTO tips(ID,cashbox_ID) VALUES (?,?)',(randId1,tipsCashboxId))
    c.execute('INSERT INTO deposits(ID,cashbox_ID) VALUES (?,?)',(randId2,depositCashboxId))
    conn.commit()
    # conn.close()
    return {randId1,randId2}
#Program to update the report to the database, returns report Id
def UpdateReport(netsales, expectedDeposit, tipAmount, quantityOrders, deposit, depositCashboxId, tipsCashboxId):
    randId = (random.randint(0,1000000000))
    c.execute('INSERT INTO report(ID, Netsales, Expected_Deposit, Tip_Amount, Quantity_Of_Orders, Deposit, Deposit_cashbox, tips_cashbox) VALUES (?,?,?,?,?,?,?,?)',(randId, netsales, expectedDeposit, tipAmount, quantityOrders, deposit, depositCashboxId, tipsCashboxId))
    conn.commit()
    # conn.close()
    return randId

def getAllCashboxes():
    
    db = conn.cursor()
    db.execute('Select * from cashbox')
    report_data = []
    desc = db.description
    for row in db:
        report = {"ID":row[0],"Netsales":row[1],"Expected_Deposit":row[1],"Tip_Amount":row[1],"Quantity_Of_Orders":row[1],"Deposit":row[1],"Deposit_cashbox":row[1],"tips_cashbox":row[1]}
        report_data.append(report)
    return report_data

