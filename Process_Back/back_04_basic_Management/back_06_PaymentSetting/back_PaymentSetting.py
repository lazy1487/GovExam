from publicUseFunction import importPackage, dbConnection
back_PaymentSetting = importPackage.Blueprint('back_PaymentSetting', __name__)

pool = importPackage.psycopg2.pool.ThreadedConnectionPool(
    minconn=1, maxconn=10, dsn=importPackage.DB_URI)


@back_PaymentSetting.route('/backPaymentSetting', methods=['GET', 'POST'])
def backPaymentSetting():

    current_time = importPackage.datetime.datetime.now()
    formatted_time = current_time.strftime("%Y/%m/%d")

    user_id = importPackage.session['user_id']
    user_name = importPackage.session['user_name']

    conn = pool.getconn()
    cursor = conn.cursor()

    if importPackage.request.method == "POST":
        MerchantID = importPackage.request.form['MerchantID']
        HashKey = importPackage.request.form['HashKey']
        HashIV = importPackage.request.form['HashIV']
        PaymentReminderText = importPackage.request.form['PaymentReminderText']
        CreditcardReminderText = importPackage.request.form['CreditcardReminderText']
        WebATMReminderText = importPackage.request.form['WebATMReminderText']
        PhysicalATMReminderText = importPackage.request.form['PhysicalATMReminderText']
        BarcodeReminderText = importPackage.request.form['BarcodeReminderText']
        try:
            with conn.cursor() as cursor:
                cursor = conn.cursor()
                cursor.execute("""
                Update "back_PaymentSetting" Set "MerchantID"=%s,"HashKey"=%s, "HashIV"=%s,"PaymentReminderText"=%s,
                            "CreditcardReminderText"=%s, "WebATMReminderText"=%s, "PhysicalATMReminderText"=%s, "BarcodeReminderText"=%s """,
                               (MerchantID, HashKey, HashIV, PaymentReminderText, CreditcardReminderText, WebATMReminderText, PhysicalATMReminderText, BarcodeReminderText))
                conn.commit()

        except Exception as e:
            result = None
            print('ErrorA')
        else:
            cursor.execute(
                """SELECT * FROM "back_PaymentSetting" """)
            result = cursor.fetchall()
        finally:
            cursor.close()
            conn.close()
            pool.putconn(conn)
        return importPackage.render_template('後台網頁/back_04_basic_Management/back_06_PaymentSetting/back_PaymentSetting.html', result=result, user_name=user_name, DateTime=formatted_time)
    else:
        try:
            with conn.cursor() as cursor:
                cursor = conn.cursor()
                cursor.execute(
                    """SELECT * FROM "back_PaymentSetting" """)
                result = cursor.fetchall()
        except Exception as e:
            result = None
            print('ErrorB')
        finally:
            cursor.close()
            pool.putconn(conn)

        return importPackage.render_template('後台網頁/back_04_basic_Management/back_06_PaymentSetting/back_PaymentSetting.html', result=result, user_name=user_name, DateTime=formatted_time)
