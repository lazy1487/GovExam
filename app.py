from publicUseFunction import importPackage  # 導入套件、資料庫連線

from Process_Front.front_05_CertificateWebSite.front_Notices import front_Notices
from Process_Front.front_04_QuestionWebSite.front_NormalQuestions import front_NormalQuestions
from Process_Front.front_03_NewWebSite.front_News import front_News
from Process_Front.front_02_ExamWebSite.front_ExamRegistration import front_ExamRegistration
from Process_Front.front_01_MainWebsite.front_ForgerPassword import front_ForgetPassword
from Process_Front.front_01_MainWebsite.front_Collect import front_Collect
from Process_Front.front_01_MainWebsite.front_FeedBack import front_FeedBack
from Process_Front.front_01_MainWebsite.front_login import front_Login
from Process_Front.front_01_MainWebsite.front_Index import front_Index


# =====後台主要網頁==============================================================================================================================
from Process_Back.back_01_MainWebSite.back_login import backLogin
from Process_Back.back_01_MainWebSite.back_Index import backIndex
# =====後台主要網頁==============================================================================================================================

# =====報名管理模組==============================================================================================================================
# =====一般考生報名==================================================
from Process_Back.back_02_Registration_Management.back_01_ExamStudent_Register.back_ExamIndex import back_ExamIndex
from Process_Back.back_02_Registration_Management.back_01_ExamStudent_Register.back_ExamRegister import back_ExamRegister
from Process_Back.back_02_Registration_Management.back_01_ExamStudent_Register.back_ExamRegisterAppend import back_ExamRegisterAppend
from Process_Back.back_02_Registration_Management.back_01_ExamStudent_Register.back_ExamRegisterImport import back_ExamRegisterImport
from Process_Back.back_02_Registration_Management.back_01_ExamStudent_Register.back_ExamRegisterModify import back_ExamRegisterModify

from Process_Back.back_02_Registration_Management.back_01_ExamStudent_Register.back_ExamInfoAppend import back_ExamInfoAppend
from Process_Back.back_02_Registration_Management.back_01_ExamStudent_Register.back_ExamInfoModify import back_ExamInfoModify
from Process_Back.back_02_Registration_Management.back_01_ExamStudent_Register.back_ExamInfoSetting import back_ExamInfoSetting
from Process_Back.back_02_Registration_Management.back_01_ExamStudent_Register.back_ExamInfoSort import back_ExamInfoSort
from Process_Back.back_02_Registration_Management.back_01_ExamStudent_Register.back_ExamInfoImport import back_ExamInfoImport

from Process_Back.back_02_Registration_Management.back_01_ExamStudent_Register.back_ExamStyleSort import back_ExamStyleSort
from Process_Back.back_02_Registration_Management.back_01_ExamStudent_Register.back_ExamStyleSetting import back_ExamStyleSetting
from Process_Back.back_02_Registration_Management.back_01_ExamStudent_Register.back_ExamStyleAppend import back_ExamStyleAppend
from Process_Back.back_02_Registration_Management.back_01_ExamStudent_Register.back_ExamStyleModify import back_ExamStyleModify
from Process_Back.back_02_Registration_Management.back_01_ExamStudent_Register.back_ExamStyleImport import back_ExamStyleImport
# =====薦送考生報名==================================================
from Process_Back.back_02_Registration_Management.back_02_Agency_Register.back_AgencyPersonalReview import back_AgencyPersonalReview
from Process_Back.back_02_Registration_Management.back_02_Agency_Register.back_AgencyPersonalInfo import back_AgencyPersonalInfo
from Process_Back.back_02_Registration_Management.back_02_Agency_Register.back_AgencyPersonalInfoModify import back_AgencyPersonalInfoModify
from Process_Back.back_02_Registration_Management.back_02_Agency_Register.back_AgencyPersonalInfoAppend import back_AgencyPersonalInfoAppend
from Process_Back.back_02_Registration_Management.back_02_Agency_Register.back_AgencyPersonalInfoSub import back_AgencyPersonalInfoSub
from Process_Back.back_02_Registration_Management.back_02_Agency_Register.back_AgencyPersonalInfoImport import back_AgencyPersonalInfoImport

from Process_Back.back_02_Registration_Management.back_02_Agency_Register.back_AgencyInfo import back_AgencyInfo
from Process_Back.back_02_Registration_Management.back_02_Agency_Register.back_AgencyInfoIndex import back_AgencyInfoIndex
from Process_Back.back_02_Registration_Management.back_02_Agency_Register.back_AgencyInfoSub import back_AgencyInfoSub
from Process_Back.back_02_Registration_Management.back_02_Agency_Register.back_AgencyInfoAppend import back_AgencyInfoAppend
from Process_Back.back_02_Registration_Management.back_02_Agency_Register.back_AgencyInfoModify import back_AgencyInfoModify
from Process_Back.back_02_Registration_Management.back_02_Agency_Register.back_AgencyInfoImport import back_AgencyInfoImport

