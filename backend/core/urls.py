from django.contrib import admin
from django.urls import path
from rest_framework import routers
from contact import views as contact_views

router = routers.DefaultRouter()

urlpatterns = router.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', contact_views.ContactAPIView.as_view())
]
