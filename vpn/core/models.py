from django.db import models
from django.utils.translation import gettext as _


class Solicitation(models.Model):
    """
    Bond Choices
    """
    IC = 'Aluno de IC'
    ME = 'Mestrado'
    DO = 'Doutorado'
    PD = 'Pós Doutorado'
    PC = 'Professor Colaborador ou visitante'

    BOND_CHOICES = (
        ('ic', IC),
        ('me', ME),
        ('do', DO),
        ('pd', PD),
        ('pc', PC),
    )

    """
    Departament choices
    """
    AST = 'Atronomia/Graduação'
    GEO = 'Geofísica/Graduação'
    ATM = 'Ciências Atmosféricas/Graduação'

    DEPTO_CHOICES = (
        ('ast', AST),
        ('geo', GEO),
        ('atm', ATM),
    )

    requester = models.ForeignKey("accounts.UserModel", verbose_name=_(
        "Requester"), on_delete=models.CASCADE)
    phone = models.CharField(_("Phone"), max_length=20)
    bond = models.CharField(_("Activity"), max_length=20, choices=BOND_CHOICES)
    departament = models.CharField(
        _("Departament"), max_length=20, choices=DEPTO_CHOICES)
    answerable = models.CharField(_("Answerable"), max_length=50)
    status = models.CharField(_("Status"), max_length=10)
    slug = models.SlugField(_("slug"))
    updated_by = models.ForeignKey("accounts.UserModel", verbose_name=_(
        "Updated by"), related_name='updated_by',
        on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)
