from model.contact import Contact

def test_change(app):
    if app.contact.count() == 0:
        app.contact.add()
        app.contact.create(Contact(first_name="", middle_name="", last_name=""))
    old_contacts = app.contact.get_contact_list()
    contact = Contact("1-name", "2-name", "3-name")
    contact.id = old_contacts[0].id
    app.contact.change(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)