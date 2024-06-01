from publicUseFunction import importPackage, dbConnection
back_AgencyInfoAppend = importPackage.Blueprint(
    'back_AgencyInfoAppend', __name__)

pool = importPackage.psycopg2.pool.ThreadedConnectionPool(
    minconn=1, maxconn=10, dsn=importPackage.DB_URI)


@back_AgencyInfoAppend.route('/backAgencyInfoAppend', methods=['GET', 'POST'])
def backAgencyInfoAppend():

    user = importPackage.session['user_id']
    current_time = importPackage.datetime.datetime.now()
    formatted_time = current_time.strftime("%Y/%m/%d")

    conn = pool.getconn()
    cursor = conn.cursor()

    if importPackage.request.method == "POST":
        cur = conn.cursor()
        AgencyID = importPackage.request.form['AgencyID']
        Agency = importPackage.request.form['Agency']
        AreaCode = importPackage.request.form['AreaCode']
        Address = importPackage.request.form['Address']
        Phone = importPackage.request.form['Phone']
        Fax = importPackage.request.form['Fax']
        # print(AgencyID,Agency,AreaCode,Address,Phone,Fax)
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO "back_AgencyInfo" 
                    ("AgencyID", "Agency","AreaCode","Address","Phone","Fax","AgencyIsUse") 
            VALUES  (%s, %s, %s, %s, %s, %s,%s)""",
                    (AgencyID, Agency, AreaCode, Address, Phone, Fax, "N"))
        conn.commit()
        conn.close()
    return importPackage.render_template('後台網頁/back_02_Registration _Management/back_02_Agency_Register/back_AgencyInfoAppend.html', Handler=user, DateTime=formatted_time)
