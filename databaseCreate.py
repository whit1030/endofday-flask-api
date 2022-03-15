#Using SQLite3
import sqlite3

conn = sqlite3.connect('endofday.db')

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




# conn.commit()

# conn.close()