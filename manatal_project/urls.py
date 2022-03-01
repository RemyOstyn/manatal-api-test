from django.contrib import admin
from django.urls import include, path
from rest_framework_nested import routers
from manatal import views

router = routers.DefaultRouter()
router.register(r'schools', views.SchoolViewSet)
router.register(r'students', views.StudentViewSet)

school_router = routers.NestedSimpleRouter(router, r'schools', lookup='schools')
school_router.register(r'students', views.StudentViewSet, basename='school-students')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('', include(school_router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
