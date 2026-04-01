from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bulletins', '0094_add_bulletin_semestriel_to_miseenpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='miseenpagebulletin',
            name='afficher_rang',
            field=models.BooleanField(default=False, help_text="Si coché, le rang de l'élève s'affiche sur la ligne des statistiques (moyenne, min, max) dans les matières où il est activé.", verbose_name="Afficher le rang de l'élève"),
        ),
    ]
