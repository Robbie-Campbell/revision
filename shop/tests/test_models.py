from django.test import TestCase
from shop.models import Post, Category

class PostTestCase(TestCase):
    def setUp(self):
        self.post = Post.objects.create(category=Category.objects.create(), title="title")

    def test_post_return_case(self):
        return self.assertTrue(str(self.post), "title")

    def test_post_data_type(self):
        return self.assertTrue(isinstance(self.post, Post))

    def test_post_ne_return_case(self):
        return self.assertNotEqual(self.post, "hello")

class CategoryTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(cat_name="category")

    def test_category_return_case(self):
        return self.assertTrue(str(self.category), "category")

    def test_category_data_type(self):
        return self.assertTrue(isinstance(self.category, Category))
    
    def test_category_ne_return_case(self):
        return self.assertNotEqual(self.category, "hello")