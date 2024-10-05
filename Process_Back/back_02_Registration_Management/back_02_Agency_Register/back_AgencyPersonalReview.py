from publicUseFunction import importPackage, dbConnection
back_AgencyPersonalReview = importPackage.Blueprint(
    'back_AgencyPersonalReview', __name__)
back_AgencyPersonalReview.secret_key = 'abc'


@back_AgencyPersonalReview.route('/backAgencyPersonalReview', methods=['GET', 'POST'])
def backExamRegister():

    user_id = importPackage.session.get("user_id")
    user_name = importPackage.session.get("user_name")

    return importPackage.render_template('後台網頁/back_02_Registration_Management/back_02_Agency_Register/back_AgencyPersonalReview.html',user_name=user_name)
