from model.contact import Contact
    
def test_add_contact(app):
    app.contact.add()
    app.contact.create(Contact("f-name", "mid-name", "l-name"))
    app.contact.return_to_home()
