from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=20, blank=True)
    dni = models.CharField(max_length=10, blank=True)
    foto = models.ImageField(upload_to='perfiles/', blank=True, null=True)
    CHOICE_ROLE = [
        ('OPERADOR', 'Operador'),
        ('ADMINISTRADOR', 'administrador'),
        ('TURISTA', 'Turista')
    ]
    rol = models.CharField(max_length= 20, choices= CHOICE_ROLE, default='TURISTA')

    def __str__(self):
        return self.user.username


def _sync_role_from_groups(user: User):
    perfil, _ = Perfil.objects.get_or_create(user=user)
    if user.is_superuser:
        nuevo = "ADMINISTRADOR"
    elif user.groups.filter(name__iexact="operador").exists():
        nuevo = "OPERADOR"
    else:
        nuevo = "TURISTA"
    if perfil.rol != nuevo:
        perfil.rol = nuevo
        perfil.save(update_fields=["rol"])

@receiver(post_save, sender=User)
def ensure_profile_and_role(sender, instance, created, **kwargs):
    Perfil.objects.get_or_create(user=instance)
    _sync_role_from_groups(instance)

@receiver(m2m_changed, sender=User.groups.through)
def user_groups_changed(sender, instance, action, **kwargs):
    if action in {"post_add", "post_remove", "post_clear"}:
        _sync_role_from_groups(instance)


