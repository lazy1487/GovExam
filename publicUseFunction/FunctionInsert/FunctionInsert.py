from publicUseFunction import importPackage, dbConnection
db_config = dbConnection.db_config


def create_user(email, username, password):
    conn = importPackage.psycopg2.connect(**db_config)
    cur = conn.cursor()
    # 插入用户数据到数据库
    cur.execute("INSERT INTO account (email, username, password) VALUES (%s, %s, %s)",(email, username, password))
    conn.commit()
    cur.close()
    conn.close()
