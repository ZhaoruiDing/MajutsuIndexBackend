from django.urls import path
from anime import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('signup', views.register, name='register'),
    path('animes', views.anime_display, name='anime_display'),
    path('animes/rec', views.recommend, name='recommend'),
    path('animes/fav', views.fav, name='favorite'),
    path('search/all', views.search, name='search'),
    path('search/fav', views.search_fav, name='search_fav'),
    path('search/date', views.date, name='search_date'),
    path('watchstatus', views.change_watch_status, name='status'),
    path('animes/debugjson', views.debug_json, name='debug_json'),
    path('animes/wish', views.wishlist, name='wishlist'),
    path('detail', views.detail_page, name='detail_page'),
    path('animes/popular', views.popular, name='popular'),
    path('rate', views.rate, name='rate'),
    path('status/likestatus', views.anime_like, name='like_status'),
    path('animes/watched', views.watched, name='watched'),
    path('animes/watching', views.watching, name='watching')
]
