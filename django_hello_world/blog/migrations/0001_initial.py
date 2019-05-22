from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.AutoField(
                        db_column="category_id", primary_key=True, serialize=False
                    ),
                ),
                ("name", models.CharField(max_length=100)),
            ],
            options={"verbose_name_plural": "categories", "db_table": "category"},
        ),
        migrations.CreateModel(
            name="Note",
            fields=[
                (
                    "id",
                    models.AutoField(
                        db_column="note_id", primary_key=True, serialize=False
                    ),
                ),
                ("keywords", models.CharField(max_length=400)),
                ("title", models.CharField(max_length=200)),
                ("date", models.DateTimeField()),
                ("content", models.TextField(max_length=50000)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="blog.Category"
                    ),
                ),
            ],
            options={"db_table": "note"},
        ),
    ]
