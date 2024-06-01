from publicUseFunction import importPackage, dbConnection
backIndex = importPackage.Blueprint('index:8887', __name__)
backIndex.secret_key = 'abc'


@backIndex.route('/index:8887')
def backindex():
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
    basic_NormalQuestionSetting = importPackage.session.get(
        'basic_NormalQuestionSetting')
    basic_NoticeSetting = importPackage.session.get('basic_NoticeSetting')
    basic_PaymentSetting = importPackage.session.get('basic_PaymentSetting')
    basic_UnitImageSetting = importPackage.session.get(
        'basic_UnitImageSetting')
    return importPackage.render_template('後台網頁/back_01_MainWebSite/back_index.html',
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
@backIndex.route('/backlogut')
def backlogout():
    importPackage.session.pop('username', None)
    return importPackage.redirect('/backendLogin')
