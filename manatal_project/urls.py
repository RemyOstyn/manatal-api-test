from django.contrib import admin
from django.urls import include, path
from rest_framework_nested import routers
from manatal import views

# Basic routers for Schools and Students endpoints
router = routers.DefaultRouter()
router.register(r'schools', views.SchoolViewSet)
router.register(r'students', views.StudentViewSet)

# Nested routers to lookup for student in specific school
school_router = routers.NestedSimpleRouter(router, r'schools', lookup='schools')
school_router.register(r'students', views.StudentViewSet, basename='school-students')

# Include router URLs and login URLs
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('', include(school_router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
