from django.contrib.auth.models import User
from django.test import TestCase

from bc.api.models import BucketList


class BaseTestCase(TestCase):
    def setUp(self):
        super(BaseTestCase, self).setUp()

        #  TODO add test users

        #  TODO add test bucket list for users

        # TODO add bucket list items
