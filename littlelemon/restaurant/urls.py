from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'restaurant/booking/tables', views.BookingViewSet)

urlpatterns = [
    path('api-token-auth/', obtain_auth_token),
    path('', views.index, name='index'),
    path('restaurant/menu', views.MenuItemView.as_view()),
    path('restaurant/menu/<int:pk>', views.SingleMenuItemView.as_view()),
]

urlpatterns += router.urls