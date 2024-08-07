"""
URL configuration for cryptocurrency_tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import debug_toolbar

from cryptodata.views import CoinsListView
from favourites.views import FavouritesListView, FavouriteAddOrDelete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CoinsListView.as_view(), name='cryptocurrency_list'),
    path('watchlist/', FavouritesListView.as_view(), name='watchlist'),
    path('toggle-favourite/', FavouriteAddOrDelete.as_view(), name='toggle-favourite'),
    path('accounts/', include('accounts.urls')),
    # debug toolbar URLS
    path('__debug__/', include(debug_toolbar.urls)),
]
