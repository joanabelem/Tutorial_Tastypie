from tastypie.resources import ModelResource
from django.contrib.auth.models import User
from tastypie import fields
from entrys.models import Entry
from tastypie.authentication import BasicAuthentication


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'auth/user'
        excludes = ['email', 'password', 'is_superuser']
        authentication = BasicAuthentication()


class EntryResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user')

    class Meta:
        queryset = Entry.objects.all()
        resource_name = 'entry'
        authentication = BasicAuthentication()
