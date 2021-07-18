from django.forms import ModelForm
from cj_app.models import CjCategory, CjPost

class CjCategoryForm(ModelForm):
    class Meta:
        model = CjCategory
        fields = "__all__"

class CjPostForm(ModelForm):
    class Meta:
        model = CjPost
        fields = "__all__"