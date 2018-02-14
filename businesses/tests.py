from django.test import TestCase
from django.urls import reverse
from .models import Business
from .forms import BusinessForm


class BusinessViewTestCase(TestCase):
    def setUp(self):
        self.data = {
            "name": "You're a noob...",
            "description": "You're a noob if you're reading this right now.",
            "established": "1994-02-18",
        }
        self.business_1 = Business.objects.create(name="Coded1", description="This is Coded1", established="2017-10-10")
        self.business_2 = Business.objects.create(name="Coded2", description="This is Coded2", established="2017-11-11")
        self.business_3 = Business.objects.create(name="Coded3", description="This is Coded3", established="2017-12-12")

    def test_create_view(self):
        create_url = reverse("business_create")
        response = self.client.get(create_url)
        self.assertEqual(response.status_code, 200)

        response2 = self.client.post(create_url, self.data)
        self.assertEqual(response2.status_code, 302)

    def test_update_view(self):
        update_url = reverse("business_update", kwargs={"business_id":self.business_1.id})
        response = self.client.get(update_url)
        self.assertEqual(response.status_code, 200)

        response = self.client.post(update_url, data=self.data)
        self.assertEqual(response.status_code, 302)

    def test_delete_view(self):
        delete_url = reverse("business_delete", kwargs={"business_id":self.business_1.id})
        response = self.client.get(delete_url)
        self.assertEqual(response.status_code, 302)


class BusinessFormTestCase(TestCase):
    def test_valid_form(self):
        name = "Some Company"
        description = "Some random description"
        established = "2017-10-10"
        obj = Business.objects.create(name=name, description=description, established=established)
        data = {
            'name':obj.name,
            'description': obj.description,
            'established': obj.established,
        }
        form = BusinessForm(data=data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data.get('name'), obj.name)
        self.assertEqual(form.cleaned_data.get('description'), obj.description)

    def test_invalid_form(self):
        name = "Some Company"
        established = "2017-10-10"
        obj = Business.objects.create(name=name, established=established)
        data = {
            'name':obj.name,
            'established': obj.established,
        }
        form = BusinessForm(data=data)
        self.assertFalse(form.is_valid())