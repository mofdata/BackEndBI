import os 

DB_USER = os.environ.get("DB_USER_NAME", 'ifmis')
DB_PASSWORD = os.environ.get("DB_USER_PASSWORD", "oracle123")
DB_SERVER = os.environ.get("DB_SERVER", "10.1.9.213")
DB_PORT = os.environ.get("DB_PORT", "1521")
ORACLE_DB_SERVICE = os.environ.get("DB_SERVICE", "orclpdb1")
ORACLE_DB_CONNECT = "{}:{}/{}".format(DB_SERVER, DB_PORT, ORACLE_DB_SERVICE) or "10.1.9.213:1521/orclpdb1"
WEB_PORT = os.environ.get("PORT", "9000")
