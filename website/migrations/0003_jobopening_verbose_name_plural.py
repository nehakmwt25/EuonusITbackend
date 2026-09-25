from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_company_company_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jobopening',
            options={'verbose_name_plural': 'Openings'},
        ),
    ]
