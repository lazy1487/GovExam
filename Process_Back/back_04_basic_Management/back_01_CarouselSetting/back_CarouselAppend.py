from publicUseFunction import importPackage, dbConnection
back_CarouselAppend = importPackage.Blueprint('back_CarouselAppend', __name__)

pool = importPackage.psycopg2.pool.ThreadedConnectionPool(
    minconn=1, maxconn=10, dsn=importPackage.DB_URI)


@back_CarouselAppend.route('/backCarouselAppend', methods=['GET', 'POST'])
def backCarouselAppend():

    user = importPackage.session['user_id']
    current_time = importPackage.datetime.datetime.now()
    formatted_time = current_time.strftime("%Y/%m/%d")

    # 產生一個 UUID
    uuid_str = str(importPackage.uuid.uuid4().hex)[:32]
    importPackage.session['uuid_str'] = uuid_str
    conn = pool.getconn()
    # ===================================================================================================================================
    current_file_path = importPackage.os.path.abspath(__file__)
    dir_path = importPackage.os.path.dirname(current_file_path)                            # 使用 os.path.dirname() 獲取目錄路徑
    dir_path_parts = importPackage.os.path.normpath(dir_path).split(importPackage.os.sep)  # 使用 os.path.normpath 將路徑標準化，然後分割路徑
    try:
        process_back_index = dir_path_parts.index('Process_Back')
        # back_04_BasicManagement\back_01_CarouselSetting
        desired_path = importPackage.os.path.join(dir_path_parts[process_back_index + 1], dir_path_parts[process_back_index + 2]) 
        desired_path = "static\\後台網頁\\"+desired_path+"\\images\\"
        ProjectPath = importPackage.os.path.join(*dir_path_parts[1:6])                      # 組出專題檔案路徑
        importPackage.os.makedirs(desired_path, exist_ok=True)
    except ValueError:
        print("Path does not contain 'Process_Back'")

    # ===================================================================================================================================
    if importPackage.request.method == "POST":
        inputTitle = importPackage.request.form['inputTitle']
        imageDes = importPackage.request.form['imageDes']
        selected = importPackage.request.form['selected']
        inputURL = importPackage.request.form['inputURL']
        imageFile = importPackage.request.form['imageFile']
        phoneimageFile = importPackage.request.form['phoneimageFile']
        upLoadTime = importPackage.request.form['upLoadTime']
        RemoveTime = importPackage.request.form['RemoveTime']

        importPackage.os.chdir("C:/Users/lazy1/OneDrive/Desktop")
        # 獲取文件名
        imageFileName = importPackage.os.path.basename(imageFile)
        phoneimageFileName = importPackage.os.path.basename(phoneimageFile)

        # 構建完整的文件路徑
        imageFilePath = importPackage.os.path.join(desired_path)
        phoneimageFilePath = importPackage.os.path.join(desired_path)

        # 構建原始文件的完整路徑
        orgimageFilePath = importPackage.os.path.abspath(imageFileName)
        orgphoneimageFilePath = importPackage.os.path.abspath(phoneimageFileName)

        importPackage.os.makedirs(imageFilePath, exist_ok=True)
        importPackage.os.makedirs(phoneimageFilePath, exist_ok=True)

        # 複製檔案
        importPackage.shutil.copy(orgimageFilePath,"C:\\"+ProjectPath+"\\"+imageFilePath)
        importPackage.shutil.copy(orgphoneimageFilePath,"C:\\"+ProjectPath+"\\"+imageFilePath) 

        try:
            with conn.cursor() as cursor:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO "back_Carousel" ("title","imgDescript", "linkOpen","linkUrl",
                               "Carousel_compute", "Carousel_cellphone", "UploadTime", "RemovedTime","uuid32")
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                               (inputTitle, imageDes, selected, inputURL, desired_path+imageFileName, desired_path+phoneimageFileName, upLoadTime, RemoveTime, uuid_str))
                conn.commit()
                conn.close()
        except Exception as e:
            result = None
            print('Error')
        finally:
            cursor.close()
            pool.putconn(conn)
    return importPackage.render_template('後台網頁/back_04_basic_Management/back_01_CarouselSetting/back_CarouselAppend.html', Handler=user, DateTime=formatted_time)
