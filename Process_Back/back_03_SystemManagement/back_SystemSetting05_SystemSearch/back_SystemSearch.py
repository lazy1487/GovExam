from publicUseFunction import importPackage, dbConnection
from datetime import datetime
back_SystemSearch = importPackage.Blueprint('back_SystemSearch', __name__)
conn = importPackage.conn

result = ''


@back_SystemSearch.route('/backSystemSearch', methods=['GET', 'POST'])
def backSystemSearch():
    global result

    hostname = importPackage.socket.gethostname()
    ip_address = importPackage.socket.gethostbyname(hostname)

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
        useraccount = importPackage.request.form['useraccount']
        userIP = importPackage.request.form['userIP']
        StartTime = importPackage.request.form['StartTime']
        EndTime = importPackage.request.form['EndTime']

        if StartTime != '':
            StartTime = importPackage.datetime.strptime(
                StartTime, "%Y-%m-%dT%H:%M")
            StartTime_formatted = StartTime.strftime("%Y-%m-%d %H:%M")
        else:
            StartTime = datetime.now()
            StartTime_formatted = StartTime.strftime("%Y-%m-%dT%H:%M")

        if EndTime != '':
            EndTime = importPackage.datetime.strptime(
                EndTime, "%Y-%m-%dT%H:%M")
            EndTime_formatted = EndTime.strftime("%Y-%m-%d %H:%M")
        else:
            EndTime = datetime.now()
            EndTime_formatted = EndTime.strftime("%Y-%m-%dT%H:%M")

        cursor = conn.cursor()
        if (useraccount == '') and (userIP == ''):
            query = """ SELECT "userAccount", "userIP", "LoginTime", "State"
                    FROM "back_SystemUsing" """
            cursor.execute(query)
            result = cursor.fetchall()
        else:
            query = """ SELECT "userAccount", "userIP", "LoginTime", "State"
                    FROM "back_SystemUsing"
                    WHERE ("userAccount" = %s) or ("userIP"=%s) or ("LoginTime" <= %s AND "LoginTime" >= %s) """
            cursor.execute(query, (useraccount, userIP, StartTime, EndTime))
            result = cursor.fetchall()

        return importPackage.render_template('後台網頁/back_03_System_Management/back_05_SystemSearch/Back_SystemSearch.html', result=result)
    return importPackage.render_template('後台網頁/back_03_System_Management/back_05_SystemSearch/Back_SystemSearch.html',user_id=user_id,
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


@back_SystemSearch.route('/backSystemSearchOutput')
def backSystemSearchOutput():
    global result
    result_json = importPackage.json.dumps(result)
    return result_json
