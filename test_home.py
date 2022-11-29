from seleniumbase import BaseCase

class HomeTest(BaseCase):
    def test_home_page(self):
        # Opens the profilence homepage
        self.open("https://profilence.com/")
        # Checks page title
        self.assert_title("Profilence Technical Quality Analysis")
        # Checks Profilence logo
        self.assert_element('img[alt="Profilence"]')