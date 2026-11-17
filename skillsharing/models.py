from django.db import models
from django.conf import settings


MAX_LENGTH = 400


def text_excerpt(text, max_length):
    return text[:max_length] + ('...' if len(text) > max_length else '')


class Skill(models.Model):
    name = models.CharField(max_length=200)

    # Relation ManyToMany :
    # - Un utilisateur peut posséder plusieurs compétences.
    # - Une compétence peut être possédée par plusieurs utilisateurs.
    users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="skills",
        blank=True,
    )

    def __str__(self):
        return self.name


class HelpRequest(models.Model):
    # Description de l'activité nécessitant une aide.
    description = models.TextField()

    # Date et heure du début et de fin du créneau demandé.
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    # Relation ForeignKey : un utilisateur peut créer
    # plusieurs demandes, mais chaque demande possède
    # obligatoirement un seul demandeur.
    #
    # CASCADE : si le demandeur est supprimé,
    # toutes ses demandes d'aide sont supprimées.
    requester = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="created_requests",
    )

    # Relation ForeignKey : un utilisateur peut aider
    # sur plusieurs demandes, mais chaque demande
    # possède au maximum un aidant.
    #
    # SET_NULL : si l'aidant est supprimé,
    # la demande est conservée et helper devient NULL.
    helper = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="helped_requests",
        null=True,
        blank=True,
    )

    # Relation ForeignKey : chaque demande nécessite
    # une seule compétence, mais une compétence peut
    # être associée à plusieurs demandes.
    #
    # PROTECT : empêche la suppression d'une compétence
    # si elle est utilisée par au moins une demande d'aide.
    skill = models.ForeignKey(Skill, on_delete=models.PROTECT)

    def __str__(self):
        return text_excerpt(self.description, MAX_LENGTH)
