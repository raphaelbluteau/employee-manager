from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from employee.models import Employee
from employee.views import EmployeeList

list_view = EmployeeList.as_view()


class EmployeeTest(TestCase):

    def setUp(self):
        User.objects.create_superuser(username='test_user', email='test_user@example.com', password='9pfgHk12')
        Employee.objects.create(name="Lorem", email="lorem@ipsum.com", department="Dolor Department")

    def test_employee_model_info(self):
        """
        Tests the creation of Employee model instances
        """
        employee = Employee.objects.get(email="lorem@ipsum.com")
        self.assertEqual(employee.email, "lorem@ipsum.com")
        self.assertEqual(employee.name, "Lorem")
        self.assertEqual(employee.department, "Dolor Department")

    def test_employee_endpoint_get(self):
        """
        Tests the endpoint /employee for the request method GET
        """
        self.client = Client()
        self.client.login(username='test_user', password='9pfgHk12')
        expected = [{'name': 'Lorem', 'email': 'lorem@ipsum.com', 'department': 'Dolor Department'}]

        response = self.client.get(reverse('employee'), format='json')
        self.assertEqual(200, response.status_code)
        self.assertEqual(expected, response.data)

    def test_employee_endpoint_post(self):
        """
        Tests the endpoint /employee for the request method POST
        """
        self.client = Client()
        self.client.login(username='test_user', password='9pfgHk12')

        response = self.client.post(reverse('employee'), {'name': 'Name', 'email': 'email@test.com',
                                                          'department': 'D1'}, format='json')
        self.assertEqual(201, response.status_code)
        self.assertEqual('D1', Employee.objects.get(email='email@test.com').department)
        self.assertEqual('Name', Employee.objects.get(email='email@test.com').name)

    def test_employee_endpoint_delete(self):
        """
        Tests the endpoint /employee/<pk> for the request method DELETE
        """
        self.client = Client()
        self.client.login(username='test_user', password='9pfgHk12')

        response = self.client.delete(reverse('employee_detail', args=['lorem@ipsum.com']), format='json')

        self.assertEqual(204, response.status_code)
        with self.assertRaises(Employee.DoesNotExist): Employee.objects.get(email='lorem@ipsum.com')
