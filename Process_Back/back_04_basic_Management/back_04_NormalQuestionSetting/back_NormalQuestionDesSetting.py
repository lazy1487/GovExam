from publicUseFunction import importPackage, dbConnection
back_NormalQuestionDesSetting = importPackage.Blueprint(
    'back_NormalQuestionDesSetting', __name__)
conn = importPackage.conn


@back_NormalQuestionDesSetting.route('/backNormalQuestionDesSetting',methods=['GET','POST'])
def backNormalQuestionDesSetting():
    cursor = conn.cursor()
    
    cursor.execute(
        """ select "normalQuestionTitle" from "back_NormalQuestion" """)
    resultSearch = cursor.fetchall()

    cursor.execute(
        """ SELECT back_NormalQuestion."normalQuestionTitle",
            back_NormalDesQuestion."normalQuestionDesTitle" 
            FROM "back_NormalQuestion" AS back_NormalQuestion 
            LEFT JOIN "back_NormalDesQuestion" AS back_NormalDesQuestion 
            ON CAST(back_NormalQuestion."normalQuestionSort" AS VARCHAR) = back_NormalDesQuestion."normalQuestionCode"
            WHERE back_NormalDesQuestion."normalQuestionDesTitle" != '' """)
    
    result=cursor.fetchall()

    return importPackage.render_template('後台網頁/back_04_basic_Management/back_04_NormalQuestionSetting/back_NormalQuestionDesSetting.html', resultSearch=resultSearch,result=result)
