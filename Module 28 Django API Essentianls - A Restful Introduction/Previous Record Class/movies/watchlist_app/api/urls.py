from django.urls import path
from .import views 


urlpatterns = [
    # path('', views.movie_list),
    # path('<pk>/', views.movie_detail),

    # For list and create operations (GET /movies/, POST /movies/)
    path('', views.MovieListCreateView.as_view(), name='movie-list-create'),
    
    # For detail operations (GET /movies/1/, PUT /movies/1/, PATCH /movies/1/, DELETE /movies/1/)
    path('<int:pk>/', views.MovieDetailView.as_view(), name='movie-detail'),

]




