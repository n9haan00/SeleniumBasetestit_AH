from seleniumbase import BaseCase

class DropdownTest(BaseCase):
    def test_dropdown(self):
        # Opens the Profilence home page
        self.open("https://profilence.com/")
        
        # Check page title
        self.assert_title("Profilence Technical Quality Analysis")

        # Open dropdown menu and click about us link + wait 3 seconds
        self.click('button[class="nav-link"]')
        self.click('a[href="https://profilence.com/company/"]')
        self.wait(1)

        # Open dropdown menu and click blog
        self.click('button[class="nav-link"]')
        self.click('a[href="https://profilence.com/category/blog/"]')
        self.wait(1)
        # Open dropdown menu and click careers and check page title
        self.click('button[class="nav-link"]')
        self.click('a[href="https://profilence.com/careers/"]')
        self.assert_title("Profilence  opportunities - Profilence")