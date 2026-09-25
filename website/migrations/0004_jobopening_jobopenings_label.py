from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_jobopening_verbose_name_plural'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jobopening',
            options={'verbose_name_plural': 'JobOpenings'},
        ),
    ]
