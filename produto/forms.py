
from django import forms

from produto.models import Produto

class ProdutoForm(forms.ModelForm):    
    class Meta:
        model = Produto
        exclude = ["slug"]

    def __init__(self, *args, **kwargs):
        super(ProdutoForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    

    
