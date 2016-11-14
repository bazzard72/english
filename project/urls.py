from django.conf.urls import include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^gradelist/$','main.views.gradelist'),
    url(r'^grade/(?P<pk>\d+)/$','main.views.gradedetail'),
    url(r'^subfield/(?P<pk>\d+)/$','main.views.subfielddetail'),
    url(r'^$','main.views.stage'),
    url(r'^stage/(?P<pk>\d+)/$','main.views.stagedetail'),
    url(r'^teacher/$','main.views.teacher'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
	