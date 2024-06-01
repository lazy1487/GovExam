from publicUseFunction import importPackage, dbConnection
front_FeedBack = importPackage.Blueprint(
    'main_FeedBack', __name__)
front_FeedBack.secret_key = 'abc'


@front_FeedBack.route('/')
@front_FeedBack.route('/frontFeedBack')
def index():
    return importPackage.render_template('前台網頁/front_01_MainWebSite/Front_Feedback.html')
