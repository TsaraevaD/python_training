import re
from model.contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def return_to_home(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def create(self, contact):
        wd = self.app.wd
        self.fill_contact_form(contact)
        # submit
        wd.find_element_by_xpath("//div[@id='content']/form/input[20]").click()
        self.contact_cache = None

    def add(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def delete(self):
        self.delete_by_index(0)

    def delete_by_index(self, index):
        wd = self.app.wd
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.contact_cache = None

    def delete_by_id(self, id):
        wd = self.app.wd
        self.select_contact_by_id(id)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def change(self):
        self.change_by_index(0)

    def change_by_index(self, index, contact):
        wd = self.app.wd
        self.select_contact_by_index(index)
        # fill contact form
        self.fill_contact_form(contact)
        # submit edition
        wd.find_element_by_xpath("//input[@value='Update']").click()
        self.contact_cache = None

    def change_by_id(self, id, contact):
        wd = self.app.wd
        self.select_contact_by_id(id)
        wd.find_element_by_xpath("//a[@href='edit.php?id=%s']" % id).click()
        # fill contact form
        self.fill_contact_form(contact)
        # submit edition
        wd.find_element_by_xpath("//input[@value='Update']").click()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)

    def select_first_contact(self):
        wd = self.app.wd
        self.open_home_page()
        # select first contact
        wd.find_element_by_xpath("//img[@alt='Edit']").click()

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("./") and len(wd.find_elements_by_name("searchform") > 0)):
            wd.find_element_by_link_text("home").click()

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_css_selector("tr[name=entry]"):
                cells = element.find_elements_by_tag_name("td")
                id = cells[0].find_element_by_name("selected[]").get_attribute("value")
                lastname = cells[1].text
                firstname = cells[2].text
                address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(id=id, lastname=lastname, firstname=firstname, address=address,
                                                  all_phones_from_home_page=all_phones, all_emails_from_home_page=all_emails))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id,
                       homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, address=address, email=email, email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        return Contact(homephone=homephone, mobilephone=mobilephone, workphone=workphone)

    def add_to_group(self, id, group_id):
        wd = self.app.wd
        self.select_contact_by_id(id)
        wd.find_element_by_name("to_group").click()
        wd.find_element_by_xpath("//select[@name='to_group']/option[@value='%s']" % group_id).click()
        wd.find_element_by_name("add").click()
        wd.find_element_by_xpath("//a[@href='./?group=%s']" % group_id).click()

    def delete_from_group(self, id, group_id):
        wd = self.app.wd
        self.select_contact_by_id(id)
        wd.find_element_by_xpath("//select[@name='group']/option[@value='%s']" % group_id).click()
        wd.find_element_by_xpath("//input[@value='%s']" % id).click()
        wd.find_element_by_name("remove").click()
        wd.find_element_by_xpath("//a[@href='./?group=%s']" % group_id).click()














