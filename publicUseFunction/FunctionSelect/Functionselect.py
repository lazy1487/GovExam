from publicUseFunction import importPackage, dbConnection
db_config = dbConnection.db_config


def get_user(username, password):
    conn = importPackage.psycopg2.connect(**db_config)
    cur = conn.cursor()
    # 从数据库中获取用户数据
    cur.execute(
        "SELECT * FROM account WHERE username = %s AND password = %s", (username, password))
    user = cur.fetchone()
    cur.close()
    conn.close()
    return user


def get_backendUser(useraccount, password):
    conn = importPackage.psycopg2.connect(**db_config)
    cur = conn.cursor()
    cur.execute("""SELECT * FROM "back_AccountSetting" WHERE useraccount = %s AND password = %s""",
                (useraccount, password))
    backendUser = cur.fetchone()
    cur.close()
    conn.close()
    return backendUser
