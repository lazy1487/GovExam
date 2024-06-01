from publicUseFunction import importPackage, dbConnection
from publicUseFunction.FunctionSelect.Functionselect import get_backendUser
backLogin = importPackage.Blueprint('/backendLogin:8888', __name__)
backLogin.secret_key = 'abc'
conn = importPackage.conn
cursor = conn.cursor()


@backLogin.route('/backendLogin', methods=['GET', 'POST'])
def backendlogin():
    current_time = importPackage.datetime.datetime.now()
    formatted_time = current_time.strftime("%Y/%m/%d-%H:%M:%S")

    if importPackage.request.method == "POST":
        useraccount = importPackage.request.form['backUser']
        password = importPackage.request.form['backPass']
        cursor.execute("""SELECT * FROM "back_AccountSetting" WHERE useraccount = %s AND password = %s""",
                       (useraccount, password))
        result = cursor.fetchone()
        if result:
            PublicUseBackAccount = result[0]                 # 使用者帳號
            PublicUseBackName = result[1]                    # 使用者名稱
            PublicUseEmail = result[3]                       # 使用者電子信箱
            Public_System_accountAdd = result[4]             # 系統管理模組-帳號新增
            Public_System_accountModify = result[5]          # 系統管理模組-帳號修改
            Public_System_Environment = result[6]            # 系統管理模組-系統環境設定
            Public_System_SMTPSetting = result[7]            # 系統管理模組-SMTP設定
            Public_System_SystemSearch = result[8]           # 系統管理模組-系統登入查詢
            Public_System_UserRecord = result[9]             # 該欄位目前不需使用等待移除
            Public_Basic_CarouselSetting = result[10]        # 基本管理模組-輪播圖維護
            Public_Basic_FastLinkSetting = result[11]        # 基本管理模組-快速連結維護
            Public_Basic_NewSetting = result[12]             # 基本管理模組-最新消息維護
            Public_Basic_NormalQuestionSetting = result[13]  # 基本管理模組-常見問題資訊維護
            Public_Basic_NoticeSetting = result[14]          # 基本管理模組-注意事項維護
            Public_Basic_PaymentSetting = result[15]         # 基本管理模組-付款提示維護
            Public_Basic_UnitImageSetting = result[16]       # 基本管理模組-單元形象維護          
            Public_AccountStatus = result[17]                # 帳號啟用狀態(啟用/停用-Y/N)
            Public_LatestDate = result[18]                   # 最近登入時間

            if Public_AccountStatus == 'Y':
                ipconfig = importPackage.requests.get("https://api.ipify.org")
                cursor.execute(""" UPDATE "back_AccountSetting" SET "latestDate"=%s,"useripify"=%s
                                    WHERE "useraccount"= %s """, (formatted_time, ipconfig.text, PublicUseBackAccount))
                conn.commit()
                importPackage.session['user_id'] = PublicUseBackAccount
                importPackage.session['user_name'] = PublicUseBackName
                importPackage.session['user_id'] = PublicUseBackAccount
                importPackage.session['user_name'] = PublicUseBackName
                importPackage.session['user_email'] = PublicUseEmail
                importPackage.session['system_accountAdd'] = Public_System_accountAdd
                importPackage.session['system_accountModify'] = Public_System_accountModify
                importPackage.session['system_Environment'] = Public_System_Environment
                importPackage.session['system_SMTPSetting'] = Public_System_SMTPSetting
                importPackage.session['system_SystemSearch'] = Public_System_SystemSearch
                importPackage.session['basic_CarouselSetting'] = Public_Basic_CarouselSetting
                importPackage.session['basic_FastLinkSetting'] = Public_Basic_FastLinkSetting
                importPackage.session['basic_NewSetting'] = Public_Basic_NewSetting
                importPackage.session['basic_NormalQuestionSetting'] = Public_Basic_NormalQuestionSetting
                importPackage.session['basic_NoticeSetting'] = Public_Basic_NoticeSetting
                importPackage.session['basic_PaymentSetting'] = Public_Basic_PaymentSetting
                importPackage.session['basic_UnitImageSetting'] = Public_Basic_UnitImageSetting
                return importPackage.redirect(importPackage.url_for('index:8887.backindex'))
            else:
                return importPackage.redirect(importPackage.url_for('/backendLogin:8888.backendlogin'))
        else:
            return importPackage.render_template('後台網頁/back_01_MainWebSite/back_login.html')
    return importPackage.render_template('後台網頁/back_01_MainWebSite/back_login.html')
