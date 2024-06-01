from publicUseFunction import importPackage, dbConnection
back_AgencyPersonalReviewAppend = importPackage.Blueprint(
    'back_AgencyPersonalReviewAppend', __name__)
back_AgencyPersonalReviewAppend.secret_key = 'abc'


@back_AgencyPersonalReviewAppend.route('/backAgencyPersonalReviewAppend', methods=['GET', 'POST'])
def backAgencyPersonalReviewAppend():

    user = importPackage.session.get('user_name')
    current_time = importPackage.datetime.datetime.now()
    formatted_time = current_time.strftime("%Y/%m/%d")


    return importPackage.render_template('後台網頁/back_02_Registration _Management/back_02_Agency_Register/back_AgencyPersonalReviewAppend.html',Handler=user,DateTime=formatted_time)
