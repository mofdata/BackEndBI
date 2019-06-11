import json

from flask_restful import Resource

from mofbi.db import get_db


class ExpenditureResource(Resource):
    """Donor wise six year Expenditure report"""
    def get(self):
        connection = get_db() 
        cursor = connection.cursor()

        query = ("SELECT d.donor_code,d.donor_edesc, "
        "sum(decode(e.BUD_YEAR,'2070/71',decode(substr(source_type_code,1,1),'0',e.expenditure_amount/1000,0),0))exp_gon70, "
        "sum(decode(e.BUD_YEAR,'2070/71',decode(substr(source_type_code,1,1),'1',e.expenditure_amount/1000,0),0))exp_grant70, "
        "sum(decode(e.BUD_YEAR,'2070/71',decode(substr(source_type_code,1,1),'2',e.expenditure_amount/1000,0),0))exp_loan70, "
        "sum(decode(e.BUD_YEAR,'2071/72',decode(substr(source_type_code,1,1),'0',e.expenditure_amount/1000,0),0))exp_gon71, "
        "sum(decode(e.BUD_YEAR,'2071/72',decode(substr(source_type_code,1,1),'1',e.expenditure_amount/1000,0),0))exp_grant71, "
        "sum(decode(e.BUD_YEAR,'2071/72',decode(substr(source_type_code,1,1),'2',e.expenditure_amount/1000,0),0))exp_loan71, "
        "sum(decode(e.BUD_YEAR,'2072/73',decode(substr(source_type_code,1,1),'0',e.expenditure_amount/1000,0),0))exp_gon72, "
        "sum(decode(e.BUD_YEAR,'2072/73',decode(substr(source_type_code,1,1),'1',e.expenditure_amount/1000,0),0))exp_grant72, "
        "sum(decode(e.BUD_YEAR,'2072/73',decode(substr(source_type_code,1,1),'2',e.expenditure_amount/1000,0),0))exp_loan72, "
        "sum(decode(e.BUD_YEAR,'2073/74',decode(substr(source_type_code,1,1),'0',e.expenditure_amount/1000,0),0))exp_gon73, "
        "sum(decode(e.BUD_YEAR,'2073/74',decode(substr(source_type_code,1,1),'1',e.expenditure_amount/1000,0),0))exp_grant73, "
        "sum(decode(e.BUD_YEAR,'2073/74',decode(substr(source_type_code,1,1),'2',e.expenditure_amount/1000,0),0))exp_loan73, "
        "sum(decode(e.BUD_YEAR,'2074/75',decode(substr(source_type_code,1,1),'0',e.expenditure_amount/1000,0),0))exp_gon74, "
        "sum(decode(e.BUD_YEAR,'2074/75',decode(substr(source_type_code,1,1),'1',e.expenditure_amount/1000,0),0))exp_grant74, "
        "sum(decode(e.BUD_YEAR,'2074/75',decode(substr(source_type_code,1,1),'2',e.expenditure_amount/1000,0),0))exp_loan74, "
        "sum(decode(e.BUD_YEAR,'2075/76',decode(substr(source_type_code,1,1),'0',e.expenditure_amount/1000,0),0))exp_gon75, "
        "sum(decode(e.BUD_YEAR,'2075/76',decode(substr(source_type_code,1,1),'1',e.expenditure_amount/1000,0),0))exp_grant75, "
        "sum(decode(e.BUD_YEAR,'2075/76',decode(substr(source_type_code,1,1),'2',e.expenditure_amount/1000,0),0))exp_loan75, "
        "sum(e.expenditure_amount) from fmis.fmis_expenditure_detail e,c_donor d "
        "where d.donor_code=e.donor_code "
        "group by d.donor_code,d.donor_edesc "
        "order by d.donor_code ")

        db_columns = (
                "donor_code",
                "donor_edesc",
                "exp_gon70",
                "exp_grant70",
                "exp_loan70",
                "exp_gon71",
                "exp_grant71",
                "exp_loan71",
                "exp_gon72",
                "exp_grant72",
                "exp_loan72",
                "exp_gon73",
                "exp_grant73",
                "exp_loan73",
                "exp_gon74",
                "exp_grant74",
                "exp_loan74",
                "exp_gon75",
                "exp_grant75",
                "exp_loan75",
                "total_expenditure",
        )

        cursor.execute(query)
        rows = []
        for row in cursor: 
                data = {}
                for key, value in zip(db_columns, row):
                        data[key] = value 
                rows.append(data)
        return rows
    
    def put(self):
        pass 

