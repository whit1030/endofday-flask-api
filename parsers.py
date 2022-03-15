from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse

#Cashbox Parsers
parser = reqparse.RequestParser()


#Cashbox Parsers
parser.add_argument('hundred', type=float, help='Hundred total value in dollars')
parser.add_argument('fifty', type=float, help="fifty total value in dollars")
parser.add_argument('twenty', type=float, help="twenty total value in dollars")
parser.add_argument('ten', type=float, help="ten total value in dollars")
parser.add_argument('five', type=float, help="five total value in dollars")
parser.add_argument('two', type=float, help="two total value in dollars")
parser.add_argument('one', type=float, help="one total value in dollars")
parser.add_argument('quarter', type=float, help="quarter total value in dollars")
parser.add_argument('dime', type=float, help="dime total value in dollars")
parser.add_argument('nickel', type=float, help="nickel total value in dollars")

#Waste Parsers
waste_parser = parser.copy()

waste_parser.add_argument('AppleCranberryMuffin', type=int, help="Quantity of AppleCranberryMuffin")
waste_parser.add_argument('TripleBerryMuffin', type=int, help="Quantity of TripleBerryMuffin")
waste_parser.add_argument('RaspberryScone', type=int, help="Quantity of RaspberryScone")
waste_parser.add_argument('Croissant', type=int, help="Quantity of Croissant")
waste_parser.add_argument('HamCroissant', type=int, help="Quantity of HamCroissant")
waste_parser.add_argument('QuinoaLoaf', type=int, help="Quantity of QuinoaLoaf")
waste_parser.add_argument('CherryLemonLoaf', type=int, help="Quantity of CherryLemonLoaf")
waste_parser.add_argument('GingerCookie', type=int, help="Quantity of GingerCookie")
waste_parser.add_argument('ChocolateChipCookie', type=int, help="Quantity of ChocolateChipCookie")
waste_parser.add_argument('GranolaCookie', type=int, help="Quantity of GranolaCookie")
waste_parser.add_argument('CocoaChiaBites', type=int, help="Quantity of CocoaChiaBites")
waste_parser.add_argument('PeanutButterBites', type=int, help="Quantity of PeanutButterBites")
waste_parser.add_argument('OvernightOats', type=int, help="Quantity of OvernightOats")
waste_parser.add_argument('EggCheeseWrap', type=int, help="Quantity of EggCheeseWrap")
waste_parser.add_argument('EggBanconWrap', type=int, help="Quantity of EggBanconWrap")
waste_parser.add_argument('EggSausageWrap', type=int, help="Quantity of EggSausageWrap")
waste_parser.add_argument('ChickpeaWrap', type=int, help="Quantity of ChickpeaWrap")
waste_parser.add_argument('BeanBurrito', type=int, help="Quantity of BeanBurrito")
waste_parser.add_argument('CoconutWrap', type=int, help="Quantity of CoconutWrap")
waste_parser.add_argument('VeggieWrap', type=int, help="Quantity of VeggieWrap")

#Report Parser



parser.add_argument('NetSales', type=float, help="NetSales for the day")
parser.add_argument('QuantityOrders', type=float, help="Quantity of Orders for the day")
parser.add_argument('TipAmount', type=float, help="Tips made for the day")
parser.add_argument('ExpectedDeposit', type=float, help="Expected deposit for the day")

#Safe Parsers

safe_parser = parser.copy()

safe_parser.add_argument('hundred', type=float, help='Hundred total value in dollars')
safe_parser.add_argument('fifty', type=float, help="fifty total value in dollars")
safe_parser.add_argument('twenty', type=float, help="twenty total value in dollars")
safe_parser.add_argument('ten', type=float, help="ten total value in dollars")
safe_parser.add_argument('five', type=float, help="five total value in dollars")
safe_parser.add_argument('two', type=float, help="two total value in dollars")
safe_parser.add_argument('one', type=float, help="one total value in dollars")
safe_parser.add_argument('quarter', type=float, help="quarter total value in dollars")
safe_parser.add_argument('dime', type=float, help="dime total value in dollars")
safe_parser.add_argument('nickel', type=float, help="nickel total value in dollars")