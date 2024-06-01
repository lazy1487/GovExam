from publicUseFunction import importPackage, dbConnection
back_AgencyInfo = importPackage.Blueprint(
    'back_AgencyInfo', __name__)
back_AgencyInfo.secret_key = 'abc'
conn = importPackage.conn
@back_AgencyInfo.route('/backAgencyInfo', methods=['GET', 'POST'])
def backExamRegister():
    cur = conn.cursor()
    with conn.cursor() as cur:
        cur.execute("""SELECT "AgencyID","Agency","Phone" FROM "back_AgencyInfo" """)
        result = cur.fetchall()
    return importPackage.render_template('後台網頁/back_02_Registration _Management/back_02_Agency_Register/back_AgencyInfo.html',result=result)
