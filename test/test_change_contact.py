from model.contact import Contact
import random

def test_change(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.add()
        app.contact.create(Contact(firstname="Di", middlename="", lastname="Ts"))
    old_contacts = db.get_contact_list()
    contact = Contact("1-name", "2-name", "3-name")
    contact.id = random.choice(old_contacts).id
    app.contact.change_by_id(contact.id, contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    contact.id = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)