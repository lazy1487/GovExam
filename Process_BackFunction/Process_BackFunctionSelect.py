from publicUseFunction import importPackage, dbConnection
db_config = dbConnection.db_config

def select_backNewSetting():
    conn = importPackage.psycopg2.connect(**db_config)
    cur = conn.cursor()
    cur.execute("select * from backnewappend")
    backNewSetting=cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return backNewSetting