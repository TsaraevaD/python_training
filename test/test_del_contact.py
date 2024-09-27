from model.contact import Contact

def test_delete(app):
    if app.contact.count() == 0:
        app.contact.open()
        app.contact.create(Contact(first_name="one", middle_name="", last_name=""))
    app.contact.delete()
