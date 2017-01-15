from bc.test_config import BaseTestCase


class IndexTest(BaseTestCase):

    def test_sample(self):
        response = self.client.get('/bucketlist.json', follow=True)

        self.assertEqual(200, response.status_code)

        self.assertIn(self.bucketlist.name,response.json())