from publicUseFunction import importPackage, dbConnection
back_AccountSetting = importPackage.Blueprint('back_AccountSetting', __name__)
back_AccountSetting.secret_key = 'abc'

pool = importPackage.psycopg2.pool.ThreadedConnectionPool(
    minconn=1, maxconn=999999999999, dsn=importPackage.DB_URI)


@back_AccountSetting.route('/backAccountSetting', methods=['GET', 'POST'])
def backAccountSetting():
    current_time = importPackage.datetime.datetime.now()
    formatted_time = current_time.strftime("%Y/%m/%d-%H:%M:%S")
    ipconfig = importPackage.requests.get("https://api.ipify.org")

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
    basic_NormalQuestionSetting = importPackage.session.get('basic_NormalQuestionSetting')
    basic_NoticeSetting = importPackage.session.get('basic_NoticeSetting')
    basic_PaymentSetting = importPackage.session.get('basic_PaymentSetting')
    basic_UnitImageSetting = importPackage.session.get('basic_UnitImageSetting')

    if importPackage.request.method == "POST":
       # ====================使用者註冊資料===================
        useraccount = importPackage.request.form['useraccount']
        username = importPackage.request.form['username']
        password = importPackage.request.form['password']
        secondpassword = importPackage.request.form['secondpassword']
        email = importPackage.request.form['email']
        phone = importPackage.request.form['phone']
        statusId = importPackage.request.form['statusId']
        # ====================報名管理模組================== ==
        hiddenExamRegistration = importPackage.request.form['Exam_Registration']
        hiddenAgencyRegistration = importPackage.request.form['Agency_Registration']
        # ====================系統管理模組====================
        hiddenaccountadd = importPackage.request.form['system_accountadd']
        hiddenaccountmodify = importPackage.request.form['system_accountmodify']
        hiddenpasswordReset = importPackage.request.form['system_passwordReset']
        hiddenenvironmentsetting = importPackage.request.form['system_environmentsetting']
        hiddensmtpsetting = importPackage.request.form['system_smtpsetting']
        hiddensystemsearch = importPackage.request.form['system_systemsearch']
        # # ====================基本管理模組====================
        hiddencarouselsetting = importPackage.request.form['basic_carouselsetting']
        hiddenfastlinksetting = importPackage.request.form['basic_fastlinksetting']
        hiddennewsetting = importPackage.request.form['basic_newsetting']
        hiddennormalquestionsetting = importPackage.request.form['basic_normalquestionsetting']
        hiddennoticesetting = importPackage.request.form['basic_noticesetting']
        hiddenpaymentsetting = importPackage.request.form['basic_paymentsetting']
        hiddenunitimagesetting = importPackage.request.form['basic_unitimagesetting']
        # ###################################################################
        try:
            with conn.cursor() as cursor:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO "back_AccountSetting" (
                            "useraccount","username","password","email","Phone",
                            "accountadd","accountmodify","passwordReset",
                            "environmentsetting","smtpsetting","systemsearch",
                            "carouselsetting","fastlinksetting","newsetting","normalquestionsetting","noticesetting",
                            "paymentsetting","unitimagesetting",
                            "ExamRegistration","AgencyRegistration","accountStatus","latestDate","useripify")
                    VALUES (%s, %s, %s, %s, %s,
                            %s, %s, %s,
                            %s, %s, %s,
                            %s, %s, %s, %s, %s,
                            %s, %s,
                            %s, %s, %s, %s, %s)""",
                               (useraccount, username, password, email, phone,
                                hiddenaccountadd, hiddenaccountmodify, hiddenpasswordReset,
                                hiddenenvironmentsetting, hiddensmtpsetting, hiddensystemsearch,
                                hiddencarouselsetting, hiddenfastlinksetting, hiddennewsetting, hiddennormalquestionsetting, hiddennoticesetting,
                                hiddenpaymentsetting, hiddenunitimagesetting,
                                hiddenExamRegistration, hiddenAgencyRegistration, statusId, formatted_time, ipconfig.text))
            conn.commit()
        except Exception as e:
            result = None
            print('Errora')
        finally:
            # cursor.close()
            pool.putconn(conn)
        return importPackage.render_template('後台網頁/back_03_System_Management/back_02_AccountSetting/back_accountSetting.html',
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
    else:
        return importPackage.render_template('後台網頁/back_03_System_Management/back_02_AccountSetting/back_accountSetting.html',
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
