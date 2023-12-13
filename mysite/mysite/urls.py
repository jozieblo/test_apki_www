from django.contrib import admin
from django.urls import path, include
from polls import views
urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('admin-tools/', include('admin_tools.urls'), ),

    path('osoby/', views.person_list),
    path('osoba/', views.person_add),
    path('osoba/<int:pk>/', views.person_detail),

    path('stanowiska/', views.stanowisko_list),
    path('stanowisko/', views.stanowisko_add),
    path('stanowisko/<int:pk>/', views.stanowisko_detail),

    path('api-auth/', include('rest_framework.urls')),
]