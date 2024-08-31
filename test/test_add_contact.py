from model.contact import Contact
    
def test_add_contact(app):
    app.open_home_page()
    app.session.login("admin", "secret")
    app.contact.open()
    app.contact.create(Contact("f-name", "mid-name", "l-name"))
    app.contact.return_to_home()
    app.session.logout()
