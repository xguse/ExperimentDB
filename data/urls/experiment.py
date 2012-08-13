from django.conf.urls.defaults import *
from django.views.generic.create_update import create_object, update_object, delete_object
from django.contrib.auth.decorators import permission_required

from data.forms import ExperimentForm

from data import views

urlpatterns = patterns('',
	url(r'^new/$', 'django.views.generic.create_update.create_object', {
		'form_class': ExperimentForm, 
		'template_name': 'experiment_form.html', 
		'login_required':True ,
		}, name="experiment-new"),
	url(r'^(?P<experimentID>[-\w]+)/$', 'data.views.experiment', name="experiment-detail"),
	url(r'^(?P<experimentID>[-\w]+)/result/new/$', 'data.views.result_new', name="result-new"),
	url(r'^(?P<slug>[-\w]+)/edit/$', views.ExperimentEdit.as_view(), name="experiment-edit"),
	url(r'^$', 'data.views.index', name="experiment-list"),
)
