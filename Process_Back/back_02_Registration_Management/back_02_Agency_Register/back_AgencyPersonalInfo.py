from publicUseFunction import importPackage, dbConnection
back_AgencyPersonalInfo = importPackage.Blueprint(
    'back_AgencyPersonalInfo', __name__)
back_AgencyPersonalInfo.secret_key = 'abc'
conn = importPackage.conn

@back_AgencyPersonalInfo.route('/backAgencyPersonalInfo', methods=['GET', 'POST'])
def backExamRegister():

    user_id = importPackage.session.get("user_id")
    user_name = importPackage.session.get("user_name")

    with conn.cursor() as cursor:
        cursor.execute("""SELECT * FROM "back_AgencyPersonalInfo" """)
        result = cursor.fetchall()
    return importPackage.render_template('後台網頁/back_02_Registration_Management/back_02_Agency_Register/back_AgencyPersonalInfo.html',result=result,user_name=user_name)
