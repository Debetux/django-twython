from django.conf.urls import patterns, url

from twitter_connect import views

urlpatterns = patterns('',
	# ex: /polls/
	url(r'^$', views.index, name='index'),

	# First leg of the authentication journey...
    url(r'^login/?$', views.begin_auth, name="twitter_login"),

    # Logout, if need be
    url(r'^logout/?$', views.logout, name="twitter_logout"),  # Calling logout and what not

    # This is where they're redirected to after authorizing - we'll
    # further (silently) redirect them again here after storing tokens and such.
    url(r'^thanks/?$', views.thanks, name="twitter_callback"),

    # An example view using a Twython method with proper OAuth credentials. Clone
    # this view and url definition to get the rest of your desired pages/functionality.
    url(r'^user_timeline/?$', views.user_timeline, name="twitter_timeline"),
)