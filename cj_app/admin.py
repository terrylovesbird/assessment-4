from django.contrib import admin
from cj_app.models import CjCategory, CjPost

#admin username: admin, password: admin
admin.site.register(CjCategory)
admin.site.register(CjPost)