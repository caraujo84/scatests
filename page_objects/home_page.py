class Home_Page:

    # Logo
    logo_a = "//img[contains(@src,'logo')]" ## Temp Comment: Works with Lakewood, IEWC, Joel Osteen
    logo_b = "//a[contains(@class,'logo')]" ## Works for Verndale

    # Sign In
    sign_in = "//a[contains(text(),'Sign In')]" ## Lakewood
    login = "//a[contains(text(),'LOGIN')]" ## Works Joel Osteen
    signin = "//a[contains(@class,'sign-in')]" ## Works IEWC


    # Copyright
    copy = "//*[contains(text(),'©')]"

    # Footer
    FAQ = "//*[contains(text(),'FAQ')]"
    terms = "//*[contains(text(),'Terms & Conditions')]"
    privacy = "//*[contains(text(),'Privacy Policy')]"
    contact = "//*[contains(text(),'Contact Us')]"
