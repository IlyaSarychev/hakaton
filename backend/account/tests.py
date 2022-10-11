from dataclasses import dataclass

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import ContractorAccount, User, CustomerAccount
from .serializers import ContractorAccountSerializer


@dataclass
class Credentials:
    email = "testcontractor@mail.ru"
    password = "contractor1234"


class ContractorsTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        ContractorAccount.objects.create(
            email="testcontractor@mail.ru",
            password="contractor1234",
            first_name="Евгений",
            last_name="Жмышенко",
            TIN="1010101010",
            position="Мафиозник",
            phone_number="79530421122"
        )
        CustomerAccount.objects.create(
            email="testcustomer@mail.ru",
            password="contractor1234",
            first_name="Алексей",
            last_name="Алеша",
            position="айтишник",
            phone_number="79539425122"
        )

    def login(self):
        self.client.login(email=Credentials.email, password=Credentials.password)

    def test_get_contractors_without_auth(self):
        url = reverse("contractors")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_contractors(self):
        self.login()

        url = reverse("contractors")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(ContractorAccountSerializer(ContractorAccount.objects.all(), many=True).data, response.json())

    def test_create_contractor(self):
        url = reverse("contractors")
        data = {
            "first_name": "test",
            "last_name": "test",
            "email": "testtestuser@test.ru",
            "password": "newtestpassword123",
            "TIN": "0123456789",
            "position": "iluha",
            "phone_number": "70123456789",
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ContractorAccount.objects.last().TIN, "0123456789")

    def test_get_contractor_info(self):
        self.login()

        last_contractor = ContractorAccount.objects.last()
        url = reverse("retrieve_update_delete_contractor", kwargs={"pk": last_contractor.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["user"]["last_name"], "Жмышенко")

    def test_update_contractor_info(self):
        self.login()

        last_contractor = ContractorAccount.objects.last()
        url = reverse("retrieve_update_delete_contractor", kwargs={"pk": last_contractor.id})
        self.client.patch(url, data={"position": "Бомж"})
        last_contractor = ContractorAccount.objects.last()
        self.assertEqual(last_contractor.position, "Бомж")

    def test_delete_contractor(self):
        self.login()

        last_contractor = ContractorAccount.objects.last()
        url = reverse("retrieve_update_delete_contractor", kwargs={"pk": last_contractor.id})
        self.client.delete(url)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_user_info(self):
        self.login()

        last_user = User.objects.last()
        url = reverse("retrieve_update_delete_user", kwargs={"pk": last_user.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_user_info(self):
        self.login()

        last_user = User.objects.last()
        url = reverse("retrieve_update_delete_user", kwargs={"pk": last_user.id})
        self.client.patch(url, data={"last_name": "Кириешко"})
        last_user = User.objects.last()
        self.assertEqual(last_user.last_name, "Кириешко")

    def test_delete_user(self):
        self.login()

        last_user = User.objects.last()
        url = reverse("retrieve_update_delete_contractor", kwargs={"pk": last_user.id})
        self.client.delete(url)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_customer_info(self):
        self.login()

        last_customer = CustomerAccount.objects.last()
        url = reverse("retrieve_update_delete_customer", kwargs={"pk": last_customer.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["user"]["last_name"], "Алеша")

    def test_update_customer_info(self):
        self.login()

        last_customer = CustomerAccount.objects.last()
        url = reverse("retrieve_update_delete_customer", kwargs={"pk": last_customer.id})
        self.client.patch(url, data={"position": "Бомж"})
        last_customer = CustomerAccount.objects.last()
        self.assertEqual(last_customer.position, "Бомж")

    def test_delete_customer(self):
        self.login()

        last_customer = CustomerAccount.objects.last()
        url = reverse("retrieve_update_delete_customer", kwargs={"pk": last_customer.id})
        self.client.delete(url)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
