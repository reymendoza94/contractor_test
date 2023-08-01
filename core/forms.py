from django import forms
from django.forms import inlineformset_factory
from .models import Label

class LabelForm(forms.ModelForm):
    
    class Meta:
        model = Label
        #fields = ['label_name','label_type','level','assignament','exclusibity']
        fields = "__all__"
        # autocomplete_fields = 'level'

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            # if self.instance.label == 'multi_level':

MultiLevelFormSet = inlineformset_factory(
    Label, Label, form=LabelForm,
    extra=1, can_delete=True, can_delete_extra=True
)               
