from django.contrib import admin
from .models import User, Question, Voice, Answer


admin.site.register(User)
admin.site.register(Question)
admin.site.register(Voice)
admin.site.register(Answer)
