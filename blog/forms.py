from django import forms
from ckeditor.widgets import CKEditorWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from blog.models import Comment


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            Fieldset(
                '',
                'name',
                'email',
                'body',
            ),
            ButtonHolder(
                Submit('submit', 'Enviar', css_class='btn btn-primary btn-lg')
            )
        )
        self.fields['name'].widget.attrs['placeholder'] = "Nome"
        self.fields['email'].widget.attrs['placeholder'] = "E-mail"
        self.fields['body'].widget.attrs['placeholder'] = "Deixe sua mensagem"