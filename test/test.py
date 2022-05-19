import unittest
from .models import Users, Comment, Expense

#Test classes
class UserModelTest(unittest.TestCase):

    def setUp(self):
        self.new_user = User(password = 'mypassword')

    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)

    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('mypassword'))


class ExpenseModelTest(unittest.TestCase):
        '''
        Test class to test the behavior of the Expense class
        '''

        def setUp(self):
            '''
            Set up method that will run before every Test
            '''
            self.new_expense = Expense(1, 1,' expense', 'expense','1', 'expense')

        def test_instance(self):
            '''
            '''
            self.assertTrue(isinstance(self.new_expense, Expense))

        def test_to_check_instance_variables(self):
            '''
            '''
            self.assertEquals(self.new_expense.id, 1)
            self.assertEquals(self.new_expense.owner_id, 1)
            self.assertEquals(self.new_expense.name, 'expense')
            self.assertEquals(self.new_expense.merchant, 'expense')
            self.assertEquals(self.new_expense.amount, '1')
            self.assertEquals(self.new_expense.description, 'expense')


class CommentModelTest(unittest.TestCase):
        '''
        Test class to test the behavior of the Comment class
        '''

        def setUp(self):
            '''
            Set up method that will run before every Test
            '''
            self.new_comment = Comment(1, 1,' comment')

        def test_instance(self):
            '''
            '''
            self.assertTrue(isinstance(self.new_comment, Comment))

        def test_to_check_instance_variables(self):
            '''
            '''
            self.assertEquals(self.new_expense.id, 1)
            self.assertEquals(self.new_comment.owner_id, 1)
            self.assertEquals(self.new_comment.content, 'comment')
            
if __name__ == '__main__':
    unittest.main()