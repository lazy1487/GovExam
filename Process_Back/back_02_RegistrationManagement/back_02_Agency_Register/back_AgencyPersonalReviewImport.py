from publicUseFunction import importPackage, dbConnection
back_AgencyPersonalReviewImport = importPackage.Blueprint(
    'back_AgencyPersonalReviewImport', __name__)
back_AgencyPersonalReviewImport.secret_key = 'abc'


@back_AgencyPersonalReviewImport.route('/backAgencyPersonalReviewImport', methods=['GET', 'POST'])
def backAgencyPersonalReviewImport():
    return importPackage.render_template('後台網頁/back_02_Registration _Management/back_02_Agency_Register/back_AgencyPersonalReviewImport.html')
