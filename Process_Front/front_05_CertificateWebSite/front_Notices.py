from publicUseFunction import importPackage, dbConnection
front_Notices = importPackage.Blueprint(
    'main_Notices', __name__)
front_Notices.secret_key = 'abc'


@front_Notices.route('/')
@front_Notices.route('/frontNotices')
def index():
    return importPackage.render_template('前台網頁/front_05_CertificateWebSite/front_Notices.html')
