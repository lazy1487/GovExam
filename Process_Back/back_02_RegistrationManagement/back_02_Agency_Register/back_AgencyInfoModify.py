from publicUseFunction import importPackage, dbConnection
back_AgencyInfoModify = importPackage.Blueprint(
    'back_AgencyInfoModify', __name__)

pool = importPackage.psycopg2.pool.ThreadedConnectionPool(
    minconn=1, maxconn=10, dsn=importPackage.DB_URI)

conn = importPackage.conn


@back_AgencyInfoModify.route('/backAgencyInfoModify', methods=['GET', 'POST'])
def backAgencyInfoModify():

    user = importPackage.session['user_name']
    current_time = importPackage.datetime.datetime.now()
    formatted_time = current_time.strftime("%Y/%m/%d")

    conn = pool.getconn()
    cursor = conn.cursor()

    oldAgencyID = str(importPackage.request.args.get('AgencyID'))

    if importPackage.request.method == "POST":
        cur = conn.cursor()
        oldAgencyID = importPackage.request.form['oldAgencyID']
        AgencyID = importPackage.request.form['AgencyID']
        Agency = importPackage.request.form['Agency']
        AreaCode = importPackage.request.form['AreaCode']
        Address = importPackage.request.form['Address']
        Phone = importPackage.request.form['Phone']
        Fax = importPackage.request.form['Fax']

        try:
            with conn.cursor() as cursor:
                cursor = conn.cursor()
                cursor.execute("""UPDATE "back_AgencyInfo" SET "AgencyID"=%s, "Agency"=%s,"AreaCode"=%s,
                                                               "Address"=%s,"Phone"=%s,"Fax"=%s WHERE "AgencyID"=%s""",
                               (AgencyID, Agency, AreaCode, Address, Phone, Fax, oldAgencyID))
                conn.commit()

        except Exception as e:
            result = None
            print('Error')
        else:
            cursor.execute(
                """SELECT * FROM "back_AgencyInfo" WHERE "AgencyID" = %s """, (AgencyID,))
            result = cursor.fetchall()
        finally:
            cursor.close()
            pool.putconn(conn)
        return importPackage.render_template('後台網頁/back_02_Registration _Management/back_02_Agency_Register/back_AgencyInfoModify.html', result=result, Handler=user, DateTime=formatted_time)
    else:
        try:
            with conn.cursor() as cursor:
                cursor.execute(
                    """SELECT * FROM "back_AgencyInfo" WHERE "AgencyID" = %s""", (oldAgencyID,))
                result = cursor.fetchall()
        except Exception as e:
            result = None
            print('ErrorB')
        finally:
            cursor.close()
            pool.putconn(conn)
        return importPackage.render_template('後台網頁/back_02_Registration _Management/back_02_Agency_Register/back_AgencyInfoModify.html', result=result, Handler=user, DateTime=formatted_time, AgencyID=oldAgencyID)