from Process_Back.back_02_Registration_Management.back_02_Agency_Register.back_AgencyTextReview import back_AgencyTextReview
from Process_Back.back_02_Registration_Management.back_02_Agency_Register.back_AgencyPersonalReviewImport import back_AgencyPersonalReviewImport
from Process_Back.back_02_Registration_Management.back_02_Agency_Register.back_AgencyPersonalReviewAppend import back_AgencyPersonalReviewAppend
# =====報名管理模組==============================================================================================================================

# =====系統管理模組==============================================================================================================================
# =====帳號權限設定==================================================
from Process_Back.back_03_SystemManagement.back_SystemSetting02_AccountSetting.back_accountSetting import back_AccountSetting
from Process_Back.back_03_SystemManagement.back_SystemSetting02_AccountSetting.back_accountSearch import back_AccountSearch
from Process_Back.back_03_SystemManagement.back_SystemSetting02_AccountSetting.back_accountSearchModify import back_AccountSearchModify
from Process_Back.back_03_SystemManagement.back_SystemSetting02_AccountSetting.back_accountSearchSub import back_AccountSearchSub
from Process_Back.back_03_SystemManagement.back_SystemSetting02_AccountSetting.back_accountImport import back_accountImport
from Process_Back.back_03_SystemManagement.back_SystemSetting02_AccountSetting.back_accountFunctionview import back_AccountFunctionView
# =====系統環境設定=====================================================
from Process_Back.back_03_SystemManagement.back_SystemSetting03_Environment.back_EnvironmentSetting import back_EnvironmentSetting
# =====SMTP設定========================================================
from Process_Back.back_03_SystemManagement.back_SystemSetting04_SMTPSetting.back_SMTPSetting import back_SMTPSetting
# =====系統查詢設定=====================================================
from Process_Back.back_03_SystemManagement.back_SystemSetting05_SystemSearch.back_SystemSearch import back_SystemSearch
# =====密碼重新設定=====================================================
from Process_Back.back_03_SystemManagement.back_SystemSetting02_AccountSetting.back_PersonalPasswordSetting import back_PersonalPasswordSetting
# =====系統管理模組==============================================================================================================================

