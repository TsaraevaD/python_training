# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

    
def test_add_contact(app):
    app.open_home_page()
    app.session.login("admin", "secret")
    app.contact.open()
    app.contact.create(Contact("f-name", "mid-name", "l-name"))
    app.contact.return_to_home()
    app.session.logout()
