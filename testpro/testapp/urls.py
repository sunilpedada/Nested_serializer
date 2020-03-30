from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter
from.views import user_register
root=DefaultRouter()
root.register("viewset",user_register)
urlpatterns=[
    url(r"",include(root.urls)),
]