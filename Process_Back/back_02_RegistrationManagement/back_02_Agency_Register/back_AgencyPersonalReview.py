from publicUseFunction import importPackage, dbConnection
back_AgencyPersonalReview = importPackage.Blueprint(
    'back_AgencyPersonalReview', __name__)
back_AgencyPersonalReview.secret_key = 'abc'


@back_AgencyPersonalReview.route('/backAgencyPersonalReview', methods=['GET', 'POST'])
def backExamRegister():
    return importPackage.render_template('後台網頁/back_02_Registration _Management/back_02_Agency_Register/back_AgencyPersonalReview.html')
