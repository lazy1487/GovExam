from publicUseFunction import importPackage, dbConnection
back_AgencyInfoImport = importPackage.Blueprint(
    'back_AgencyInfoImport', __name__)
back_AgencyInfoImport.secret_key = 'abc'
conn = importPackage.conn
pool = importPackage.psycopg2.pool.ThreadedConnectionPool(
    minconn=1, maxconn=999999999999, dsn=importPackage.DB_URI)


@back_AgencyInfoImport.route('/backAgencyInfoImport', methods=['GET', 'POST'])
def backAgencyInfoImport():

    user_id = importPackage.session.get("user_id")
    user_name = importPackage.session.get("user_name")

    return importPackage.render_template('後台網頁/back_02_Registration_Management/back_02_Agency_Register/back_AgencyInfoImport.html',user_name=user_name)
