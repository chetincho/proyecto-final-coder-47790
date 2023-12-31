from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreAnimal', models.CharField(max_length=40)),
                ('edad', models.IntegerField()),
                ('tipo', models.CharField(max_length=40)),
                ('motivo', models.CharField(max_length=40)),
                ('fecha', models.DateField()),
                ('costo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('telefono', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Veterinario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('veterinario', models.CharField(max_length=20)),
                ('apellidoVet', models.CharField(max_length=40)),
                ('matricula', models.CharField(max_length=40)),
            ],
        ),
    ]
