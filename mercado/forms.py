from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length,EqualTo,Email,DataRequired, ValidationError
from mercado.models import User
class CadastroForm (FlaskForm):
    def validate_username(self, username_to_check):
        user = User.query.filter_by(usuario=username_to_check.data).first()
        if user:
            raise ValidationError('Usuario ja existe! cadastre outro nome de usuario')
    def validate_email(self, email_to_check):
        email = User.query.filter_by(email=email_to_check.data).first()
        if email:
            raise ValidationError('Email ja cadastrado! cadastre outro email')
    def validate_senha(self, senha_to_check):
        senha = User.query.filter_by(senha=senha_to_check.data).first()
        if senha:
            raise ValidationError('Senha ja existe! cadastre outra senha')
    
    usuario = StringField(label='Username: ',validators=[Length(min=4,max=30),DataRequired()])
    email = StringField(label='Email: ',validators=[Email(),DataRequired()])
    senha1 = PasswordField(label='Senha:', validators=[Length(min=6),DataRequired()])
    senha2 = PasswordField(label='Confirmação de Senha:', validators=[EqualTo('senha1'),DataRequired()] )
    submit = SubmitField(label='Cadastrar')

class LoginForm(FlaskForm):
    usuario = StringField(label='Usuário: ',validators=[DataRequired()])
    senha1 = PasswordField(label='Senha:', validators=[DataRequired()])
    submit = SubmitField(label='Login')