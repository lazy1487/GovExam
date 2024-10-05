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

        # 查詢資料庫檢查帳號是否存在
        cursor.execute("""SELECT * FROM "back_AccountSetting" WHERE useraccount = %s""",
                       (useraccount,))
        result = cursor.fetchone()

        # 判断账户是否存在以及密码是否正确
        if result is None:
            # 帳號不存在
            return importPackage.render_template(
                '後台網頁/back_01_MainWebSite/back_login.html',
                error="帳號不存在"
            )
        elif result[2] != password:
            # 密碼錯誤
            return importPackage.render_template(
                '後台網頁/back_01_MainWebSite/back_login.html',
                error="密碼錯誤"
            )
        else:
            PublicUseBackAccount = result[0]                 # 使用者帳號
            PublicUseBackName = result[1]                    # 使用者名稱
            PublicUseEmail = result[3]                       # 使用者電子信箱
            PublicUsePhone = result[4]                       # 使用者電子信箱
            Public_System_accountAdd = result[5]             # 系統管理模組-帳號新增
            Public_System_accountModify = result[6]          # 系統管理模組-帳號修改
            Public_System_passwordReset = result[7]          # 系統管理模組-密碼重設
            Public_System_Environment = result[8]            # 系統管理模組-系統環境設定
            Public_System_SMTPSetting = result[9]            # 系統管理模組-SMTP設定
            Public_System_SystemSearch = result[10]          # 系統管理模組-系統登入查詢
            Public_Basic_CarouselSetting = result[11]        # 基本管理模組-輪播圖維護
            Public_Basic_FastLinkSetting = result[12]        # 基本管理模組-快速連結維護
            Public_Basic_NewSetting = result[13]             # 基本管理模組-最新消息維護
            Public_Basic_NormalQuestionSetting = result[14]  # 基本管理模組-常見問題資訊維護
            Public_Basic_NoticeSetting = result[15]          # 基本管理模組-注意事項維護
            Public_Basic_PaymentSetting = result[16]         # 基本管理模組-付款提示維護
            Public_Basic_UnitImageSetting = result[17]       # 基本管理模組-單元形象維護
            Public_Exam_Registration = result[18]            # 報名管理模組-一般考生報名
            Public_Agency_Registration = result[19]          # 報名管理模組-薦送考生報名
            # 帳號啟用狀態(啟用/停用-Y/N)
            Public_AccountStatus = result[20]
            Public_LatestDate = result[21]                   # 最近登入時間
            UserIpify = result[22]                           # 使用者IP

            if Public_AccountStatus == 'Y':
                # 模擬讀取IP地址
                ipconfig = '114.44.0.28'
                cursor.execute(""" UPDATE "back_AccountSetting" SET "latestDate"=%s,"useripify"=%s
                                    WHERE "useraccount"= %s """, (formatted_time, ipconfig, PublicUseBackAccount))
                conn.commit()

                # =====存储用户信息到session====================================================
                importPackage.session['user_id'] = PublicUseBackAccount
                importPackage.session['user_name'] = PublicUseBackName
                importPackage.session['user_email'] = PublicUseEmail
                importPackage.session['user_Phone'] = PublicUsePhone
                importPackage.session['system_accountAdd'] = Public_System_accountAdd
                importPackage.session['system_accountModify'] = Public_System_accountModify
                importPackage.session['system_passwordReset'] = Public_System_passwordReset
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
                importPackage.session['exam_Registration'] = Public_Exam_Registration
                importPackage.session['agency_Registration'] = Public_Agency_Registration

                return importPackage.redirect(importPackage.url_for('index:8887.backindex'))
            else:

                return importPackage.render_template(
                    '後台網頁/back_01_MainWebSite/back_login.html',
                    error="帳號已停用"
                )
    else:
        # 如果请求方法为GET，渲染登录页面
        return importPackage.render_template('後台網頁/back_01_MainWebSite/back_login.html')
