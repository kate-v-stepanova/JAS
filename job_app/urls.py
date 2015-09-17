from django.conf.urls import patterns, include, url

from django.contrib import admin

from views import home, login, register, logout, cover_letter_pdf, applications
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
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
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    # pdf
urlpatterns += patterns("",
    url(r"^cover_letter_pdf$", cover_letter_pdf, name='cover_letter_pdf'),
)