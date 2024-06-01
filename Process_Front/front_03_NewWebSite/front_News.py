from publicUseFunction import importPackage, dbConnection
front_News = importPackage.Blueprint(
    'front_News', __name__)
front_News.secret_key = 'abc'
conn = importPackage.conn

@front_News.route('/frontNews')
def index():
    cursor = conn.cursor()
    cursor.execute(""" select "inputTitle" from "back_NewsSetting" """)
    result = cursor.fetchall()
    return importPackage.render_template('前台網頁/front_03_NewWebSite/front_News.html',result=result)
