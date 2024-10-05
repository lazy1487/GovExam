from publicUseFunction import importPackage, dbConnection
back_AgencyPersonalInfoAppend = importPackage.Blueprint(
    'back_AgencyPersonalInfoAppend', __name__)
back_AgencyPersonalInfoAppend.secret_key = 'abc'

pool = importPackage.psycopg2.pool.ThreadedConnectionPool(minconn=1, maxconn=999999999999, dsn=importPackage.DB_URI)

conn = importPackage.conn

@back_AgencyPersonalInfoAppend.route('/backAgencyPersonalInfoAppend', methods=['GET', 'POST'])
def backAgencyPersonalInfoAppend():
    
    user = importPackage.session['user_id']
    
    current_time = importPackage.datetime.datetime.now()
    formatted_time = current_time.strftime("%Y/%m/%d")

    user_id = importPackage.session.get("user_id")
    user_name = importPackage.session.get("user_name")
    
    conn = pool.getconn()
    cursor = conn.cursor()

    if importPackage.request.method == "POST":
        hiddeninputName = importPackage.request.form['hiddeninputName']
        hiddeninputID = importPackage.request.form['hiddeninputID']
        hiddeninputAge = importPackage.request.form['hiddeninputAge']
        hiddeninputAddress = importPackage.request.form['hiddeninputAddress']
        hiddeninputPhone = importPackage.request.form['hiddeninputPhone']
        hiddeninputEmail = importPackage.request.form['hiddeninputEmail']
        hiddeninputAgency = importPackage.request.form['hiddeninputAgency']
        hiddeninputAgencyDepa = importPackage.request.form['hiddeninputAgencyDepa']
        hiddeninputAgencyPhone = importPackage.request.form['hiddeninputAgencyPhone']
        hiddeninputAgencyAddress = importPackage.request.form['hiddeninputAgencyAddress']
        # print(AgencyID,Agency,AreaCode,Address,Phone,Fax)

        cur = conn.cursor()
        cur.execute("""
            INSERT INTO "back_AgencyPersonalInfo" 
                    ("AgencyPersonName", "AgencyPersonID","AgencyPersonAddress","AgencyPersonAge","AgencyPersonPhone",
                     "AgencyPersonEmail","Agency","AgencyDepartment","AgencyAddress","AgencyPhone") 
            VALUES  (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                    (hiddeninputName, hiddeninputID, hiddeninputAge, hiddeninputAddress, hiddeninputPhone,
                     hiddeninputEmail,hiddeninputAgency,hiddeninputAgencyDepa,hiddeninputAgencyPhone,hiddeninputAgencyAddress))
        conn.commit()
        conn.close()
        return importPackage.redirect(importPackage.url_for('back_AgencyPersonalInfo.backAgencyPersonalInfo'))
    else:
        try:
            with conn.cursor() as cursor:
                cursor.execute(
                    """SELECT "AgencyPersonName", "AgencyPersonEmail", "AgencyPhone","AgencyPersonID","Agency" FROM "back_AgencyPersonalInfo" """)
                result = cursor.fetchall()
        except:
            result = None
            print('ErrorA')
        finally:
            cursor.close()
            pool.putconn(conn)
        return importPackage.render_template('後台網頁/back_02_Registration_Management/back_02_Agency_Register/back_AgencyPersonalInfoAppend.html',Handler=user,DateTime=formatted_time,user_name=user_name)
