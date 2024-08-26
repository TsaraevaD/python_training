# -*- coding: utf-8 -*-
import pytest
from application import Application
from contact import Contact

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

    
def test_add_contact(app):
    app.open_home_page()
    app.login("admin", "secret")
    app.open_new_contact()
    app.create_contact(Contact("f-name", "mid-name", "l-name"))
    app.return_to_contacts()
    app.logout()
