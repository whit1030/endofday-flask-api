#Using SQLite3
import sqlite3

conn = sqlite3.connect('endofday.db',check_same_thread=False)

c= conn.cursor()

# c.execute(''' CREATE TABLE `cashbox` (
#   `cashbox_ID` int(16) NOT NULL,
#   `hundred_Value` float(10) DEFAULT 0,
#   `fifty_Value` float(10) DEFAULT 0,
#   `twenty_Value` float(10) DEFAULT 0,
#   `ten_Value` float(10) DEFAULT 0,
#   `five_Value` float(10) DEFAULT 0,
#   `two_Value` float(10) DEFAULT 0,
#   `one_Value` float(10) DEFAULT 0,
#   `quarter_Value` float(10) DEFAULT 0,
#   `dime_Value` float(10) DEFAULT 0,
#   `nickel_Value` float(10) DEFAULT 0,
#   `date` date 
# )''')

# c.execute('CREATE TABLE `deposits` (`ID` int(16) NOT NULL,`cashbox_ID` int(11) NOT NULL')
# c.execute('CREATE TABLE `tips` (`ID` int(16) NOT NULL,`cashbox_ID` int(11) NOT NULL)')
#  c.execute('CREATE TABLE `report` (`ID` int(16) NOT NULL,`Netsales` int(16) NOT NULL,`Expected_Deposit` float(16) NOT NULL,`Tip_Amount` float(16) NOT NULL,`Quantity_Of_Orders` int(16) NOT NULL,`Deposit` float(16) NOT NULL,`deposit_cashbox` INT(16) NOT NULL,`tips_cashbox` INT(16) NOT NULL)')
# c.execute('CREATE TABLE `wastesheet`(`ID` int(16) NOT NULL,`AppleCranberryMuffin` int(16) NULL DEFAULT NULL,`TripleBerryMuffin` int(16) NULL DEFAULT NULL,`RaspberryScone` int(16) NULL DEFAULT NULL,`Croissant` int(16) NULL DEFAULT NULL,`HamCroissant` int(16) NULL DEFAULT NULL,`QuinoaLoaf` int(16) NULL DEFAULT NULL,`CherryLemonLoaf` int(16) NULL DEFAULT NULL,`GingerCookie` int(16) NULL DEFAULT NULL,`ChocolateChipCookie` int(16) NULL DEFAULT NULL,`GranolaCookie` int(16) NULL DEFAULT NULL,`CocoaChiaBites` int(16) NULL DEFAULT NULL,`PeanutButterBites` int(16) NULL DEFAULT NULL,`OvernightOats` int(16) NULL DEFAULT NULL,`EggCheeseWrap` int(16) NULL DEFAULT NULL,`EggBanconWrap` int(16) NULL DEFAULT NULL,`EggSausageWrap` int(16) NULL DEFAULT NULL,`ChickpeaWrap` int(16) NULL DEFAULT NULL,`BeanBurrito` int(16) NULL DEFAULT NULL,`CoconutWrap` int(16) NULL DEFAULT NULL,`VeggieWrap` int(16) NULL DEFAULT NULL)')
# conn.commit()

# conn.close()

# c.execute('''
# DROP TABLE deposits;
# ''')
# c.execute('''
# CREATE TABLE `deposits` (
#     ID int(16) PRIMARY KEY,
#     cashbox_ID int(11) NOT NULL,
#     FOREIGN KEY(cashbox_ID) REFERENCES cashbox (cashbox_ID)

# );
# ''')

# c.execute('''
# DROP TABLE tips;
# ''')
# c.execute('''
# CREATE TABLE `tips` (
#     ID int(16) PRIMARY KEY,
#     cashbox_ID int(11) NOT NULL,
#     FOREIGN KEY(cashbox_ID) REFERENCES cashbox (cashbox_ID)

# );
# ''')

# c.execute('''
#  DROP TABLE report;
#  ''')


# c.execute('''
# CREATE TABLE `report` (
#     `ID` int(16) NOT NULL,
#     `Netsales` int(16) NOT NULL,
#     `Expected_Deposit` float(16) NOT NULL,
#     `Tip_Amount` float(16) NOT NULL,
#     `Quantity_Of_Orders` int(16) NOT NULL,
#     `Deposit` float(16) NOT NULL,
#     `deposit_cashbox` INT(16) NOT NULL REFERENCES deposits(ID),
#     `tips_cashbox` INT(16) NOT NULL REFERENCES tips(ID)
    
#     );
    
#     ''')