# =====基本管理模組==============================================================================================================================
# =====輪播圖設定======================================================
from Process_Back.back_04_basic_Management.back_01_CarouselSetting.back_CarouselSort import back_CarouselSort
from Process_Back.back_04_basic_Management.back_01_CarouselSetting.back_CarouselModify import back_CarouselModify
from Process_Back.back_04_basic_Management.back_01_CarouselSetting.back_CarouselAppend import back_CarouselAppend
from Process_Back.back_04_basic_Management.back_01_CarouselSetting.back_CarouselSetting import back_CarouselSetting
from Process_Back.back_04_basic_Management.back_01_CarouselSetting.back_CarouselImageShow import back_CarouselImageShow
# =====快速連結設定====================================================
from Process_Back.back_04_basic_Management.back_02_FastLinkSetting.back_FastLinkModify import back_FastLinkModify
from Process_Back.back_04_basic_Management.back_02_FastLinkSetting.back_FastLinkSort import back_FastLinkSort
from Process_Back.back_04_basic_Management.back_02_FastLinkSetting.back_FastLinkSetting import back_fastLinkSetting
from Process_Back.back_04_basic_Management.back_02_FastLinkSetting.back_FastLinkImageShow import back_FastLinkImageShow
# =====最新消息設定====================================================
from Process_Back.back_04_basic_Management.back_03_NewSetting.back_NewsModify import back_NewsModify
from Process_Back.back_04_basic_Management.back_03_NewSetting.back_NewsAppend import back_NewsAppend
from Process_Back.back_04_basic_Management.back_03_NewSetting.back_NewsSetting import back_NewsSetting
# =====常見問題設定====================================================
from Process_Back.back_04_basic_Management.back_04_NormalQuestionSetting.back_NormalQuestionDataImport import back_NormalQuestionDataImport
from Process_Back.back_04_basic_Management.back_04_NormalQuestionSetting.back_NormalQuestionDesSort import back_NormalQuestionDesSort
from Process_Back.back_04_basic_Management.back_04_NormalQuestionSetting.back_NormalQuestionDesAppend import back_NormalQuestionDesAppend
from Process_Back.back_04_basic_Management.back_04_NormalQuestionSetting.back_NormalQuestionDesModify import back_NormalQuestionDesModify
from Process_Back.back_04_basic_Management.back_04_NormalQuestionSetting.back_NormalQuestionDesSub import back_NormalQuestionDesSub
from Process_Back.back_04_basic_Management.back_04_NormalQuestionSetting.back_NormalQuestionDesSetting import back_NormalQuestionDesSetting
from Process_Back.back_04_basic_Management.back_04_NormalQuestionSetting.back_NormalQuestionSort import back_NormalQuestionSort
from Process_Back.back_04_basic_Management.back_04_NormalQuestionSetting.back_NormalQuestionSetting import back_NormalQuestionSetting
from Process_Back.back_04_basic_Management.back_04_NormalQuestionSetting.back_NormalQuestionAppend import back_NormalQuestionAppend
from Process_Back.back_04_basic_Management.back_04_NormalQuestionSetting.back_NormalQuestionModify import back_NormalQuestionModify
from Process_Back.back_04_basic_Management.back_04_NormalQuestionSetting.back_NormalQuestionSub import back_NormalQuestionSub
# =====注意事項設定====================================================
from Process_Back.back_04_basic_Management.back_05_NoticeSetting.back_NoticeSort import back_NoticeSort
from Process_Back.back_04_basic_Management.back_05_NoticeSetting.back_NoticeModify import back_NoticeModify
from Process_Back.back_04_basic_Management.back_05_NoticeSetting.back_NoticeAppend import back_NoticeAppend
from Process_Back.back_04_basic_Management.back_05_NoticeSetting.back_NoticeSetting import back_NoticeSetting
from Process_Back.back_04_basic_Management.back_05_NoticeSetting.back_NoticeSub import back_NoticeSub
from Process_Back.back_04_basic_Management.back_05_NoticeSetting.back_NoticeStyleSetting import back_NoticeStyleSetting
from Process_Back.back_04_basic_Management.back_05_NoticeSetting.back_NoticeStyleAppend import back_NoticeStyleAppend
from Process_Back.back_04_basic_Management.back_05_NoticeSetting.back_NoticeStyleModify import back_NoticeStyleModify
from Process_Back.back_04_basic_Management.back_05_NoticeSetting.back_NoticeStyleSub import back_NoticeStyleSub
# =====付款提示設定==================================================
from Process_Back.back_04_basic_Management.back_06_PaymentSetting.back_PaymentSetting import back_PaymentSetting
# =====單元形象圖設定====================================================
from Process_Back.back_04_basic_Management.back_07_UnitImageSetting.back_UnitImageShow import back_UnitImageShow
from Process_Back.back_04_basic_Management.back_07_UnitImageSetting.back_UnitImageModify import back_UnitImageModify
from Process_Back.back_04_basic_Management.back_07_UnitImageSetting.back_UnitImage import back_UnitImage
# =====基本管理模組==============================================================================================================================
app = importPackage.Flask(__name__)
app.secret_key = 'abc'

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465  # 一般是587端口
app.config['MAIL_USERNAME'] = 'lazy1487@gmail.com'
app.config['MAIL_PASSWORD'] = 'iklwwrgprwlmzbna'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
# 初始化 Flask-Mail
mail = importPackage.Mail(app)

# =====前台所有設定==================================================================================================
# front_01_mainWebSite
# front_02_ExamWebSite
# front_03_NewWebSite
# front_04_QuestionWebSite
# front_05_CertificateWebSite

# from Process_Front.main_register import mainRegister

# =====前台所有設定==================================================================================================
# front_01_mainWebSite
app.register_blueprint(front_Index)
app.register_blueprint(front_Login)
app.register_blueprint(front_FeedBack)
app.register_blueprint(front_Collect)
app.register_blueprint(front_ForgetPassword)
# front_02_ExamWebSite
app.register_blueprint(front_ExamRegistration)
# front_03_NewWebSite
app.register_blueprint(front_News)
# front_04_QuestionWebSite
app.register_blueprint(front_NormalQuestions)
# front_05_CertificateWebSite
app.register_blueprint(front_Notices)

# =====後台主要網頁==============================================================================================================================
app.register_blueprint(backIndex)
app.register_blueprint(backLogin)
# =====後台主要網頁==============================================================================================================================

# =====報名管理模組==============================================================================================================================
# =====一般考生報名==================================================
app.register_blueprint(back_ExamRegister)
app.register_blueprint(back_ExamRegisterAppend)
app.register_blueprint(back_ExamRegisterImport)

