def test_delete(app):
    app.session.login("admin", "secret")
    app.contact.delete()
    app.session.logout()
