from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bulletins', '0096_remove_max_length_text_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='seuilscompteurcaracteres',
            name='discipline_commentaire_limit',
            field=models.PositiveIntegerField(default=0, help_text='0 = pas de limite', verbose_name='Limite stricte'),
        ),
        migrations.AddField(
            model_name='seuilscompteurcaracteres',
            name='discipline_descriptif_limit',
            field=models.PositiveIntegerField(default=0, help_text='0 = pas de limite', verbose_name='Limite stricte'),
        ),
        migrations.AddField(
            model_name='seuilscompteurcaracteres',
            name='stage_descriptif_limit',
            field=models.PositiveIntegerField(default=0, help_text='0 = pas de limite', verbose_name='Limite stricte'),
        ),
        migrations.AddField(
            model_name='seuilscompteurcaracteres',
            name='stage_appreciation_limit',
            field=models.PositiveIntegerField(default=0, help_text='0 = pas de limite', verbose_name='Limite stricte'),
        ),
        migrations.AddField(
            model_name='seuilscompteurcaracteres',
            name='projet_descriptif_limit',
            field=models.PositiveIntegerField(default=0, help_text='0 = pas de limite', verbose_name='Limite stricte'),
        ),
        migrations.AddField(
            model_name='seuilscompteurcaracteres',
            name='projet_appreciation_limit',
            field=models.PositiveIntegerField(default=0, help_text='0 = pas de limite', verbose_name='Limite stricte'),
        ),
        migrations.AddField(
            model_name='seuilscompteurcaracteres',
            name='avis_college_limit',
            field=models.PositiveIntegerField(default=0, help_text='0 = pas de limite', verbose_name='Limite stricte'),
        ),
    ]
