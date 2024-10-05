from publicUseFunction import importPackage, dbConnection
back_AccountSearchModify = importPackage.Blueprint(
    'back_AccountSearchModify', __name__)
back_AccountSearchModify.secret_key = 'abc'

pool = importPackage.psycopg2.pool.ThreadedConnectionPool(
    minconn=1, maxconn=999999999999, dsn=importPackage.DB_URI)

@back_AccountSearchModify.route('/backaccountSearchModify')
def backAccountSearchModify():
    global user_id, user_name, user_email
    global system_accountAdd, system_accountModify, system_passwordReset,system_Environment, system_SMTPSetting, system_SystemSearch
    global basic_CarouselSetting, basic_FastLinkSetting, basic_NewSetting,basic_NormalQuestionSetting, basic_NoticeSetting, basic_PaymentSetting,basic_UnitImageSetting
    global exam_Registration, agency_Registration
    global formatted_time

    current_time = importPackage.datetime.datetime.now()
    formatted_time = current_time.strftime("%Y/%m/%d")

    conn = pool.getconn()
    cursor = conn.cursor()

    account = str(importPackage.request.args.get('account'))

    user_id = importPackage.session.get('user_id')
    user_name = importPackage.session.get('user_name')
    user_email = importPackage.session.get('user_email')

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
    exam_Registration = importPackage.session.get('exam_Registration')
    agency_Registration = importPackage.session.get('agency_Registration')

    try:
        with conn.cursor() as cursor:
            cursor.execute(
                """SELECT "useraccount", "username", "accountStatus","useripify" FROM "back_AccountSetting" 
                    where useraccount = %s """, (account,))
            result = cursor.fetchall()
            # =====報名管理模組=====
            cursor.execute(
                """Select "ExamRegistration","AgencyRegistration" from "back_AccountSetting"
                   Where useraccount = %s """, (account,))
            registrationResult = cursor.fetchall()
            # =====系統管理模組=====
            cursor.execute(
                """Select "accountadd","accountmodify","passwordReset","environmentsetting","smtpsetting","systemsearch" from "back_AccountSetting"
                   Where useraccount = %s """, (account,))
            systemResult = cursor.fetchall()
            # =====基本管理模組=====
            cursor.execute(
                """Select "carouselsetting","fastlinksetting","newsetting",
                  "normalquestionsetting","noticesetting","paymentsetting","unitimagesetting" from "back_AccountSetting"
                   Where useraccount = %s """, (account,))
            basicResult = cursor.fetchall()
    except:
        result = None
        print('ErrorA')
    finally:
        cursor.close()

    return importPackage.render_template('後台網頁/back_03_System_Management/back_02_AccountSetting/Back_accountSearchModify.html',
                                         result=result,
                                         account=account,

                                         user_id=user_id,
                                         user_name=user_name,
                                         user_email=user_email,
                                         DateTime=formatted_time,

                                         registrationResult=registrationResult,
                                         systemResult=systemResult,
                                         basicResult=basicResult,
                                        
                                         exam_Registration=exam_Registration,
                                         agency_Registration=agency_Registration,
                                         system_accountAdd=system_accountAdd,
                                         system_accountModify=system_accountModify,
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

# ==============================帳號開啟設定==============================
@back_AccountSearchModify.route('/backaccountOpen',methods=['GET','POST'])
def backaccountOpen():
    current_time = importPackage.datetime.datetime.now()
    formatted_time = current_time.strftime("%Y/%m/%d")

    conn = pool.getconn()
    cursor = conn.cursor()

    account = str(importPackage.request.args.get('account'))

    if importPackage.request.method == 'POST':
        hiddenaccount = importPackage.request.form['hiddenaccount']
        hiddenaccountOpen = importPackage.request.form['hiddenaccountOpen']
        try:
            with conn.cursor() as cursor:
                cursor.execute(
                    """Update "back_AccountSetting" SET "accountStatus" = %s  WHERE "useraccount" = %s""", (hiddenaccountOpen,hiddenaccount))
                conn.commit()
        except Exception as e:
            result = None
            print('ErrorB')
        finally:
            cursor.close()
            pool.putconn(conn)
        return importPackage.redirect(importPackage.url_for('back_AccountSearchModify.backaccountOpen'))
    else:
        try:
            with conn.cursor() as cursor:
                cursor.execute(
                    """SELECT "useraccount", "username", "accountStatus","useripify" FROM "back_AccountSetting" """)
                result = cursor.fetchall()
        except Exception as e:
            result = None
            print('ErrorB')
        finally:
            cursor.close()
            pool.putconn(conn)
        return importPackage.render_template('後台網頁/back_03_System_Management/back_02_AccountSetting/back_accountSearch.html',
                                                     result=result,
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

# ==============================帳號關閉設定==============================
@back_AccountSearchModify.route('/backaccountClose',methods=['GET','POST'])
def backaccountClose():
    current_time = importPackage.datetime.datetime.now()
    formatted_time = current_time.strftime("%Y/%m/%d")

    conn = pool.getconn()
    cursor = conn.cursor()

    account = str(importPackage.request.args.get('account'))

    if importPackage.request.method == 'POST':
        hiddenaccount = importPackage.request.form['hiddenaccount']
        hiddenaccountClose = importPackage.request.form['hiddenaccountClose']
        try:
            with conn.cursor() as cursor:
                cursor.execute(
                    """Update "back_AccountSetting" SET "accountStatus" = %s  WHERE "useraccount" = %s""", (hiddenaccountClose,hiddenaccount))
                conn.commit()
        except Exception as e:
            result = None
            print('ErrorB')
        finally:
            cursor.close()
            pool.putconn(conn)
        return importPackage.redirect(importPackage.url_for('back_AccountSearchModify.backaccountClose'))
    else:
        try:
            with conn.cursor() as cursor:
                cursor.execute(
                    """SELECT "useraccount", "username", "accountStatus","useripify" FROM "back_AccountSetting" """)
                result = cursor.fetchall()
        except Exception as e:
            result = None
            print('ErrorB')
        finally:
            cursor.close()
            pool.putconn(conn)
        return importPackage.render_template('後台網頁/back_03_System_Management/back_02_AccountSetting/back_accountSearch.html',
                                                     result=result,
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