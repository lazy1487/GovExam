from publicUseFunction import importPackage, dbConnection
back_EnvironmentSetting = importPackage.Blueprint(
    'back_EnvironmentSetting', __name__)
conn = importPackage.conn

pool = importPackage.psycopg2.pool.ThreadedConnectionPool(
    minconn=1, maxconn=999999999999, dsn=importPackage.DB_URI)


@back_EnvironmentSetting.route('/backEnvironmentSetting', methods=['GET', 'POST'])
def backEnvironmentSetting():
    user_id = importPackage.session.get('user_id')
    user = importPackage.session.get('user_name')
    current_time = importPackage.datetime.datetime.now()
    formatted_time = current_time.strftime("%Y/%m/%d")

    conn = pool.getconn()

    user_id = importPackage.session.get('user_id')
    user_name = importPackage.session.get('user_name')
    user_email = importPackage.session.get('user_email')

    exam_Registration = importPackage.session.get('exam_Registration')
    agency_Registration = importPackage.session.get('agency_Registration')

    system_accountAdd = importPackage.session.get('system_accountAdd')
    system_accountModify = importPackage.session.get('system_accountModify')
    system_passwordReset = importPackage.session.get('system_passwordReset')
    system_Environment = importPackage.session.get('system_Environment')
    system_SMTPSetting = importPackage.session.get('system_SMTPSetting')
    system_SystemSearch = importPackage.session.get('system_SystemSearch')

    basic_CarouselSetting = importPackage.session.get('basic_CarouselSetting')
    basic_FastLinkSetting = importPackage.session.get('basic_FastLinkSetting')
    basic_NewSetting = importPackage.session.get('basic_NewSetting')
    basic_NormalQuestionSetting = importPackage.session.get(
        'basic_NormalQuestionSetting')
    basic_NoticeSetting = importPackage.session.get('basic_NoticeSetting')
    basic_PaymentSetting = importPackage.session.get('basic_PaymentSetting')
    basic_UnitImageSetting = importPackage.session.get(
        'basic_UnitImageSetting')

    try:
        with conn.cursor() as cursor:
            cursor.execute(""" select * from "back_EnvironmentSetting" """)
            result = cursor.fetchall()
    except Exception as e:
        result = None
        print('Error')
    finally:
        pool.putconn(conn)

    if importPackage.request.method == "POST":

        switchcarouselsetting = importPackage.request.form['hiddenswitchcarouselsetting']
        UpLoadTime = importPackage.request.form['hiddenUpLoadTime']
        RemoveTime = importPackage.request.form['hiddenRemoveTime']
        inputWebTitle = importPackage.request.form['hiddeninputWebTitle']
        inputEmailTitle = importPackage.request.form['hiddeninputEmailTitle']
        inputDescription = importPackage.request.form['hiddeninputDescription']
        inputAddress = importPackage.request.form['hiddeninputAddress']
        inputswitchboard = importPackage.request.form['hiddeninputswitchboard']
        inputFax = importPackage.request.form['hiddeninputFax']
        inputPrivacy = importPackage.request.form['hiddeninputPrivacy']
        inputuseraccount = importPackage.request.form['hiddenuseraccount']
        conn = pool.getconn()
        try:
            with conn.cursor() as cursor:
                cursor.execute("""
                    update "back_EnvironmentSetting"
                            SET "switchcarouselsetting"=%s,"UpLoadTime"=%s,"RemoveTime"=%s,
                            "maintainTitle"=%s,"maintainEmail"=%s,"maintainContext"=%s,"inputAddress"=%s,
                            "inputswitchboard"=%s,"inputFax"=%s,"inputPrivacy"=%s
                    where "inputuseraccount"=%s """,
                               (switchcarouselsetting, UpLoadTime, RemoveTime,
                                inputWebTitle, inputEmailTitle, inputDescription, inputAddress,
                                inputswitchboard, inputFax, inputPrivacy, inputuseraccount))
                conn.commit()
        except Exception as e:
            print('Error:', e)
        finally:
            pool.putconn(conn)

    return importPackage.render_template('後台網頁/back_03_System_Management/back_03_Environment/Back_EnvironmentSetting.html', result=result, userid=user_id, Handler=user_name, DateTime=formatted_time,
                                         user_id=user_id,
                                         user_name=user_name,
                                         user_email=user_email,
                                         exam_Registration=exam_Registration,
                                         agency_Registration=agency_Registration,
                                         system_accountAdd=system_accountAdd,
                                         system_accountModify=system_accountModify,
                                         system_passwordReset=system_passwordReset,
                                         system_Environment=system_Environment,
                                         system_SMTPSetting=system_SMTPSetting,
                                         system_SystemSearch=system_SystemSearch,
                                         basic_CarouselSetting=basic_CarouselSetting,
                                         basic_FastLinkSetting=basic_FastLinkSetting,
                                         basic_NewSetting=basic_NewSetting,
                                         basic_NormalQuestionSetting=basic_NormalQuestionSetting,
                                         basic_NoticeSetting=basic_NoticeSetting,
                                         basic_PaymentSetting=basic_PaymentSetting,
                                         basic_UnitImageSetting=basic_UnitImageSetting)
