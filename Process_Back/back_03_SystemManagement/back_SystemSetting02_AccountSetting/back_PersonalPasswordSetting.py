from publicUseFunction import importPackage, dbConnection
back_PersonalPasswordSetting = importPackage.Blueprint(
    'back_PersonalPasswordSetting', __name__)
back_PersonalPasswordSetting.secret_key = 'abc'
conn = importPackage.conn


@back_PersonalPasswordSetting.route('/backPersonalPasswordSetting', methods=['GET', 'POST'])
def backPersonalPasswordSetting():
    PublicUseBackAccount = importPackage.session.get('user_id')
    PublicUseBackName = importPackage.session.get('user_name')

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
        email = importPackage.request.form['email']
        newPassword = importPackage.request.form['newPassword']
        cursor = conn.cursor()
        cursor.execute(
            """ select "useraccount","username","password"
            from "back_AccountSetting" where "useraccount"= %s and "email"= %s """, (PublicUseBackAccount, email))
        result = cursor.fetchone()
        if (result and (result[1] != result[2])):
            cursor = conn.cursor()
            cursor.execute(""" UPDATE "back_AccountSetting" SET 
                           "password" = %s WHERE useraccount = %s """, (newPassword, PublicUseBackAccount))
            conn.commit()
        return importPackage.render_template('後台網頁/back_03_System_Management/back_02_AccountSetting/Back_PersonalPassWordSetting.html', result=result,
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
    return importPackage.render_template('後台網頁/back_03_System_Management/back_02_AccountSetting/back_PersonalPassWordSetting.html', username=PublicUseBackName)
