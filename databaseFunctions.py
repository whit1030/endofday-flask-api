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

def updateWastesheet(AppleCranberryMuffin,TripleBerryMuffin,RaspberryScone,Croissant,HamCroissant,QuinoaLoaf,CherryLemonLoaf,GingerCookie,ChocolateChipCookie,GranolaCookie,CocoaChiaBites,PeanutButterBites,OvernightOats,EggCheeseWrap,EggBanconWrap,EggSausageWrap,ChickpeaWrap,BeanBurrito,CoconutWrap,VeggieWrap):
    randId = (random.randint(0,1000000000))
    c.execute('INSERT INTO wastesheet(ID,AppleCranberryMuffin,TripleBerryMuffin,RaspberryScone,Croissant,HamCroissant,QuinoaLoaf,CherryLemonLoaf,GingerCookie,ChocolateChipCookie,GranolaCookie,CocoaChiaBites,PeanutButterBites,OvernightOats,EggCheeseWrap,EggBanconWrap,EggSausageWrap,ChickpeaWrap,BeanBurrito,CoconutWrap,VeggieWrap)',(randId,AppleCranberryMuffin,TripleBerryMuffin,RaspberryScone,Croissant,HamCroissant,QuinoaLoaf,CherryLemonLoaf,GingerCookie,ChocolateChipCookie,GranolaCookie,CocoaChiaBites,PeanutButterBites,OvernightOats,EggCheeseWrap,EggBanconWrap,EggSausageWrap,ChickpeaWrap,BeanBurrito,CoconutWrap,VeggieWrap))
    conn.commit()
    return randId

def getAllCashboxes():
    
    db = conn.cursor()
    db.execute('Select * from cashbox')
    cashbox_data = []
    for row in db:
        cashbox = {"ID":row[0],"hundred_Value":row[1],"fifty_Value":row[2],"twenty_Value":row[3],"ten_Value":row[4],"five_Value":row[5],"two_Value":row[6],"one_Value":row[7],"quarter_Value":row[8],"dime_Value":row[9],"nickel_Value":row[10],"date":row[11]}
        cashbox_data.append(cashbox)
    return cashbox_data

def getAllReports():
    
    db = conn.cursor()
    db.execute('Select * from report')
    report_data = []
    for row in db:
        report = {"ID":row[0],"Netsales":row[1],"Expected_Deposit":row[2],"Tip_Amount":row[3],"Quantity_Of_Orders":row[4],"Deposit":row[5],"Deposit_cashbox":row[6],"tips_cashbox":row[7]}
        report_data.append(report)
    return report_data

def getReportById(id):
    id = int(id)
    c.execute('SELECT * FROM report WHERE `id`=`?`'(id))
    report = c.fetchone()
    return {"ID":report[0],"Netsales":report[1],"Expected_Deposit":report[2],"Tip_Amount":report[3],"Quantity_Of_Orders":report[4],"Deposit":report[5],"Deposit_cashbox":report[6],"tips_cashbox":report[7]}

def getDepositById(id):
    c.execute('SELECT * FROM deposits WHERE `id`=`?`'(id))
    deposit = c.fetchone()
    return{"ID":deposit[0], "cashbox_Id":deposit[1]}

def getTipsById(id):
    c.execute('SELECT * FROM tips WHERE `id`=`?`'(id))
    deposit = c.fetchone()
    return{"ID":deposit[0], "cashbox_Id":deposit[1]}

def getWastesheetById(id):
    c.execute('SELECT * FROM wastesheet WHERE `id`=`?`'(id))
    wastesheet = c.fetchone()
    return {"ID":wastesheet[0],"AppleCranberryMuffin":wastesheet[1],"TripleBerryMuffin":wastesheet[2],"RaspberryScone":wastesheet[3],"Croissant":wastesheet[4],"HamCroissant":wastesheet[5],"QuinoaLoaf":wastesheet[6],"CherryLemonLoaf":wastesheet[7],"GingerCookie":wastesheet[8],"ChocolateChipCookie":wastesheet[9],"GranolaCookie":wastesheet[10],"CocoaChiaBites":wastesheet[11],"PeanutButterBites":wastesheet[12],"OvernightOats":wastesheet[13],"EggCheeseWrap":wastesheet[14],"EggBanconWrap":wastesheet[15],"EggSausageWrap":wastesheet[16],"ChickpeaWrap":wastesheet[17],"BeanBurrito":wastesheet[18],"CoconutWrap":wastesheet[19], "VeggieWrap":wastesheet[20]}

def getAllDeposits():
    c.execute('Select* from deposits')
    deposit_data = []
    for row in c:
        deposit = {"ID":row[0],"cashbox_Id":row[1]}
        deposit_data.append(deposit)
    return deposit_data

def getAllTips():
    c.execute('Select * from tips')
    tips_data = []
    for row in c:
        tips = {"ID":row[0],"cashbox_Id":row[1]}
        tips_data.append(tips)
    return tips_data

def getAllWastesheets():
    c.execute('Select * from wastesheet')
    wastesheet_data = []
    for row in c:
        wastesheet = {"ID":row[0],"AppleCranberryMuffin":row[1],"TripleBerryMuffin":row[2],"RaspberryScone":row[3],"Croissant":row[4],"HamCroissant":row[5],"QuinoaLoaf":row[6],"CherryLemonLoaf":row[7],"GingerCookie":row[8],"ChocolateChipCookie":row[9],"GranolaCookie":row[10],"CocoaChiaBites":row[11],"PeanutButterBites":row[12],"OvernightOats":row[13],"EggCheeseWrap":row[14],"EggBanconWrap":row[15],"EggSausageWrap":row[16],"ChickpeaWrap":row[17],"BeanBurrito":row[18],"CoconutWrap":row[19], "VeggieWrap":row[20]}
        wastesheet_data.append(wastesheet)
    return wastesheet_data
