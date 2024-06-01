from publicUseFunction import importPackage, dbConnection
back_AgencyPersonalInfo = importPackage.Blueprint(
    'back_AgencyPersonalInfo', __name__)
back_AgencyPersonalInfo.secret_key = 'abc'
conn = importPackage.conn

@back_AgencyPersonalInfo.route('/backAgencyPersonalInfo', methods=['GET', 'POST'])
def backExamRegister():

    with conn.cursor() as cursor:
        cursor.execute("""SELECT "AgencyPersonName","AgencyPersonEmail","AgencyPersonPhone",
                              "AgencyPersonID","Agency" FROM "back_AgencyPersonalInfo" """)
        result = cursor.fetchall()
    return importPackage.render_template('後台網頁/back_02_Registration _Management/back_02_Agency_Register/back_AgencyPersonalInfo.html',result=result)
