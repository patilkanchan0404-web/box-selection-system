from django.test import TestCase
from .models import Product, Box


class BoxSelectionTest(TestCase):

    def setUp(self):
        self.small_box = Box.objects.create(
            name="Small Box",
            length=20,
            width=15,
            height=10,
            max_weight=2,
            cost=20
        )

        self.medium_box = Box.objects.create(
            name="Medium Box",
            length=40,
            width=30,
            height=15,
            max_weight=5,
            cost=35
        )

        self.large_box = Box.objects.create(
            name="Large Box",
            length=60,
            width=45,
            height=30,
            max_weight=10,
            cost=50
        )

    # TC01 - Product fits Small Box
    def test_product_fits_small_box(self):
        product = Product.objects.create(
            name="Mobile Phone",
            length=16,
            width=8,
            height=2,
            weight=0.5
        )

        response = self.client.post(
            "/",
            {"product": product.id}
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Small Box")
        self.assertContains(response, "20")

    # TC02 - Product fits Medium Box
    def test_product_fits_medium_box(self):
        product = Product.objects.create(
            name="Laptop",
            length=30,
            width=20,
            height=5,
            weight=2
        )

        response = self.client.post(
            "/",
            {"product": product.id}
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Medium Box")
        self.assertContains(response, "35")

    # TC03 - Product does not fit any box
    def test_product_does_not_fit_any_box(self):
        product = Product.objects.create(
            name="Large TV",
            length=100,
            width=80,
            height=50,
            weight=20
        )

        response = self.client.post(
            "/",
            {"product": product.id}
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No Suitable Box Found")

    # TC04 - Product weight exceeds box capacity
    def test_product_weight_exceeds_capacity(self):
        product = Product.objects.create(
            name="Heavy Product",
            length=15,
            width=10,
            height=5,
            weight=15
        )

        response = self.client.post(
            "/",
            {"product": product.id}
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No Suitable Box Found")

    # TC05 - Multiple boxes fit, lowest-cost box selected
    def test_lowest_cost_box_selected(self):
        product = Product.objects.create(
            name="Small Product",
            length=15,
            width=10,
            height=5,
            weight=1
        )

        response = self.client.post(
            "/",
            {"product": product.id}
        )

        self.assertEqual(response.status_code, 200)

        # Small Box and Medium Box both fit,
        # but Small Box has the lower cost.
        self.assertContains(response, "Small Box")
        self.assertContains(response, "20")