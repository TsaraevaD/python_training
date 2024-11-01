from model.contact import Contact
from random import randrange

def test_delete(app):
    if app.contact.count() == 0:
        app.contact.add()
        app.contact.create(Contact(first_name="one", middle_name="", last_name=""))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_by_index(index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts

