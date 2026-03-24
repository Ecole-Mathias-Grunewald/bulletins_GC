from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bulletins', '0093_add_afficher_descriptif_classe_to_miseenpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='miseenpagebulletin',
            name='bulletin_semestriel',
            field=models.BooleanField(default=False, help_text="Si coché, le terme «Trimestre» est remplacé par «Semestre» dans l'en-tête du bulletin.", verbose_name='Bulletin semestriel'),
        ),
    ]
