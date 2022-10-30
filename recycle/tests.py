from django.test import TestCase, Client

# Create your tests here.


class TestUrls(TestCase):
    def setUp(self):
        self.client = Client()
        self.index_url = ("/recycle/")
        self.jsonquestionall_url = ("/recycle/json-question-all/")

    def test_index_url(self):
        response = self.client.get((self.index_url))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")

    def test_jsonQuestionAll_url(self):
        response = self.client.get((self.jsonquestionall_url))
        self.assertEquals(response.status_code, 200)
