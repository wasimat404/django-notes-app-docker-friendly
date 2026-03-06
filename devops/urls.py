from django.contrib import admin
from django.urls import path, include
from notes.views import notes_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('notes/', include('notes.urls')),
    path('', notes_list),
]
