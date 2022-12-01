class SIGN_IN_PAGE:

    # Email
    email = "//input[contains(@placeholder,'Email')]" ### Works Lakewood and IEWC
    #email_1 = "//input[contains(@placeholder,'mail')]" ### Works for Joel Osteen
    email_1 = "//input[@id='f01d2165158b494d8ef50b9983207dfc_EmailAddress']"
    password = "//input[contains(@placeholder,'assword')]"
    signin_btn = "//button[contains(text(),'Sign In')]" ## Works for Lakewood and IEWC


    modal = "//div[contains(@class,'modal-content')]" ## Works for Joel Osteen
    error_sign_in = "//*[contains(text(),'Error')]"
    error_sign_in_1 = "//*[contains(text(),'Invalid Email')]" ### Works on IEWC


    create_account_link = "//a[contains(text(),'Create Account')]" ## Works on IEWC

    cookiebot = "//a[contains(text(),'Accept')]"
    user_inf = "//h1[contains(text(),'Create Account')]"
