from publicUseFunction import importPackage

# 資料庫連線設定
db_config = {
    'host': '127.0.0.1',
    'user': 'postgres',
    'password': 'sam101554',
    'dbname': 'Python_FlaskProject03'
}

app = importPackage.Flask(__name__)
app.secret_key = 'abc'
