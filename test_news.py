from seleniumbase import BaseCase

class NewsTest(BaseCase):
    def test_news(self):
        # Open the home page
        self.open("https://profilence.com/")

        self.scroll_to_bottom()

        self.click('a[href="/newsletter/"]')

        self.add_text('#mce-EMAIL', 'test@email.com')

        self.wait(1)

        self.click('input[id="gdpr_45714"]')

        self.click('input[id="mc-embedded-subscribe"]')