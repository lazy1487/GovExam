from publicUseFunction import importPackage, dbConnection
from Process_Front.front_01_MainWebsite.front_login import get_user
from Process_BackFunction.Process_BackFunctionSelect import select_backNewSetting
front_Index = importPackage.Blueprint('front_Index', __name__)
front_Index.secret_key = 'abc'

conn = importPackage.conn

pool = importPackage.psycopg2.pool.ThreadedConnectionPool(
    minconn=1, maxconn=999999999999, dsn=importPackage.DB_URI)


@front_Index.route('/')
@front_Index.route('/index')
def frontIndex():

    current_time = importPackage.datetime.datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d")
    try:
        with pool.getconn() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    """SELECT "inputTitle", "UploadTime" FROM "back_NewsSetting" Limit 5 """
                )
                result = cursor.fetchall()

                # 抓取維護啟動開關的value值
                cursor.execute(
                    """ SELECT "switchcarouselsetting","UpLoadTime","RemoveTime",
                               "maintainTitle","maintainEmail","maintainContext" FROM "back_EnvironmentSetting" """
                )
                switch = cursor.fetchall()
    except Exception as e:
        result = None
        switch = None
        print('Error:', e)

    finally:
        # 将返回连接到池中的代码放到 finally 块内
        if 'conn' in locals():
            pool.putconn(conn)

        if 'user_id' in importPackage.session:
            user = importPackage.session['user_id']
            return importPackage.render_template('前台網頁/front_01_MainWebsite/front_index.html', user=user, result=result, switch=switch, DateTime=formatted_time)
        else:
            return importPackage.render_template('前台網頁/front_01_MainWebsite/front_index.html', user=None, result=result, switch=switch, DateTime=formatted_time)


@front_Index.route('/logout')
def logout():
    if 'user_id' in importPackage.session:
        del importPackage.session['user_id']
    return importPackage.redirect(importPackage.url_for('front_Index.frontIndex'))
