from publicUseFunction import importPackage, dbConnection
back_ExamInfoAppend = importPackage.Blueprint(
    'back_ExamInfoAppend', __name__)
back_ExamInfoAppend.secret_key = 'abc'

pool = importPackage.psycopg2.pool.ThreadedConnectionPool(
    minconn=1, maxconn=10, dsn=importPackage.DB_URI)


@back_ExamInfoAppend.route('/backExamInfoAppend', methods=['GET', 'POST'])
def backExamRegister():
    conn = pool.getconn()

    # 產生使用者相關資訊
    user = importPackage.session.get('user_name')
    current_time = importPackage.datetime.datetime.now()
    formatted_time = current_time.strftime("%Y/%m/%d")

    # 產生UUID
    generated_uuid = importPackage.uuid.uuid4().hex

    if importPackage.request.method == "POST":
        # ========== 所屬類別、標題、顯示於前台、開放報名、梯次、級別 ==========
        hiddeninputExamStyleID = importPackage.request.form['hiddeninputExamStyleID']
        hiddeninputExamTitle = importPackage.request.form['hiddeninputExamTitle']
        hiddenshowdesk = importPackage.request.form['hiddenshowdesk']
        hiddenopenRegister = importPackage.request.form['hiddenopenRegister']
        hiddenladder = importPackage.request.form['hiddenladder']
        hiddenlevel = importPackage.request.form['hiddenlevel']
        # ========== 北部地區、中部地區、南部地區、東部地區、離島地區 ==========
        hiddenregisterCount_N = importPackage.request.form['hiddenregisterCount_N']
        hiddenregisterCount_C = importPackage.request.form['hiddenregisterCount_C']
        hiddenregisterCount_S = importPackage.request.form['hiddenregisterCount_S']
        hiddenregisterCount_E = importPackage.request.form['hiddenregisterCount_E']
        hiddenregisterCount_I = importPackage.request.form['hiddenregisterCount_I']
        # ========== 一般考生費用、薦送考生費用、年齡限制 ==========
        hiddengeneralPayment = importPackage.request.form['hiddengeneralPayment']
        hiddenagencyPayment = importPackage.request.form['hiddenagencyPayment']
        hiddenageLimit = importPackage.request.form['hiddenageLimit']
        # ========== 考試資訊內文、報名填寫內文、考試日期 ==========
        hiddenexamInfoContent = importPackage.request.form['hiddenexamInfoContent']
        hiddenregisterContent = importPackage.request.form['hiddenregisterContent']
        hiddenexamDate = importPackage.request.form['hiddenexamDate']
        # ========== 文章上架時間、文章下架時間 ==========
        hiddenarticleUpdateTime = importPackage.request.form['hiddenarticleUpdateTime']
        hiddenarticleRemoveTime = importPackage.request.form['hiddenarticleRemoveTime']
        # ========== 一般報名開始日期、一般報名結束日期 ==========
        hiddenexamRegistrationStartDate = importPackage.request.form['hiddenexamRegistrationStartDate']
        hiddenexamRegistrationEndDate = importPackage.request.form['hiddenexamRegistrationEndDate']
        # ========== 機關報名開始日期、機關報名結束日期 ==========
        hiddenagencyRegistrationStartDate = importPackage.request.form['hiddenagencyRegistrationStartDate']
        hiddenagencyRegistrationEndDate = importPackage.request.form['hiddenagencyRegistrationEndDate']
        # ========== 一般報名繳費開始日期、一般報名繳費結束日期 ==========
        hiddenexamPaymentStartDate = importPackage.request.form['hiddenexamPaymentStartDate']
        hiddenexamPaymentEndDate = importPackage.request.form['hiddenexamPaymentEndDate']
        # ========== 薦送報名繳費開始日期、薦送報名繳費結束日期 ==========
        hiddenagencyPaymentStartDate = importPackage.request.form['hiddenagencyPaymentStartDate']
        hiddenagencyPaymentEndDate = importPackage.request.form['hiddenagencyPaymentEndDate']
        # ========== 考試通知單下載起始日期、考試通知單下載結束日期 ==========
        hiddenexamNoticeDownloadStartDate = importPackage.request.form['hiddenexamNoticeDownloadStartDate']
        hiddenexamNoticeDownloadEndDate = importPackage.request.form['hiddenexamNoticeDownloadEndDate']
        # ========== 成績查詢起始日期、成績查詢結束日期 ==========
        hiddenscoreSearchStartDate = importPackage.request.form['hiddenscoreSearchStartDate']
        hiddenscoreSearchEndDate = importPackage.request.form['hiddenscoreSearchEndDate']
        # ========== 證書下載起始日期、證書下載結束日期 ==========
        hiddencertificateDownloadStartDate = importPackage.request.form['hiddencertificateDownloadStartDate']
        hiddencertificateDownloadEndDate = importPackage.request.form['hiddencertificateDownloadEndDate']
        cursor = conn.cursor()
        cursor.execute(
            """ INSERT INTO "back_ExamSetting" 
                ("inputExamStyleID","inputExamTitle","showdesk","openRegister","ladder","level",
                "registerCount_N","registerCount_C","registerCount_S","registerCount_E","registerCount_I",
                "registerCount_AN","registerCount_AC","registerCount_AS","registerCount_AE","registerCount_AI",
                "generalPayment","agencyPayment","ageLimit",
                "examInfoContent","regiserContent","examDate",
                "articleUpdateTime","articleRemoveTime","agencyRegistrationStartDate","agencyRegistrationEndDate",
                "examRegistrationStartDate","examRegistrationEndDate","examPaymentStartDate","examPaymentEndDate",
                "agencyPaymentStartDate","agencyPaymentEndDate","examNoticeDownloadStartDate","examNoticeDownloadEndDate",
                "scoreSearchStartDate","scoreSearchEndDate","certificateDownloadStartDate","certificateDownloadEndDate","examUUID")
                VALUES (%s,%s,%s,%s,%s,%s,
                        %s,%s,%s,%s,%s,
                        %s,%s,%s,%s,%s,
                        %s,%s,%s,
                        %s,%s,%s,
                        %s,%s,%s,%s,
                        %s,%s,%s,%s,
                        %s,%s,%s,%s,
                        %s,%s,%s,%s,%s) """, 
                (hiddeninputExamStyleID, hiddeninputExamTitle, hiddenshowdesk, hiddenopenRegister, hiddenladder, hiddenlevel,
                 hiddenregisterCount_N,hiddenregisterCount_C,hiddenregisterCount_S,hiddenregisterCount_E,hiddenregisterCount_I,
                 0,0,0,0,0,
                 hiddengeneralPayment,hiddenagencyPayment,hiddenageLimit,
                 hiddenexamInfoContent,hiddenregisterContent,hiddenexamDate,
                 hiddenarticleUpdateTime,hiddenarticleRemoveTime,hiddenagencyRegistrationStartDate,hiddenagencyRegistrationEndDate,
                 hiddenexamRegistrationStartDate,hiddenexamRegistrationEndDate,hiddenexamPaymentStartDate,hiddenexamPaymentEndDate,
                 hiddenagencyPaymentStartDate,hiddenagencyPaymentEndDate,hiddenexamNoticeDownloadStartDate,hiddenexamNoticeDownloadEndDate,
                 hiddenscoreSearchStartDate,hiddenscoreSearchEndDate,hiddencertificateDownloadStartDate,hiddencertificateDownloadEndDate,generated_uuid
                 ))
        conn.commit()
        conn.close()
        return importPackage.render_template('後台網頁/back_02_Registration_Management/back_01_ExamStudent_Register/back_ExamInfoSetting.html')
    else:
        try:
            cursor = conn.cursor()
            cursor.execute(
                """ Select "inputExamStyleID","inputExamStyle" from "back_ExamStyleSetting" """)
            result = cursor.fetchall()
        except Exception as e:
            result = None
            print('Error')
        finally:
            cursor.close()
            pool.putconn(conn)

        return importPackage.render_template('後台網頁/back_02_Registration_Management/back_01_ExamStudent_Register/back_ExamInfoAppend.html', result=result,Handler=user,DateTime=formatted_time)
