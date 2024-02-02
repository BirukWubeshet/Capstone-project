from django.test import TestCase, RequestFactory

from .models import Menu
from .serializers import MenuSerializer
from .views import MenuItemView

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title='IceCream', price=80, inventory=100)
        self.assertEqual(item.__str__(), 'IceCream : 80')

class MenuViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        
        Menu.objects.create(title='IceCream', price=80, inventory=100)
        Menu.objects.create(title='Salad', price=100, inventory=00)
    
    def test_getall(self):
        request = self.factory.get('/restaurant/menu/')
        
        menuitems = Menu.objects.all()
        serialized_menuitems = MenuSerializer(menuitems, many=True)
        
        response = MenuItemView.as_view()(request)
        
        self.assertEqual(response.data, serialized_menuitems.data)