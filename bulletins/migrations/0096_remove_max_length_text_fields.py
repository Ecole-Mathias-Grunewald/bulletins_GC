from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bulletins', '0095_add_afficher_rang_to_miseenpage'),
    ]

    operations = [
        # Appreciation
        migrations.AlterField(
            model_name='appreciation',
            name='commentaire',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='appreciation',
            name='commentaire_correction',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='appreciation',
            name='remarque_correction',
            field=models.TextField(null=True, blank=True),
        ),
        # AvisCollege
        migrations.AlterField(
            model_name='aviscollege',
            name='avis',
            field=models.TextField(null=True, blank=True),
        ),
        # AvantPropos
        migrations.AlterField(
            model_name='avantpropos',
            name='contenu',
            field=models.TextField(null=True, blank=True, verbose_name='Contenu'),
        ),
        # Discipline
        migrations.AlterField(
            model_name='discipline',
            name='descriptif',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='discipline',
            name='descriptif_correction',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='discipline',
            name='remarque_correction',
            field=models.TextField(null=True, blank=True),
        ),
        # Stage
        migrations.AlterField(
            model_name='stage',
            name='descriptif',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='stage',
            name='descriptif_correction',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='stage',
            name='appreciation',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='stage',
            name='appreciation_correction',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='stage',
            name='remarque_correction',
            field=models.TextField(null=True, blank=True),
        ),
        # Projet
        migrations.AlterField(
            model_name='projet',
            name='descriptif',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='projet',
            name='descriptif_correction',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='projet',
            name='appreciation',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='projet',
            name='appreciation_correction',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='projet',
            name='remarque_correction',
            field=models.TextField(null=True, blank=True),
        ),
    ]