app.register_blueprint(back_ExamStyleSetting)
app.register_blueprint(back_ExamStyleAppend)
app.register_blueprint(back_ExamStyleModify)
app.register_blueprint(back_ExamStyleSort)
app.register_blueprint(back_ExamStyleImport)

app.register_blueprint(back_ExamIndex)
app.register_blueprint(back_ExamInfoSetting)
app.register_blueprint(back_ExamInfoAppend)
app.register_blueprint(back_ExamInfoModify)
app.register_blueprint(back_ExamInfoSort)
app.register_blueprint(back_ExamInfoImport)
app.register_blueprint(back_ExamRegisterModify)
# =====薦送考生報名==================================================
app.register_blueprint(back_AgencyInfoIndex)
app.register_blueprint(back_AgencyInfo)
app.register_blueprint(back_AgencyInfoSub)
app.register_blueprint(back_AgencyInfoAppend)
app.register_blueprint(back_AgencyInfoModify)
app.register_blueprint(back_AgencyInfoImport)

app.register_blueprint(back_AgencyPersonalInfo)
app.register_blueprint(back_AgencyPersonalInfoSub)
app.register_blueprint(back_AgencyPersonalInfoModify)
app.register_blueprint(back_AgencyPersonalInfoAppend)
app.register_blueprint(back_AgencyPersonalInfoImport)

app.register_blueprint(back_AgencyPersonalReview)
app.register_blueprint(back_AgencyPersonalReviewAppend)
app.register_blueprint(back_AgencyPersonalReviewImport)
app.register_blueprint(back_AgencyTextReview)
# =====報名管理模組==============================================================================================================================

# =====系統管理模組==============================================================================================================================
# =====帳號權限設定==================================================
app.register_blueprint(back_AccountSetting)
app.register_blueprint(back_AccountSearch)
app.register_blueprint(back_AccountSearchSub)
app.register_blueprint(back_AccountSearchModify)
app.register_blueprint(back_AccountFunctionView)
app.register_blueprint(back_accountImport)
# =====系統環境設定=====================================================
app.register_blueprint(back_EnvironmentSetting)
# =====SMTP設定========================================================
app.register_blueprint(back_SMTPSetting)
# =====系統查詢設定=====================================================
app.register_blueprint(back_SystemSearch)
# =====密碼重新設定=====================================================
app.register_blueprint(back_PersonalPasswordSetting)
# =====系統管理模組==============================================================================================================================

# =====基本管理模組==============================================================================================================================
# =====輪播圖設定=====================================================
app.register_blueprint(back_CarouselSetting)
app.register_blueprint(back_CarouselAppend)
app.register_blueprint(back_CarouselModify)
app.register_blueprint(back_CarouselSort)
app.register_blueprint(back_CarouselImageShow)
# =====快速連結設定=====================================================
app.register_blueprint(back_fastLinkSetting)
app.register_blueprint(back_FastLinkSort)
app.register_blueprint(back_FastLinkModify)
app.register_blueprint(back_FastLinkImageShow)
# =====最新消息設定=====================================================
app.register_blueprint(back_NewsAppend)
app.register_blueprint(back_NewsSetting)
app.register_blueprint(back_NewsModify)
# =====常見問題設定=====================================================
app.register_blueprint(back_NormalQuestionSetting)
app.register_blueprint(back_NormalQuestionSort)
app.register_blueprint(back_NormalQuestionAppend)
app.register_blueprint(back_NormalQuestionModify)
app.register_blueprint(back_NormalQuestionSub)

app.register_blueprint(back_NormalQuestionDesSetting)
app.register_blueprint(back_NormalQuestionDesSort)
app.register_blueprint(back_NormalQuestionDesAppend)
app.register_blueprint(back_NormalQuestionDesModify)
app.register_blueprint(back_NormalQuestionDesSub)
app.register_blueprint(back_NormalQuestionDataImport)
# =====注意事項設定=====================================================
app.register_blueprint(back_NoticeSetting)
app.register_blueprint(back_NoticeAppend)
app.register_blueprint(back_NoticeModify)
app.register_blueprint(back_NoticeSub)

app.register_blueprint(back_NoticeSort)
app.register_blueprint(back_NoticeStyleSetting)
app.register_blueprint(back_NoticeStyleAppend)
app.register_blueprint(back_NoticeStyleModify)
app.register_blueprint(back_NoticeStyleSub)
# =====付款提示設定=====================================================
app.register_blueprint(back_PaymentSetting)
# =====單元形象設定=====================================================
app.register_blueprint(back_UnitImage)
app.register_blueprint(back_UnitImageModify)
app.register_blueprint(back_UnitImageShow)
# =====基本管理模組==============================================================================================================================
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)
