from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

class Myaccount(BaseUserManager): 
    def create_user(self,username,first_name,last_name,email,password):
    #Declaro las variables de entrada y valido que no sean nulas de caso contrario elevo el error con RAISE.
        if not email:
            raise ValueError ("Se debe declarar el mail")
        if not username:
            raise ValueError ("Se debe agregar el nombre de usuario")
        if not password:
            raise ValueError ("Se debe tener una contraseña")

    # Creo el usuario y añado los datos de las variables 
        user = self.model(email = self.normalize_email(email),
                            password = password,
                            username = username, 
                            first_name = last_name,
                            last_name = last_name)

 # Añado la contraseña y guardo el usuario en la base de datos mediante "using = self._db".
        user.set_password(password)
        user.save(using = self._db)
        return user
 
# Creacion de un super usuario.
    def create_superuser(self,username,first_name,last_name,email,password):
        user = self.model(email = self.normalize_email(email),
        username = username, 
        password = password,
        first_name = last_name,
        last_name = last_name)
        #Se agregan los valores de administrador de la aplicacion
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using = self._db)

        return user



class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=40)
    username = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    phone_number = models.IntegerField(max_length=40)

    #campos requeridos por django para crear un usuario.
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login=models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active= models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name']

    #Instanciamos la class
    objetcs = Myaccount()

    def __str__(self) -> str:
        return self.email

    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self,add_label):
        return True