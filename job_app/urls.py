from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

# from views import home, login, register, logout, cover_letter_pdf, applications
from views.profile import profile
from views.home import home, cover_letter_pdf
from views.auth import login, register, logout
from views.applications import applications

admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'job_app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # admin
    url(r'^admin/', include(admin.site.urls)),
    # auth
    url(r'^register/$', register, name='register'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    # custom
    url(r'^$', home, name="home"),
    url(r'^applications/$', applications, name='applications'),
    # profile
    url(r'^profile/$', profile, name='profile'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    # pdf
urlpatterns += [
    url(r"^cover_letter_pdf$", cover_letter_pdf, name='cover_letter_pdf'),
]