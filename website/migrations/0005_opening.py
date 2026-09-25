from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_jobopening_jobopenings_label'),
    ]

    operations = [
        migrations.CreateModel(
            name='Opening',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_job', models.CharField(max_length=120, verbose_name='Type of job')),
                ('background_image', models.ImageField(blank=True, null=True, upload_to='openings/')),
                ('heading', models.CharField(max_length=180)),
                ('address', models.CharField(max_length=255)),
                ('short_description', models.TextField()),
            ],
            options={
                'verbose_name': 'Opening',
                'verbose_name_plural': 'Openings',
            },
        ),
    ]
