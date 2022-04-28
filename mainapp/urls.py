from django.urls import path
from . import views 
urlpatterns = [
    path('',views.index),

    path('farmer-signup/',views.farmer_signup, name='farmer-signup'),
    path("farmer-login/", views.farmer_login, name="farmer-login"),
    path("farmer_otp/", views.farmer_confirm_otp, name="farmer_otp"),
    path("farmer_home/", views.farmer_home, name="farmer_home"),
    path("farmer_home/farmer_complete_profile/",views.farmer_complete_profile,
    name="farmer_complete_profile"),
    path("farmer_home/product_form/", views.product_form, name="product_form"),

    path('businessman-signup/',views.businessman_signup, name='businessman-signup'),
    path("businessman-login/", views.businessman_login, name="businessman-login"),
    path("businessman_otp/", views.businessman_confirm_otp, name="farmer_otp"),
    path("businessman_home/", views.businessman_home, name="businessman_home"),
    path("businessman_home/businessman_complete_profile/",views.businessman_complete_profile),

    path("businessman_home/bidding_products/<str:product>",views.bidding_products, name='bidding_products' ),
    # path('businessman_home/soyabeen_page/',views.soyabeen_page, name='soyabeen' )

]