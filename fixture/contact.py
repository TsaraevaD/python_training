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

    def add(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def delete(self):
        wd = self.app.wd
        self.select_first_contact()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()

    def change(self, contact):
        wd = self.app.wd
        self.select_first_contact()
        # fill contact form
        self.fill_contact_form(contact)
        # submit edition
        wd.find_element_by_xpath("//input[@value='Update']").click()

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
        wd.find_element_by_link_text("home").click()







