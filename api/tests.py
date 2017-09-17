from django.test import TestCase
from .models import BucketList
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse
class ModelTestCase(TestCase):
    def setUp(self):
        self.bucketlist_name = "Hello world"
        self.bucketlist = BucketList(name = self.bucketlist_name)
    def test_model_can_create_a_bucketlist(self):
        old_count = BucketList.objects.count()
        self.bucketlist.save()
        new_count = BucketList.objects.count()
        self.assertNotEqual(old_count,new_count)
class ViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.bucketlist_data = {'name':'Phuoc Nguyen'}
        self.response = self.client.post(
            reverse('create'),
            self.bucketlist_data,
            format='json'
        )
    def test_api_can_create_a_bucketlist(self):
        """Test the api has bucket creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)