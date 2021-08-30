from django.test import TestCase
from django.contrib.auth import get_user_model

from store.models import Category, Product


class TestCategoryModel(TestCase):
    def setUp(self):
        self.data1 = Category.objects.create(name="django", slug="django")

    def test_category_model_entry(self):
        """Test category model data insertion"""
        data = self.data1
        self.assertTrue(isinstance(data, Category))

    def test_category_model_name(self):
        """Test the default name of model object"""
        data = self.data1
        self.assertEqual(str(data), "django")


class TestProductsModel(TestCase):
    def setUp(self):
        category = Category.objects.create(name="django", slug="django")
        get_user_model().objects.create(username="admin")
        payload = {
            "category": category,
            "title": "django beginners",
            "created_by_id": 1,
            "slug": "django-beginners",
            "price": 20.00,
            "image": "django.jpg",
        }
        self.data1 = Product.objects.create(**payload)
        another_payload = {
            "category": category,
            "title": "django advanced",
            "created_by_id": 1,
            "slug": "django-advanced",
            "price": 20.00,
            "image": "django-advanced.jpg",
        }
        self.data2 = Product.objects.create(**another_payload)

    def test_products_model_entry(self):
        """Test product model data insertion/types/field attributes"""
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), "django beginners")
