from model.contact import Contact

def test_delete(app):
    if app.contact.count() == 0:
        app.contact.add()
        app.contact.create(Contact(first_name="one", middle_name="", last_name=""))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts

