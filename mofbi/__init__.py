import os 
import json 
from flask import Flask 
import config
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE={
            "user": config.DB_USER,
            "password": config.DB_PASSWORD,
            "dsn": config.ORACLE_DB_CONNECT,
        },
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello

    
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    
    
    @app.route('/')
    def index():
        from .db import get_db 
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

        rows = json.dumps(rows)

        return rows
    

    

    return app