from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views
from infty.users import views


class JSONTemplateView(TemplateView):
    def render_to_response(self, context, **response_kwargs):
        response_kwargs['content_type'] = 'application/json'
        return super(TemplateView, self).render_to_response(context, **response_kwargs)


urlpatterns = [
    path('', JSONTemplateView.as_view(template_name='pages/home.html'), name='home'),
    path('about/', TemplateView.as_view(template_name='pages/about.html'), name='about'),

    # Django Admin, use {% url 'admin:index' %}
    path('admin/', admin.site.urls),

    # User management
    path('users/', include('infty.users.urls', namespace='users')),
    path('accounts/', include('allauth.urls')),
    path('api/', include('infty.api.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('captcha/', include('captcha.urls')),
    path('otp/singup/', views.OTPRegister.as_view()),
    path('otp/login/', views.OTPLogin.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path('400/', default_views.bad_request, kwargs={
            'exception': Exception('Bad Request!')
        }),
        path('403/', default_views.permission_denied, kwargs={
            'exception': Exception('Permission Denied')
        }),
        path('404/', default_views.page_not_found, kwargs={
            'exception': Exception('Page not Found')
        }),
        path('500/', default_views.server_error),
    ]
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns = [
            path('__debug__/', include(debug_toolbar.urls)),
        ] + urlpatterns
