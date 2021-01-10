
from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView

# from .serializer import MoviesSerializer
# from .models import Movies
# from .models import Movies
from .serializer import MoviesSerializer
from .models import Movies

# Create your views here.
class MoviesListView(ListAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer

class MoviesDetailsView(RetrieveAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer