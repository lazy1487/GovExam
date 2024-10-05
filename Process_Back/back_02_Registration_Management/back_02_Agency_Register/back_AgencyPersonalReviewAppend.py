from publicUseFunction import importPackage, dbConnection
back_AgencyPersonalReviewAppend = importPackage.Blueprint(
    'back_AgencyPersonalReviewAppend', __name__)
back_AgencyPersonalReviewAppend.secret_key = 'abc'


@back_AgencyPersonalReviewAppend.route('/backAgencyPersonalReviewAppend', methods=['GET', 'POST'])
def backAgencyPersonalReviewAppend():
    
    current_time = importPackage.datetime.datetime.now()
    formatted_time = current_time.strftime("%Y/%m/%d")

    user_id = importPackage.session.get('user_id')
    user_name = importPackage.session.get('user_name')

    return importPackage.render_template('後台網頁/back_02_Registration_Management/back_02_Agency_Register/back_AgencyPersonalReviewAppend.html',user_name=user_name,DateTime=formatted_time)
