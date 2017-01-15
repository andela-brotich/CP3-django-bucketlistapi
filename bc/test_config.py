from django.contrib.auth.models import User
from django.test import TestCase

from bc.api.models import BucketList, BucketListItem


class BaseTestCase(TestCase):
    def setUp(self):
        super(BaseTestCase, self).setUp()

        #  test users
        self.brian = User(first_name='Brian', last_name='Rotich',
                          username='brian', password='password',
                          email='brian@gmail.com')
        self.brian.save()
        self.brian.refresh_from_db()

        self.tom = User(first_name='Tom', last_name='Hardy',
                        username='tom', password='password',
                        email='tom@gmail.com')
        self.tom.save()
        self.tom.refresh_from_db()

        #  bucketlist for each user
        self.brian_bucketlist = BucketList(name='Checkpoint', user=self.brian,
                                           description='Task for checkpoint')
        self.brian_bucketlist.save()
        self.brian_bucketlist.refresh_from_db()

        self.tom_bucketlist = BucketList(
                                name='Checkpoint', user=self.tom,
                                description='Task for checkpoint')
        self.tom_bucketlist.save()
        self.tom_bucketlist.refresh_from_db()

        # add item to brian bucket list
        self.brian_bucketlist_item = BucketListItem(
            name='Write Tests', description='Complete models',
            bucketlist=self.brian_bucketlist
        )
        self.brian_bucketlist_item.save()
        self.brian_bucketlist_item.refresh_from_db()

        # tokens
        self.token = {'Authorization': 'Token {}'.format('TOKEN HERE')}
