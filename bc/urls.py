from django.conf.urls import url, include

from bc.api.views import BucketListView
from bc import router

router.register(prefix='bucketlist', viewset=BucketListView)

urlpatterns = [

] + router.urls
