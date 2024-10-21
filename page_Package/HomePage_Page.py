class HomePage:

    def __init__(self, page):
        self.page = page

        self.Sign_In_Button = page.get_by_role("link", name="Sign In")
        self.Email_Field = page.get_by_label("Email")
        self.Password_Field = page.get_by_label("Password")
        self.Submit_Login_Details_Field = page.get_by_role("button", name="Submit")
        self.Login_Validation_Element = page.get_by_role("heading", name="Courses", exact=True)


    def SignIn(self,Enter_email,Enter_Password):
        self.Sign_In_Button.click()
        self.Email_Field.fill(Enter_email)
        self.Password_Field.fill(Enter_Password)
        self.Submit_Login_Details_Field.click()





