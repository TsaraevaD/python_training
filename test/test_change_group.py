from model.group import Group

def test_change(app):
    app.session.login("admin", "secret")
    app.group.change(Group("name", "header", "footer"))
    app.session.logout()