class BudgetResource(Resource):
    """Donarwise six year budget report"""
    cols = [
    "donor_code",
    "donor_edesc",
    "bud_gon70",
    "bud_grant70",
    "bud_loan70",
    "bud_gon71",
    "bud_grant71",
    "bud_loan71",
    "bud_gon72",
    "bud_grant72",
    "bud_loan72",
    "bud_gon73",
    "bud_grant73",
    "bud_loan73",
    "bud_gon74",
    "bud_grant74",
    "bud_loan74",
    "bud_gon75",
    "bud_grant75",
    "bud_loan75",
    ]
    def get(self):
        query = ("SELECT d.donor_code,d.donor_edesc, "
        "sum(decode(b.BUD_YEAR,'2070/71',decode(substr(s.source_type_code,1,1),'0',b.BUDGET_AMOUNT,0),0)) bud_gon70, "
        "sum(decode(b.BUD_YEAR,'2070/71',decode(substr(s.source_type_code,1,1),'2',b.BUDGET_AMOUNT,0),0))bud_loan70, "
        "sum(decode(b.BUD_YEAR,'2071/72',decode(substr(s.source_type_code,1,1),'0',b.BUDGET_AMOUNT,0),0))bud_gon71, "
        "sum(decode(b.BUD_YEAR,'2071/72',decode(substr(s.source_type_code,1,1),'1',b.BUDGET_AMOUNT,0),0))bud_grant71, "
        "sum(decode(b.BUD_YEAR,'2071/72',decode(substr(s.source_type_code,1,1),'2',b.BUDGET_AMOUNT,0),0))bud_loan71, "
        "sum(decode(b.BUD_YEAR,'2072/73',decode(substr(s.source_type_code,1,1),'0',b.BUDGET_AMOUNT,0),0))bud_gon72, "
        "sum(decode(b.BUD_YEAR,'2072/73',decode(substr(s.source_type_code,1,1),'1',b.BUDGET_AMOUNT,0),0))bud_grant72, "
        "sum(decode(b.BUD_YEAR,'2072/73',decode(substr(s.source_type_code,1,1),'2',b.BUDGET_AMOUNT,0),0))bud_loan72, "
        "sum(decode(b.BUD_YEAR,'2073/74',decode(substr(s.source_type_code,1,1),'0',b.BUDGET_AMOUNT,0),0))bud_gon73, "
        "sum(decode(b.BUD_YEAR,'2073/74',decode(substr(s.source_type_code,1,1),'1',b.BUDGET_AMOUNT,0),0))bud_grant73, "
        "sum(decode(b.BUD_YEAR,'2073/74',decode(substr(s.source_type_code,1,1),'2',b.BUDGET_AMOUNT,0),0))bud_loan73, "
        "sum(decode(b.BUD_YEAR,'2074/75',decode(substr(s.source_type_code,1,1),'0',b.BUDGET_AMOUNT,0),0))bud_gon74, "
        "sum(decode(b.BUD_YEAR,'2074/75',decode(substr(s.source_type_code,1,1),'1',b.BUDGET_AMOUNT,0),0))bud_grant74, "
        "sum(decode(b.BUD_YEAR,'2074/75',decode(substr(s.source_type_code,1,1),'2',b.BUDGET_AMOUNT,0),0))bud_loan74, "
        "sum(decode(b.BUD_YEAR,'2075/76',decode(substr(s.source_type_code,1,1),'0',b.BUDGET_AMOUNT,0),0))bud_gon75, "
        "sum(decode(b.BUD_YEAR,'2075/76',decode(substr(s.source_type_code,1,1),'1',b.BUDGET_AMOUNT,0),0))bud_grant75, "
        "sum(decode(b.BUD_YEAR,'2075/76',decode(substr(s.source_type_code,1,1),'2',b.BUDGET_AMOUNT,0),0))bud_loan75 "
        "FROM FMIS_redbook_expenditure  b, "
        "C_SOURCE_TYPE S, C_SOURCE O,c_donor d "
        "WHERE  "
        "B.SOURCE_TYPE_CODE=S.SOURCE_TYPE_CODE AND "
        "O.SOURCE_CODE=S.SOURCE_CODE and "
        "d.donor_code=b.donor_code "
        "GROUP BY  d.donor_code,d.donor_edesc "
        "order by   d.donor_code,d.donor_edesc "
        )

        connection = get_db() 
        cursor = connection.cursor()
        cursor.execute(query)
        result = []
        for data in cursor:
            record = {}
            for key, value in zip(self.cols, data):
                record[key] = value 
            result.append(record)
        return result

        

    def put(self):
        pass 

class BudgetDistrictDonerWiseResource(Resource):
    """Donor and district wise query report""" 
    query = ("select a.acc_CODE,P.PROJECT_EDESC,d.donor_code,d.donor_edesc,O.DISTRICT_CODE,O.DISTRICT_EDESC ",
    "sum(decode(substr(source_type_code,1,1),'1',e.expenditure_amount/1000,0)) grant1, "
    "sum(decode(substr(source_type_code,1,1),'2',e.expenditure_amount/1000,0)) loan, "
    "sum(e.expenditure_amount/1000) from fmis.fmis_expenditure_detail e,c_donor d,C_PROJECT P,C_ACCOUNT A, LMBS_DISTRICT O "
    "where  e.BUD_YEAR=A.BUD_YEAR AND "
    "e.ACC_CODE=A.ACC_CODE AND "
    "A.BUD_YEAR=P.BUD_YEAR AND "
    "A.PROJECT_CODE=P.PROJECT_CODE AND "
    "d.donor_code=e.donor_code AND  "
    "e.expenditure_amount>0 AND "
    "O.DISTRICT_CODE=e.DISTRICT_CODE and d.donor_code!='110101' and "
    "e.bud_year='2075/76' "
    "group by a.acc_CODE,P.PROJECT_EDESC,d.donor_code,d.donor_edesc,O.DISTRICT_CODE,O.DISTRICT_EDESC "
    "order by a.acc_CODE ")

    def get(self):
        pass 