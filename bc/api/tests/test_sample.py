from bc.test_config import BaseTestCase


class BucketListTestCase(BaseTestCase):

    def test_sample(self):
        data = {
            'name': 'Create Checkpoint APi',
            'description': 'Finish this thing man'

        }
        response = self.client.post('/bucketlist.json', data=data, follow=True)

        # response = response.json()
        # self.assertEqual(data['name'], response['name'])
        # self.assertEqual(data['description'], response['description'])