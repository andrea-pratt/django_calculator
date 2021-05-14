from django.test import TestCase
from .models import Calculation
from django.urls import reverse


class TestSaveCalculations(TestCase):

    def test_save_calculation_calculation_in_database(self):

        initial_calculation_count = Calculation.objects.count()
        calculation_url = reverse('save_calculation')
        response = self.client.post(calculation_url, {'first_operand': '3', 
                                                          'second_operand': '4',
                                                          'result': '7',
                                                          'operator': '+'}, follow=True)

        new_calculation_query = Calculation.objects.filter(calculation='3 + 4 = 7')

        self.assertEqual(new_calculation_query.count(), 1)
        self.assertEqual(Calculation.objects.count(), initial_calculation_count + 1)
        self.assertEqual(response.status_code, 200)


    def test_retrieve_10_results(self):

        calculation_url = reverse('save_calculation')

        for i in range(15):
            response = self.client.post(calculation_url, {'first_operand': '3', 
                                                          'second_operand': '4',
                                                          'result': '7',
                                                          'operator': '+'}, follow=True)
            self.assertEqual(response.status_code, 200)

        url = reverse('calculator')
        response = self.client.get(url)

        self.assertEqual(response.context['calculations'].count(), 10)
        self.assertEqual(response.status_code, 200)

