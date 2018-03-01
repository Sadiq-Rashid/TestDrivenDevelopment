def main ():
    ''' Main 
    '''
    cont = Contact ('sa', 'ra', '728652l')
    print(cont.mobile)
    print('done')




class Contact ():

    '''
        Phonebook: contains a contacts basic data; names are case-sensitive
        params: first_name, last_name, mobile
    '''
    def __init__ (self, first_name, last_name, mobile):
        self.first_name = first_name
        self.last_name = last_name
        self._mobile = None
        self.mobile = mobile

    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, num):
        # should raise ValueError for non-int characters
        num = int(num)
        self._mobile = num



class Phonebook():
    '''
        Phonebook: contains a list of contacts
            methods:    add_contact
                            params: Contact object
                        update_contact
                            paramas: first_name, last_name, new_first, new_last, new_mobile
                        delete_contact
                            params: first_name, last_name
                        view_contact
                            params: first_name, last_name
            params:     none
    '''

    def __init__(self):
        self.contacts = []

    def add_contact (self, contact):
        for existing in self.contacts:
            if existing.first_name == contact.first_name and existing.last_name == contact.last_name:
                assert 0, 'Duplicate Contact'

        self.contacts.append(contact)
        pushed_contact = self.contacts[-1]
        return pushed_contact.first_name

    def update_contact (self, first_name, last_name,
                        new_first = None, new_last = None, new_mobile = None):

        for contact in self.contacts:
            if contact.first_name == first_name and contact.last_name == last_name:
                if new_first: contact.first_name = new_first
                if new_last: contact.last_name =  new_last
                if new_mobile: contact.mobile =  new_mobile

                return contact
                break

    def delete_contact (self, first_name, last_name):

        for contact in self.contacts:
            if contact.first_name == first_name and contact.last_name == last_name:
                del contact
                break

    def view_contact (self, first_name, last_name):

        for contact in self.contacts:
            if contact.first_name == first_name and contact.last_name == last_name:
                return contact.mobile
                break


#call main

if __name__ == "__main__":
    main ()