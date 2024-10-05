from publicUseFunction import importPackage, dbConnection
back_CarouselAppend = importPackage.Blueprint('back_CarouselAppend', __name__)

pool = importPackage.psycopg2.pool.ThreadedConnectionPool(
    minconn=1, maxconn=999999999999, dsn=importPackage.DB_URI)


@back_CarouselAppend.route('/backCarouselAppend', methods=['GET', 'POST'])
def backCarouselAppend():

    current_time = importPackage.datetime.datetime.now()
    formatted_time = current_time.strftime("%Y/%m/%d")

    user = importPackage.session.get('user_id')
    user_name = importPackage.session.get('user_name')

    print(user_name)
    uuid_str = str(importPackage.uuid.uuid4().hex)[:32]
    importPackage.session['uuid_str'] = uuid_str

    conn = pool.getconn()

    if importPackage.request.method == "POST":
        hiddeninputTitle = importPackage.request.form['hiddeninputTitle']
        hiddenimageDes = importPackage.request.form['hiddenimageDes']
        hiddenselected = importPackage.request.form['hiddenselected']
        hiddeninputURL = importPackage.request.form['hiddeninputURL']
        hiddenimageFile = importPackage.request.form['hiddenimageFile']
        hiddenphoneimageFile = importPackage.request.form['hiddenphoneimageFile']
        hiddenupLoadTime = importPackage.request.form['hiddenupLoadTime']
        hiddenRemoveTime = importPackage.request.form['hiddenRemoveTime']

        hiddenimage_File = importPackage.os.path.basename(hiddenimageFile)
        hiddenphoneimage_File = importPackage.os.path.basename(
            hiddenphoneimageFile)

        current_file_path = importPackage.os.path.abspath(__file__)
        root_folder = 'FlaskPorject03'
        origin_Path = current_file_path.split(
            root_folder)[0] + root_folder + importPackage.os.sep

        current_directory = importPackage.os.path.dirname(current_file_path)
        root_folder = 'Process_Back'
        relative_path = current_directory.split(root_folder)[-1]
        desired_path = importPackage.os.path.join(
            relative_path.lstrip(importPackage.os.sep))
        desired_path = 'static\\後台網頁\\'+desired_path+'\\images'

        originalImagePath = 'allImages\\backEnd\\Carousel'

        fulloriginPath = origin_Path+originalImagePath+'\\'+hiddenimage_File
        fullCopyPath = origin_Path+desired_path+'\\'+hiddenimage_File

        fullphoneoriginPath = origin_Path+originalImagePath+'\\'+hiddenphoneimage_File
        fullphoneCopyPath = origin_Path+desired_path+'\\'+hiddenphoneimage_File

        importPackage.shutil.copy(fulloriginPath, fullCopyPath)
        importPackage.shutil.copy(fullphoneoriginPath, fullphoneCopyPath)
        try:
            with conn.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO "back_Carousel" ("title","imgDescript", "linkOpen","linkUrl",
                                "Carousel_compute", "Carousel_cellphone", "UploadTime", "RemovedTime","uuid32","switch")
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,%s)""",
                               (hiddeninputTitle, hiddenimageDes, hiddenselected, hiddeninputURL,
                                desired_path+'\\'+hiddenimage_File, desired_path+'\\'+hiddenphoneimage_File, hiddenupLoadTime, hiddenRemoveTime, uuid_str, 'Y'))
                conn.commit()
        except Exception as e:
            print('Error:', e)
            conn.rollback()
        finally:
            pool.putconn(conn)
        return importPackage.render_template('後台網頁/back_04_basic_Management/back_01_CarouselSetting/back_CarouselAppend.html', Handler=user, DateTime=formatted_time, user_name=user_name)

    return importPackage.render_template('後台網頁/back_04_basic_Management/back_01_CarouselSetting/back_CarouselAppend.html', Handler=user, DateTime=formatted_time, user_name=user_name)
