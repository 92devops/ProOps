from django import  forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

from .models import Mobile


class MobileForm(forms.ModelForm):
    # 字段验证方法1
    # mobile_num = forms.CharField(label="号码", validators=[RegexValidator(r'^135\d{8}$', '需要以135开头')])
    class Meta:
        model = Mobile
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        # super(Form, self).__init__(*args, **kwargs)
        super().__init__(*args, **kwargs)
        # for field in self.fields:
        #     self.fields[field].widget.attrs = {'class': 'form-control'}
        for name, field in self.fields.items():
            field.widget.attrs = {'class': 'form-control', "placeholder": field.label}

    # 字段验证方法2
    def clean_mobile_num(self):
        m = self.cleaned_data["mobile_num"]
        if len(m) != 11:
            raise ValidationError("手机号不合法")

        if Mobile.objects.filter(mobile_num=m).exists():
            raise ValidationError("手机号已存在")
        return  m

class MobileEditForm(forms.ModelForm):
    """
     专用于编辑手机号的Form
    """
    mobile_num = forms.CharField(disabled=True, label="手机号")
    class Meta:
        model = Mobile
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        # super(Form, self).__init__(*args, **kwargs)
        super().__init__(*args, **kwargs)
        # for field in self.fields:
        #     self.fields[field].widget.attrs = {'class': 'form-control'}
        for name, field in self.fields.items():
            field.widget.attrs = {'class': 'form-control', "placeholder": field.label}

    # 字段验证方法2


