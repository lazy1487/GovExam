from publicUseFunction import importPackage, dbConnection
from flask_mail import Mail, Message
from flask import Flask

back_SMTPSetting = importPackage.Blueprint('back_SMTPSetting', __name__)
mail = Mail()

back_SMTPSetting.config = {
    'MAIL_SERVER': 'smtp.gmail.com',
    'MAIL_PORT': 465,
    'MAIL_USERNAME': 'lazy1487@gmail.com',
    'MAIL_PASSWORD': 'iklwwrgprwlmzbna',
    'MAIL_USE_TLS': False,
    'MAIL_USE_SSL': True
}

pool = importPackage.psycopg2.pool.ThreadedConnectionPool(
    minconn=1, maxconn=999999999999, dsn=importPackage.DB_URI)


@back_SMTPSetting.route('/backSMTPSetting', methods=['GET', 'POST'])
def send_email():

    conn = pool.getconn()

    current_time = importPackage.datetime.datetime.now()
    formatted_time = current_time.strftime("%Y/%m/%d")

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

    if importPackage.request.method == "POST":
        senderEmail = importPackage.request.form['senderEmail']
        msg = Message('Hello', sender=senderEmail, recipients=[
                      'lazy1487@gmail.com', 'abnerhsu001@gmail.com'])
        msg.body = 'Hello Flask message sent From Flask-Email'
        mail.send(msg)
    return importPackage.render_template('後台網頁/back_03_System_Management/back_04_SMTPSetting/back_SMTPSetting.html',
                                         Handler=user_name,
                                         DateTime=formatted_time,
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
