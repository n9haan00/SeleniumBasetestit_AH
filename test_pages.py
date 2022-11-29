from seleniumbase import BaseCase

class PagesTest(BaseCase):
    def test_page_links(self):
        # Opens the Profilence home page
        self.open("https://profilence.com/")
        
        # Check page title
        self.assert_title("Profilence Technical Quality Analysis")
        
        # Clicks platforms link
        self.click('a[href="https://profilence.com/products/"]')
        
        # Check for correct URL
        product_url = self.get_current_url()
        self.assert_equal(product_url, "https://profilence.com/products/")
        
        # Click services link
        self.click('a[href="https://profilence.com/services/"]')

        # Check for correct URL
        services_url = self.get_current_url()
        self.assert_equal(services_url, "https://profilence.com/services/")
