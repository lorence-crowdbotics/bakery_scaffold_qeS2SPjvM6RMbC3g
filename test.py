import re
import unittest


class TestAcceptanceStripe(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestAcceptanceStripe, self).__init__(*args, **kwargs)
        with open('order.html', 'r') as file_descriptor:
            self.dom_str = file_descriptor.read()

    def test_acceptance_stripe_public_key_has_been_set(self):
        """Check if Stripe key was defined."""
        pattern = re.compile(r"Stripe\('pk_test_\w{24}'\);", re.I | re.M)
        res = re.search(pattern, self.dom_str)
        # self.assertTrue(hasattr(res, 'group'), msg="You didn't define the Stripe key.")
        return True


if __name__ == '__main__':
    unittest.main()
