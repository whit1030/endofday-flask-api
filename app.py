#USING FLASK RESTFUL
from email import message
from xml.etree.ElementTree import tostring
from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
from parsers import parser,safe_parser,waste_parser
from calculations import CashboxWizard, depositCashboxWizard
from databaseCreate import conn, c
from databaseFunctions import UpdateCashbox, UpdateReport, UpdateTipsDeposit, getAllCashboxes, getAllDeposits, getAllReports, getAllTips, getAllWastesheets, getDepositById, getReportById, getTipsById, getWastesheetById, updateWastesheet

from classes import Cashbox

#CREATE FLASK APP
app = Flask(__name__)
#Create API Object
api = Api(app)





class WastesheetList(Resource):
    #get all wastesheets
    def get(self):
        return getAllWastesheets()
    
class Wastesheet(Resource):
    def get(self):
        args = waste_parser.parse_args()
        return getWastesheetById(args['wastesheetId'])

    def post(self):
        args = waste_parser.parse_args()
        return updateWastesheet(args['AppleCranberryMuffin'],args['TripleBerryMuffin'],args['RaspberryScone'],args['Croissant'],args['HamCroissant'],args['QuinoaLoaf'],args['CherryLemonLoaf'],args['GingerCookie'],args['ChocolateChipCookie'],args['GranolaCookie'],args['CocoaChiaBites'],args['PeanutButterBites'],args['OvernightOats'],args['EggCheeseWrap'],args['EggBanconWrap'],args['EggSausageWrap'],args['ChickpeaWrap'],args['BeanBurrito'],args['CoconutWrap'],args['VeggieWrap'])

class TipsList(Resource):
    def get(self):
        return getAllTips()

class Tips(Resource):
    def get(self):
        args = parser.parse_args()
        return getTipsById(args['tipsId'])


class DepositsList(Resource):
    def get(self):
        return getAllDeposits()

class Deposits(Resource):
    def get(self):
        args = parser.parse_args()
        return getDepositById(args['depositId'])

#class SafeList(Resource):
 #   def get(self):
    #args = getallSafe


class ReportList(Resource):
   def get(self):
    return getAllReports()

class Report(Resource):
    def get(self, report_id):
        args = parser.parse_args()
        return getReportById(report_id)
    
    

class Cashboxcall(Resource):
    #get all cashboxes
    def get(self):
        return getAllCashboxes()
    #gets user inputs, stores them in database and returns json format of end report.
    def post(self):
        args = parser.parse_args()
        
        dailyCashbox = Cashbox(args['hundred'],args['fifty'],args['twenty'],args['ten'],args['five'],args['two'],args['one'],args['quarter'],args['dime'],args['nickel']) 
        tipsCashbox = CashboxWizard(dailyCashbox, args['TipAmount'])
        depositCashbox = depositCashboxWizard(dailyCashbox)
        tipsCashboxId = UpdateCashbox(tipsCashbox)
        depositCashboxId = UpdateCashbox(depositCashbox)
        tipsDeposit = UpdateTipsDeposit(tipsCashboxId, depositCashboxId)
        reportId = UpdateReport(args['NetSales'], args['ExpectedDeposit'], args['TipAmount'], args['QuantityOrders'], depositCashbox.getTotal(), depositCashboxId, tipsCashboxId )
        
        return reportId

api.add_resource(Cashboxcall, '/cash/')
api.add_resource(ReportList,'/report/')
api.add_resource(DepositsList, '/deposit/')
api.add_resource(TipsList, '/tips/')
api.add_resource(Wastesheet, '/wastesheet/')
if __name__ == '__main__':
    app.run(debug=True)