from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.shortcuts import redirect

# Simple homepage view
def home(request):
    return HttpResponse("Welcome to the Social Media API!")

# Optional: redirect root to /api/
# def root_redirect(request):
#     return redirect('/api/')

urlpatterns = [
    path('', home),  # root path
    # path('', root_redirect),  # use this if you prefer redirect to /api/
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
