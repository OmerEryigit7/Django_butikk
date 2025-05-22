from django.urls import path

from . import views

urlpatterns = [
	path('', views.store, name="store"),
    path('logg-ut', views.logout_user, name='logout_url'),
    path('registrer-produkt', views.register_product, name='register_product_url'),
    path('opprett-bruker', views.register_user, name='create_user_url'),
    path('logg-inn', views.login_user, name='login_url'),
    path('produkt/<pk>', views.get_product_info, name='get_product_info'),
    path('produkt/<pk>/add-to-cart', views.add_to_cart, name='add_to_cart'),
    path('handlekurv', views.get_cart, name='get_cart'),
]