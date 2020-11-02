from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import UpdateView, CreateView
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from .models import Question, User
from .forms import RegisterUserForm, ChangeUserInfoForm


def index(request):
	que = Question.objects.all()[:10]
	context = {"questions": que}
	return render(request, 'main/index.html', context=context)


class BBLoginView(LoginView):
	template_name = 'main/login.html'


class BBLogoutView(LoginRequiredMixin, LogoutView):
	template_name = 'main/logout.html'


class ChangeUserInfoView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
	model = User
	template_name = 'main/changeUserInfo.html'
	form_class = ChangeUserInfoForm
	success_url = reverse_lazy('myApp:profile')
	success_message = 'Личные данные пользователя изменены'

	def dispatch(self, request, *args, **kwargs):
		self.user_id = request.user.pk
		return super().dispatch(request, *args, **kwargs)

	def get_object(self, queryset=None):
		if not queryset:
			queryset = self.get_queryset()
		return get_object_or_404(queryset, pk=self.user_id)


class BBPasswordChangeView(SuccessMessageMixin, LoginRequiredMixin, PasswordChangeView):
	template_name = 'main/passwordChange.html'
	success_url = reverse_lazy('myApp:profile')
	success_message = 'Пароль пользователя изменен'


class RegisterUserView(CreateView):
	model = User
	template_name = 'main/registerUser.html'
	form_class = RegisterUserForm
	success_url = reverse_lazy('myApp:login')


class RegisterDoneView(TemplateView):
	template_name = 'main/registerDone.html'
