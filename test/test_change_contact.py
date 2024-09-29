from model.contact import Contact

def test_change(app):
    if app.contact.count() == 0:
        app.contact.add()
        app.contact.create(Contact(first_name="", middle_name="", last_name=""))
    app.contact.change(Contact("1-name", "2-name", "3-name"))