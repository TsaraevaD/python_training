from model.group import Group

def test_modify_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="", header="New", footer=""))
    app.group.modify_first_group(Group(name="New group"))

def test_modify_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Old", header="field", footer=""))
    app.group.modify_first_group(Group(header="New header"))

