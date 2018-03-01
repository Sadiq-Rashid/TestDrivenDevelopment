import unittest

from app.phonebook import Phonebook, Contact

class PhonebookTestCase (unittest.TestCase):

    def setUp (self):
        self.phonebook = Phonebook ()



    def test_add_contact (self):
        contact = Contact ('Samira', 'mariam', '728655088')
        first_name = self.phonebook.add_contact (contact)
        self.assertEqual (first_name, 'Samira')

        #test that it raises ValueError for non int chars
        with self.assertRaises (ValueError):
            contact.mobile = '07a5280860'

        with self.assertRaises (AssertionError):
            self.phonebook.add_contact (contact)

    def test_update_contact (self):

        contact = Contact ('Samira', 'mariam', '728655088')
        self.phonebook.add_contact (contact)

        # test update first_name alone
        updated_contact = self.phonebook.update_contact("Samira", "mariam", new_first = "Samira Olive")
        self.assertEqual(updated_contact.first_name, 'Samira Olive')

        # test update last_name alone
        updated_contact = self.phonebook.update_contact("Samira Olive", "mariam", new_last = "Murimi")
        self.assertEqual (updated_contact.last_name, 'Murimi')

        # test update mobile number alone
        updated_contact = self.phonebook.update_contact("Samira Olive", "Murimi", new_mobile = "725280260")
        self.assertEqual (updated_contact.mobile, 725280260)

        # test update All
        updated_contact = self.phonebook.update_contact("Samira Olive", "Murimi", new_mobile = "728655088",
                                                            new_last = 'mariam',
                                                            new_first = 'Samira')

        # for loop here
        self.assertEqual (updated_contact.mobile, 728655088)
        self.assertEqual (updated_contact.first_name, 'Samira')
        self.assertEqual (updated_contact.last_name, 'mariam')


    def test_delete_contact (self):

        contact = Contact ('Lazuli', 'Muthoni', '728655088')
        self.phonebook.add_contact (contact)

        # delete second contact
        self.phonebook.delete_contact ('Sheelah', 'B')

        # check if the contact still exists
        contact = None
        for contact in self.phonebook.contacts:
            if contact.first_name == 'Sheelah' and contact.last_name == 'B':
                contact = contact
                break
        #if contact is not None, then it was not deleted successfully
        self.assertNotEqual(contact, None)


    def test_view_contact(self):

            contact = Contact ('Lazuli', 'Muthoni', '728655088')
            self.phonebook.add_contact (contact)

            mobile = self.phonebook.view_contact('Lazuli', 'Muthoni')
            self.assertEqual(mobile, 728655088)






if __name__ == "__main__":
    unittest.main ()