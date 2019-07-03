from django.shortcuts import redirect, render, reverse, Http404
from django.http import HttpResponse
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView
from django.contrib.auth.models import Group
from django.db.models import Q
from django.core.exceptions import PermissionDenied
from users.models import Reporter, DepartmentHead, QualityDepartment
from userrole.permissions import CheckPermissionCreateMixin, CheckPermissionUpdateMixin, CheckPermissionListMixin, \
    CheckPermissionDeleteMixin, CheckPermissionDetailMixin
from .forms import ReporterSignupForm, DepartmentSignupForm, QdSignupForm
from .mixins import ReporterMixin, DepartmentMixin, QdMixin


class ReporterCreateView( ReporterMixin, CreateView):
    template_name = 'reporter_form.html'

    def get(self, request, *args, **kwargs):
        form = ReporterSignupForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = ReporterSignupForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = True
            user.save()
            user.groups.add(Group.objects.get(name='Reporter'))

            first_name = form.cleaned_data['first_name']
            middle_name = form.cleaned_data['middle_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            gender = form.cleaned_data['gender']
            phone = form.cleaned_data['phone']
            address = form.cleaned_data['address']
            signature = form.cleaned_data['signature']
            Reporter.objects.create(user=user, first_name=first_name, middle_name=middle_name,
                                          last_name=last_name, email=email, gender=gender, phone=phone,
                                          address=address, signature = signature
                                         )
            return redirect('/admin')

        return render(request, self.template_name, {'form': form})