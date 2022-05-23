from django.urls import path
from . import views
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'main'

urlpatterns = [
     path('',views.index, name='home'),
     path('contact/', views.contact, name="contact"),
     path('register/', views.register, name="register"),
     path('login/', views.login, name='login'),
     #path("logout/", views.logout, name="logout"),
     path('comments/', views.crudindex, name='comment'),
     path('comments/upload/', views.crud_upload, name='crud_upload'),
     path('comments/update/<int:crud_id>', views.crud_update),
     path('comments/delete/<int:crud_id>', views.crud_delete),
     #####################################################################
     path('product_list/', views.product_list, name='product_list'),
     path('<slug:category_slug>/', views.product_list,
          name='product_list_by_category'
          ),
     path('<int:id>/<slug:slug>', views.product_detail, 
          name='product_detail'),
     #####################################################################
     
     
]

