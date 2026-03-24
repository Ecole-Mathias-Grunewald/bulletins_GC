from bulletins import models


def seuils_compteur_caracteres(request):
    return {
        'seuils_compteur': models.SeuilsCompteurCaracteres.get_settings()
    }
