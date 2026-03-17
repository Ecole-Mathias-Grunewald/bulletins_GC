from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bulletins", "0088_miseenpagebulletin_couleuravantpropos"),
    ]

    operations = [
        migrations.AddField(
            model_name="discipline",
            name="activerRangMaxMin",
            field=models.BooleanField(
                default=False, verbose_name="afficher rang, note max et min"
            ),
        ),
    ]

