# -*- coding: utf-8 -*-
import pytest
from attachment import Attachment
from contact import Contact

@pytest.fixture
def att(request):
    fixture = Attachment()
    request.addfinalizer(fixture.destroy)
    return fixture

    
def test_add_contact(att):
    att.open_home_page()
    att.login("admin", "secret")
    att.open_new_contact()
    att.create_contact(Contact("f-name", "mid-name", "l-name"))
    att.return_to_contacts()
    att.logout()
