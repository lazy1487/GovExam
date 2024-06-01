from publicUseFunction import importPackage, dbConnection
back_AccountSetting = importPackage.Blueprint('back_AccountSetting', __name__)
back_AccountSetting.secret_key = 'abc'
conn = importPackage.conn


@back_AccountSetting.route('/backAccountSetting', methods=['GET', 'POST'])
def backAccountSetting():
    current_time = importPackage.datetime.datetime.now()
    formatted_time = current_time.strftime("%Y/%m/%d-%H:%M:%S")
    ipconfig = importPackage.requests.get("https://api.ipify.org")

    user_id = importPackage.session.get('user_id')
    user_name = importPackage.session.get('user_name')
    user_email = importPackage.session.get('user_email')
    system_accountAdd = importPackage.session.get('system_accountAdd')
    system_accountModify = importPackage.session.get('system_accountModify')
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
        ###################################################################
        useraccount = importPackage.request.form['useraccount']
        username = importPackage.request.form['username']
        password = importPackage.request.form['password']
        secondpassword = importPackage.request.form['secondpassword']
        email = importPackage.request.form['email']
        statusId = importPackage.request.form['statusId']
        if password == secondpassword:
            ###################################################################
            try:
                accountadd = bool(importPackage.request.form['accountadd'])
            except:
                accountadd = 'false'
            try:
                accountmodify = bool(
                    importPackage.request.form['accountmodify'])
            except:
                accountmodify = 'false'
            try:
                environmentsetting = bool(
                    importPackage.request.form['environmentsetting'])
            except:
                environmentsetting = 'false'
            try:
                smtpsetting = bool(importPackage.request.form['smtpsetting'])
            except:
                smtpsetting = 'false'
            try:
                systemsearch = bool(importPackage.request.form['systemsearch'])
            except:
                systemsearch = 'false'
            try:
                userecord = bool(importPackage.request.form['userecord'])
            except:
                userecord = 'false'
            ###################################################################
            try:
                carouselsetting = bool(
                    importPackage.request.form['carouselsetting'])
            except:
                carouselsetting = 'false'
            try:
                fastlinksetting = bool(
                    importPackage.request.form['fastlinksetting'])
            except:
                fastlinksetting = 'false'
            try:
                newsetting = bool(importPackage.request.form['newsetting'])
            except:
                newsetting = 'false'
            try:
                normalquestionsetting = bool(
                    importPackage.request.form['normalquestionsetting'])
            except:
                normalquestionsetting = 'false'
            try:
                noticesetting = bool(
                    importPackage.request.form['noticesetting'])
            except:
                noticesetting = 'false'

            try:
                paymentsetting = bool(
                    importPackage.request.form['paymentsetting'])
            except:
                paymentsetting = 'false'
            try:
                unitimagesetting = bool(
                    importPackage.request.form['unitimagesetting'])
            except:
                unitimagesetting = 'false'
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO "back_AccountSetting" (
                        "useraccount","username","password","email",
                        "accountadd","accountmodify","environmentsetting","smtpsetting","systemsearch","userecord",
                        "carouselsetting","fastlinksetting","newsetting","normalquestionsetting","noticesetting",
                        "paymentsetting","unitimagesetting","accountStatus","latestDate","useripify")
                VALUES (%s, %s, %s, %s,
                        %s, %s, %s, %s, %s, %s,
                        %s, %s, %s, %s, %s,%s, %s, %s, %s, %s)""",
                        (useraccount, username, password, email,
                         accountadd, accountmodify, environmentsetting, smtpsetting, systemsearch, userecord,
                         carouselsetting, fastlinksetting, newsetting, normalquestionsetting, noticesetting,
                         paymentsetting, unitimagesetting, statusId, formatted_time, ipconfig.text))
            conn.commit()
        return importPackage.render_template('後台網頁/back_03_System_Management/back_02_AccountSetting/back_accountSetting.html',
                                            user_id=user_id,
                                            user_name=user_name,
                                            user_email=user_email,
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
    else:
        return importPackage.render_template('後台網頁/back_03_System_Management/back_02_AccountSetting/back_accountSetting.html',
                                             user_id=user_id,
                                             user_name=user_name,
                                             user_email=user_email,
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
