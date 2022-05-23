from django.db import models

class Company(models.Model):
    class Meta:
        db_table = 'company'

class Language(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    code = models.CharField(max_length=2, unique=True)

    class Meta:
        db_table = 'language'

class CompanyName(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    code = models.ForeignKey('Language', default='', on_delete=models.CASCADE)
    company = models.ForeignKey('Company', null=True, blank=True, on_delete=models.CASCADE)
    # TODO: tages fields 추가

    class Meta:
        db_table = 'company_name'

