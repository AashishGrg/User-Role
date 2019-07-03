from django.shortcuts import reverse
from users.models import Reporter, DepartmentHead, QualityDepartment
from .forms import ReporterSignupForm, DepartmentSignupForm, QdSignupForm


class ReporterMixin(object):
    model = Reporter
    context_object_name = 'reporters'
    form_class = ReporterSignupForm

    def get_success_url(self):
        return reverse('/admin')


class DepartmentMixin(object):
    model = DepartmentHead
    form_class = DepartmentSignupForm
    context_object_name = 'departments'

    def get_success_url(self):
        return reverse('/admin')

class QdMixin(object):
    model = QualityDepartment
    form_class = QdSignupForm
    context_object_name = 'students'

    def get_success_url(self):
        return reverse('/admin')
