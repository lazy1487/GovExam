from publicUseFunction import importPackage, dbConnection
back_NormalQuestionSetting = importPackage.Blueprint(
    'back_NormalQuestionSetting', __name__)
conn = importPackage.conn


@back_NormalQuestionSetting.route('/backNormalQuestionSetting', methods=['GET', 'POST'])
def backNormalQuestionSetting():

    cursor = conn.cursor()

    user_id = importPackage.session.get('user_id')
    user_name = importPackage.session.get('user_name')

    normalQuestionTitle = ''
    if importPackage.request.method == 'POST':
        normalQuestionTitle = importPackage.request.form['normalQuestionTitle']
        if normalQuestionTitle != "":
            cursor.execute(""" insert into "back_NormalQuestion"("normalQuestionTitle","normalQuestionIsUsed")
                            values(%s,%s) """, (normalQuestionTitle, 'F'))
            conn.commit()

    cursor.execute(
        """ select "normalQuestionCode","normalQuestionTitle","normalQuestionIsUsed" from "back_NormalQuestion" """)
    result = cursor.fetchall()
    return importPackage.render_template('後台網頁/back_04_basic_Management/back_04_NormalQuestionSetting/back_NormalQusetionSetting.html', result=result, user_name=user_name)


@back_NormalQuestionSetting.route('/backNormalQuestionSettingDelete', methods=['GET', 'POST'])
def backNormalQuestionSettingDelete():
    if importPackage.request.method == "POST":
        normalQuestionTitle = importPackage.request.form['hiddennormalQuestionTitle']
    return importPackage.redirect(importPackage.url_for('back_NormalQuestionSetting.backNormalQuestionSetting'))
