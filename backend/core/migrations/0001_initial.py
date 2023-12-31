# Generated by Django 4.2.7 on 2023-12-31 12:09

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="ClassRoom",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        choices=[
                            ("JUNIOR SECONDARY SCHOOL 1", "Junior Secondary School 1"),
                            ("JUNIOR SECONDARY SCHOOL 2", "Junior Secondary School 2"),
                            ("JUNIOR SECONDARY SCHOOL 3", "Junior Secondary School 3"),
                            ("SENIOR SECONDARY SCHOOL 1", "Senior Secondary School 1"),
                            ("SENIOR SECONDARY SCHOOL 2", "Senior Secondary School 2"),
                            ("SENIOR SECONDARY SCHOOL 3", "Senior Secondary School 3"),
                        ],
                        max_length=30,
                        unique=True,
                    ),
                ),
                (
                    "code",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("JSS 1", "Jss 1"),
                            ("JSS 2", "Jss 2"),
                            ("JSS 3", "Jss 3"),
                            ("SSS 1", "Sss 1"),
                            ("SSS 2", "Sss 2"),
                            ("SSS 3", "Sss 3"),
                        ],
                        max_length=10,
                        null=True,
                        unique=True,
                    ),
                ),
                ("capacity", models.PositiveIntegerField(default=1)),
                (
                    "stream",
                    models.CharField(
                        choices=[("A", "A"), ("B", "B"), ("C", "C"), ("D", "D")],
                        max_length=1,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Exam",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "exam_type",
                    models.CharField(
                        choices=[
                            ("Mid Term", "Midterm"),
                            ("Final Exam", "Final"),
                            ("Quiz", "Quiz"),
                        ],
                        max_length=10,
                    ),
                ),
                ("scheduled_date", models.DateTimeField(auto_now_add=True)),
                (
                    "duration",
                    models.DurationField(
                        validators=[
                            django.core.validators.MaxValueValidator(
                                limit_value=datetime.timedelta(seconds=10800),
                                message="Duration should not exceed 3 hours.",
                            )
                        ]
                    ),
                ),
                (
                    "max_marks",
                    models.PositiveIntegerField(
                        validators=[
                            django.core.validators.MaxValueValidator(
                                limit_value=100,
                                message="Maximum marks should not exceed 100.",
                            )
                        ]
                    ),
                ),
                ("instructions", models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "classroom",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="core.classroom",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Subject",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        choices=[
                            ("ENGLISH LANGUAGE", "English Language"),
                            ("MATHEMATICS", "Mathematics"),
                            ("AGRICULTURAL SCIENCE", "Agricultural Science"),
                            ("BIOLOGY", "Biology"),
                            ("ECONOMICS", "Economics"),
                            ("CIVIC EDUCATION", "Civic Education"),
                            ("FRENCH LANGUAGE", "French"),
                            ("FURTHER MATHEMATICS", "Further Mathematics"),
                            ("CHEMISTRY", "Chemistry"),
                            ("PHYSICS", "Physics"),
                            ("GEOGRAPHY", "Geography"),
                            ("COMPUTER SCIENCE", "Computer Science"),
                            ("SOCIAL STUDIES", "Social Studies"),
                            ("MUSIC", "Music"),
                            ("GOVERNMENT", "Government"),
                            ("COMMERCE", "Commerce"),
                        ],
                        max_length=30,
                    ),
                ),
                (
                    "code",
                    models.CharField(
                        choices=[
                            ("ENG", "Eng"),
                            ("MTH", "Mth"),
                            ("AGS", "Ags"),
                            ("BIO", "Bio"),
                            ("ECONS", "Econs"),
                            ("CVE", "Cve"),
                            ("FRN", "Frn"),
                            ("FMTH", "Fmth"),
                            ("CHM", "Chm"),
                            ("PHY", "Phy"),
                            ("GEO", "Geo"),
                            ("CPS", "Cps"),
                            ("SOS", "Sos"),
                            ("MUSIC", "Music"),
                            ("GOV", "Gov"),
                            ("COMMERCE", "Commerce"),
                        ],
                        max_length=10,
                    ),
                ),
                ("added_at", models.DateTimeField(auto_now_add=True)),
                (
                    "class_room",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.classroom"
                    ),
                ),
            ],
            options={
                "unique_together": {("title", "code", "class_room")},
            },
        ),
        migrations.CreateModel(
            name="Teacher",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "assigned_subjects",
                    models.ManyToManyField(related_name="teachers", to="core.subject"),
                ),
                (
                    "classroom",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="core.classroom",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        limit_choices_to={"role": "Teacher"},
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SubjectResult",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "marks_obtained",
                    models.PositiveIntegerField(
                        validators=[django.core.validators.MaxValueValidator(100)]
                    ),
                ),
                ("remarks", models.TextField(null=True)),
                (
                    "exam",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.exam"
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.student"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="student",
            name="enrolled_subjects",
            field=models.ManyToManyField(related_name="student", to="core.subject"),
        ),
        migrations.AddField(
            model_name="student",
            name="user",
            field=models.OneToOneField(
                limit_choices_to={"role": "Student"},
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="exam",
            name="subject",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="core.subject"
            ),
        ),
        migrations.CreateModel(
            name="Admin",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.OneToOneField(
                        limit_choices_to={"role": "Admin"},
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
