from django.conf.urls import url, include

from bc.api.views import BucketListViewSet
from bc import router

router.register(prefix='bucketlist', viewset=BucketListViewSet)

urlpatterns = [

] + router.urls
