from rest_framework import viewsets
from rest_framework import permissions
from manatal.models import School, Student
from manatal.serializers import SchoolSerializer, StudentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

# School View Set
# Adding filters for search
class SchoolViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows schools to be viewed or edited.
    """
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields  = ['name', 'address']

# School View Set
# Adding filters for search and ordering
class StudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows students to be viewed or edited.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields  = ['first_name', 'last_name','identification']
    ordering_fields = ['age']

    # This was done to allow the nested router to find the student belonging to the selected school
    def get_queryset(self):
        queryset = Student.objects.all()
        print(self.kwargs)
        if 'schools_pk' in self.kwargs:
            queryset = Student.objects.filter(school_id=self.kwargs['schools_pk'])
        return queryset
