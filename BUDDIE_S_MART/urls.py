"""
URL configuration for BUDDIE_S_MART project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from MyBuddie_s_Mart import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Homepage,name='homepage'),
    path('signin/',views.Signinpage,name='signinpage'),
    path('signup/',views.Signuppage,name='signuppage'),
    path('logout/',views.Logout,name='logoutpage'),
    path(' /<str:name>',views.Myproduct,name="productpage"),
    path(' /<str:sname>/<str:pname>',views.Product_details,name="Product_detailspage"),
    path('addtocart/',views.Add_to_cart,name='addtocart'),
    path('cart/',views.My_cart,name='cartpage'),
    path('remove/<str:cid>',views.Remove_cart,name='remove'),
    path('suppor/',views.Suppor,name='Supporpage'),

    path('checkout/',views.Checkout_mail,name='checkout'),

    path('shops/',views.Shop_page,name='Shop_page'),
    path('shops/<str:name>',views.Myproduct,name="productpage"),
    path('shops/<str:sname>/<str:pname>',views.Product_details,name="Product_detailspage"),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
