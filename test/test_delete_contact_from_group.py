from model.contact import Contact
import random
from fixture.orm import ORMFixture
from model.group import Group

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_delete_contact(app):
    if len(db.get_contact_list()) == 0:
        app.contact.add()
        app.contact.create(Contact(firstname="one", middlename="", lastname=""))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    contacts = app.contact.get_contact_list()
    contact = random.choice(contacts)
    groups = app.group.get_group_list()
    group = random.choice(groups)
    old = db.get_contacts_not_in_group(group)
    if contact in old:
        app.contact.add_to_group(contact.id, group.id)
    app.contact.delete_from_group(contact.id, group.id)
    new = db.get_contacts_in_group(group)
    assert contact not in new


