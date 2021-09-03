
from test.page.LoginPage import LoginPage
from test.common.SampleReview import SampleReview


class SampleReviewPage(LoginPage):

    def sample_search(self, sample_number):
        SampleReview(self.driver).sample_search(sample_number)

    def sample_reply(self, review_result, note, button):
        SampleReview(self.driver).sample_reply(review_result, note, button)

    def upload_sample(self):
        SampleReview(self.driver).upload_sample()

    def download_sample(self):
        SampleReview(self.driver).download_sample()
