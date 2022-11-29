from seleniumbase import BaseCase

class PicTest(BaseCase):
    def test_pics(self):
        # Open the home page
        self.open("https://profilence.com/")
        
        # Click the Customers link
        self.click('a[href="https://profilence.com/customers/"]')
        
        # Highlight all of the logos
        self.highlight('div[class="element-logo-grid-container"]')

        # Find all of the logos
        self.find_elements('div[class="logo-grid-element logo-grid-element-landscape"]')