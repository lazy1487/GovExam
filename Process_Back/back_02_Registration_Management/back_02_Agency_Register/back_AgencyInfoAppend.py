from publicUseFunction import importPackage, dbConnection
back_AgencyInfoAppend = importPackage.Blueprint(
    'back_AgencyInfoAppend', __name__)

back_AgencyInfoConAppend = importPackage.Blueprint(
    'back_AgencyInfoConAppend', __name__)

pool = importPackage.psycopg2.pool.ThreadedConnectionPool(
    minconn=1, maxconn=10, dsn=importPackage.DB_URI)


@back_AgencyInfoAppend.route('/backAgencyInfoAppend', methods=['GET', 'POST'])
@back_AgencyInfoConAppend.route('/backAgencyInfoAppend', methods=['GET', 'POST'])
def backAgencyInfoAppend():

    current_time = importPackage.datetime.datetime.now()
    formatted_time = current_time.strftime("%Y/%m/%d")

    user_id = importPackage.session.get("user_id")
    user_name = importPackage.session.get("user_name")

    conn = pool.getconn()
    cursor = conn.cursor()

    if importPackage.request.method == "POST":
        cur = conn.cursor()
        hiddenAgencyDepartmentID = importPackage.request.form['hiddenAgencyDepartmentID']
        hiddenAgencyDepartmentName = importPackage.request.form['hiddenAgencyDepartmentName']
        hiddenAgencyDepartmentAreaCode = importPackage.request.form['hiddenAgencyDepartmentAreaCode']
        hiddenAgencyDepartmentAddress = importPackage.request.form['hiddenAgencyDepartmentAddress']
        hiddenAgencyDepartmentTyped= importPackage.request.form['hiddenAgencyDepartmentTyped']
        hiddenAgencyaffiliated = importPackage.request.form['hiddenAgencyaffiliated']
        hiddenAgencyDepartmentPhone = importPackage.request.form['hiddenAgencyDepartmentPhone']
        hiddenAgencyDepartmentFax = importPackage.request.form['hiddenAgencyDepartmentFax']
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO "back_AgencyInfo" 
                    ("AgencyDepartmentID", "AgencyDepartmentName","AgencyDepartmentAreaCode","AgencyDepartmentAddress",
                     "AgencyDepartmentTyped","Agencyaffiliated","AgencyDepartmentPhone","AgencyDepartmentFax","AgencyDepartmentIsUse") 
            VALUES  (%s, %s, %s, %s, 
                     %s, %s, %s, %s, %s)""",
                    (hiddenAgencyDepartmentID, hiddenAgencyDepartmentName, hiddenAgencyDepartmentAreaCode, hiddenAgencyDepartmentAddress,
                     hiddenAgencyDepartmentTyped, hiddenAgencyaffiliated,hiddenAgencyDepartmentPhone,hiddenAgencyDepartmentFax,"N"))
        conn.commit()
        conn.close()
    return importPackage.render_template('後台網頁/back_02_Registration_Management/back_02_Agency_Register/back_AgencyInfoAppend.html', user_name=user_name, DateTime=formatted_time)
