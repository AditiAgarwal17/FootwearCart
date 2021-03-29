
from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.index,name="ShopHome"),
    path("about/",views.about,name="AboutUs"),
    path("tracker/",views.tracker,name="Tracker"),
    path("contact/",views.contact,name="ContactUs"),
    path("search/",views.search,name="Search"),
    path("products/<int:myid>",views.productView,name="productView"),
    path("checkout/",views.checkOut,name="CheckOut"),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
   
    
]
