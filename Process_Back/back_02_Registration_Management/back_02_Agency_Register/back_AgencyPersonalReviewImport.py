from publicUseFunction import importPackage, dbConnection
back_AgencyPersonalReviewImport = importPackage.Blueprint(
    'back_AgencyPersonalReviewImport', __name__)
back_AgencyPersonalReviewImport.secret_key = 'abc'


@back_AgencyPersonalReviewImport.route('/backAgencyPersonalReviewImport', methods=['GET', 'POST'])
def backAgencyPersonalReviewImport():

    user_id = importPackage.session.get("user_id")
    user_name = importPackage.session.get("user_name")

    return importPackage.render_template('後台網頁/back_02_Registration_Management/back_02_Agency_Register/back_AgencyPersonalReviewImport.html',user_name=user_name)
