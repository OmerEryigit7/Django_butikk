from django.urls import path

from . import views

urlpatterns = [
	path('', views.store, name="store"),
    path('registrer_produkt', views.register_product, name='register_product_url'),
    path('opprett_bruker', views.register_user, name='create_user_url'),
    path('logg_inn', views.login_user, name='login_url'),
    path('produkt/<pk>', views.get_product_info, name='get_product_info')
]