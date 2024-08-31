class ContactHelper:
    def __init__(self, app):
        self.app = app


    def return_to_home(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def create(self, contact):
        # fill contact form
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
        # submit
        wd.find_element_by_xpath("//div[@id='content']/form/input[20]").click()

    def open(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def delete_contact(self):
        wd = self.app.wd
        # select first contact
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()



