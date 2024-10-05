from publicUseFunction import importPackage, dbConnection
back_AgencyPersonalInfoImport = importPackage.Blueprint(
    'back_AgencyPersonalInfoImport', __name__)
back_AgencyPersonalInfoImport.secret_key = 'abc'

pool = importPackage.psycopg2.pool.ThreadedConnectionPool(
    minconn=1, maxconn=999999999999, dsn=importPackage.DB_URI)

conn = importPackage.conn


@back_AgencyPersonalInfoImport.route('/backAgencyPersonalInfoImport', methods=['GET', 'POST'])
def backAgencyPersonalInfoImport():

    user_id = importPackage.session.get("user_id")
    user_name = importPackage.session.get("user_name")

    return importPackage.render_template('後台網頁/back_02_Registration_Management/back_02_Agency_Register/back_AgencyPersonalInfoImport.html',user_name = user_name)
