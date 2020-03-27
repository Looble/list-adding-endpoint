from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase, APIRequestFactory
from coding_test.number_sum.views import TotalViewSet

class NumberAddTestCase(APITestCase):
    def test_number_totaling_returns_correctly(self):
        """
        Test that checks that the TotalViewSet endpoint returns a valid
        response that includes the total.
        """
        # TODO add test for correct total when the list is coming from an external source
        factory = APIRequestFactory()
        view = TotalViewSet.as_view({'get': 'list'})
        request = factory.get('')
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data), 1)
        self.assertIn('total', response.data)
