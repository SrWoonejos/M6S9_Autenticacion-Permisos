from django import forms

from .models import Usuario

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password']
        labels = {
            'username': 'Nombre de usuario',
            'email': 'Correo electrónico',
            'password': 'Contraseña',
        }
        help_texts = {
            'username': 'Un nombre de usuario único que contenga solo letras, números y @/./+/-/_ caracteres.',
            'email': 'Un correo electrónico válido.',
            'password': 'Una contraseña segura.',
        }
        error_messages = {
            'email': {
                'unique': 'Este correo ya está en uso.',
            },
        }
        
class LoginForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario', max_length=254)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        # Verifica si el usuario existe
        try:
            user = Usuario.objects.get(username=username, password=password)
        except Usuario.DoesNotExist:
            raise forms.ValidationError('Error de credenciales')
        # Si todo está bien, retornar el usuario
        cleaned_data["user"] = user
        return cleaned_data
    
    def authenticate(self):
        user = self.cleaned_data.get("user")
        if user is not None:
            return user
        return None