from publicUseFunction import importPackage, dbConnection
back_accountImport = importPackage.Blueprint('back_accountImport', __name__)
back_accountImport.secret_key = 'abc'

pool = importPackage.psycopg2.pool.ThreadedConnectionPool(
    minconn=1, maxconn=999999999999, dsn=importPackage.DB_URI)


@back_accountImport.route('/backAccountImport', methods=['GET', 'POST'])
def backAccountImport():

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

    return importPackage.render_template('後台網頁/back_03_System_Management/back_02_AccountSetting/back_accountImport.html',
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