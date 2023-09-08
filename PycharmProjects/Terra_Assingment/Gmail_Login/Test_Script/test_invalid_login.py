from POM.gmail_page import Gmail


def test_gmail_invalid(setup):
    # After Opening the Browser and enter the URL

    fp = Gmail(setup)

    # Checking element is visible on DOM
    fp.check_visible_gmail_page()
    assert fp.get_sign_in_text() == "Sign in", "Sign in Page is not Loaded"

    # Enter email in email text box
    email_id = 'sampleterra3@gmail.com'
    fp.enter_email(email_id)

    # Click on next button
    fp.click_next_button()

    # Checking correct email id
    assert fp.get_entered_email_text() == email_id, "Wrong Email Entered"

    # Enter Password in password text box
    fp.enter_password('SampleTerra3')

    # Click on Next button
    fp.click_next_button()

    # Get wrong password text
    wrong_password = fp.get_wrong_password_text()
    print(wrong_password)

