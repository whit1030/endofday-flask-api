#USING FLASK RESTFUL
from email import message
from xml.etree.ElementTree import tostring
from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
from parsers import parser,safe_parser,waste_parser
from calculations import CashboxWizard, depositCashboxWizard
from databaseCreate import conn, c
from databaseFunctions import UpdateCashbox, UpdateReport, UpdateTipsDeposit, getAllCashboxes

from classes import Cashbox

#CREATE FLASK APP
app = Flask(__name__)
#Create API Object
api = Api(app)





#class WastesheetList(Resource):
    #get all wastesheets
 #   def get(self):
    #Add waste sheet to waste sheet database
    
class Wastesheet(Resource):
    #def get(self, waste_id)
    #stop if not in database
    #return wastesheet[id]
    def post(self):
        args = waste_parser.parse_args()
        return args

#class TipsList(Resource):
 #   def get(self):
    #args = getallTips

#class Tips(Resource):
    #def get(self, tip_id)
    #stop if not in database
    #return Tipcashbox[id]


#class DepositsList(Resource):
 #   def get(self):
    #args = getallDeposits

#class Deposits(Resource):
    #def get(self, tip_id)
    #stop if not in database
    #return Depositcashbox[id]

#class SafeList(Resource):
 #   def get(self):
    #args = getallSafe


#class ReportList(Resource):
 #   def get(self):
    #args = getallReport

#class Report(Resource):
    #def get(self, tip_id)
    #stop if not in database
    #return Reportcashbox[id]

class Cashboxcall(Resource):
    #get all cashboxes
    def get(self):
        return getAllCashboxes()

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

if __name__ == '__main__':
    app.run(debug=True)