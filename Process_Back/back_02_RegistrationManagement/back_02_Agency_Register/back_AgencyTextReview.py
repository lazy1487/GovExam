from publicUseFunction import importPackage, dbConnection
back_AgencyTextReview = importPackage.Blueprint(
    'back_AgencyTextReview', __name__)
back_AgencyTextReview.secret_key = 'abc'


@back_AgencyTextReview.route('/backAgencyTextReview', methods=['GET', 'POST'])
def backAgencyTextReview():

    user = importPackage.session.get('user_name')
    current_time = importPackage.datetime.datetime.now()
    formatted_time = current_time.strftime("%Y/%m/%d")


    return importPackage.render_template('後台網頁/back_02_Registration _Management/back_02_Agency_Register/back_AgencyTextReview.html',Handler=user,DateTime=formatted_time)
