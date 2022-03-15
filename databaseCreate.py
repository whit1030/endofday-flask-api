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
# c.execute('CREATE TABLE `tips` (`ID` int(16) NOT NULL,`cashbox_ID` int(11) NOT NULL')
# c.execute('CREATE TABLE `report` (`ID` int(16) NOT NULL,`Netsales` int(16) NOT NULL,`Expected_Deposit` float(16) NOT NULL,`Tip_Amount` float(16) NOT NULL,`Quantity_Of_Orders` int(16) NOT NULL,`Deposit` float(16) NOT NULL,`deposit_cashbox` float(11) NOT NULL,`tips_cashbox` float(11) NOT NULL)')

# conn.commit()

# conn.close()