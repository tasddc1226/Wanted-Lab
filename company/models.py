from django.db import models

class Company(models.Model):
    class Meta:
        db_table = 'company'


class Language(models.Model):
    code = models.CharField(max_length=2, unique=True)
    in_use = models.BooleanField(default=True)
    is_test = models.BooleanField(default=False)
    test_textfield = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'language'


class CompanyName(models.Model):
    code = models.ForeignKey(Language, default='', on_delete=models.CASCADE)
    company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.CASCADE)

    name = models.CharField(max_length=100, null=True, blank=True)
    tags = models.JSONField(default=dict, null=True, blank=True)

    class Meta:
        db_table = 'company_name'

