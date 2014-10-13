from django.conf.urls import patterns, include
from tastypie.api import Api
from api import EntryResource, UserResource

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(EntryResource())

urlpatterns = patterns('',
    (r'^api/', include(v1_api.urls)),
)
