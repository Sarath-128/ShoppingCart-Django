from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('add_to_cart/<int:book_id>/',views.Add_cart,name="addcart"),
    path("view_card/",views.view_card,name='viewcart'),
    path('increase_quantity/<int:item_id>/',views.increase_quantity,name='increase'),
    path('decrease_quantity/<int:item_id>/',views.decrease_quantity,name='decrease'),
    path('remove/<int:item_id>/',views.remove_cart,name='remove'),

    path('create-checkout-session/',views.create_checkout_session, name="create-checkout-session"),
    path('success/',views.success,name='success'),
    path('cancel/',views.cancel, name='cancel' )

]