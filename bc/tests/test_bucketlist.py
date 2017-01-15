from bc.test_config import BaseTestCase


class BucketListTestCase(BaseTestCase):
    def test_gets_bucketlist_for_user(self):
        response = self.client.get('/bucketlist/', follow=True,
                                   headers=self.token)

        self.assertIn(self.brian_bucketlist.name, response.json()[0]['name'])
        self.assertIn(self.brian_bucketlist.description,
                      response.json()[0]['description'])

    def test_it_creates_new_bucketlist(self):
        data = {
            'name': 'Create Checkpoint API',
            'description': 'Finish this thing man'

        }
        response = self.client.post('/bucketlist/', data=data, follow=True,
                                    headers=self.token)

        self.assertEqual(201, response.status_code)

        response = response.json()
        self.assertEqual(data['name'], response['name'])
        self.assertEqual(data['description'], response['description'])

    def test_bucketlist_creation_fails_with_same_name(self):
        data = {
            'name': 'Create Checkpoint API',
            'description': 'Finish this thing man'

        }
        response = self.client.post('/bucketlist/', data=data, follow=True,
                                    headers=self.token)

        self.assertEqual(409, response.status_code)

        response = response.json()
        self.assertEqual('bucketlist with same name exits', response['error'])

    def test_bucketlist_create_fails_with_no_name(self):
        data = {
            'description': 'Finish this thing man'

        }
        response = self.client.post('/bucketlist/', data=data, follow=True,
                                    headers=self.token)

        response = response.json()
        self.assertEqual(400, response.status_code)
        self.assertEqual('name field missing/empty from POST request',
                         response['error'])

    def test_bucketlist_create_fails_with_no_token(self):
        data = {
            'name': 'Functional Weekend',
            'description': 'Finish this thing man'

        }
        response = self.client.post('/bucketlist/', data=data, follow=True)

        response = response.json()
        self.assertEqual(401, response.status_code)
        self.assertEqual('token not submitted',
                         response['error'])
