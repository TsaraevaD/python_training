from model.contact import Contact

def test_change(app):
    app.contact.change(Contact("1-name", "2-name", "3-name"))