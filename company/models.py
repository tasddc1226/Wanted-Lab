from django.db import models

class Company(models.Model):
    company_ko = models.CharField(max_length=100, blank=True, null=True)
    company_en = models.CharField(max_length=100, blank=True, null=True)
    company_ja = models.CharField(max_length=100, blank=True, null=True)
    tag_ko = models.CharField(max_length=255)
    tag_en = models.CharField(max_length=255)
    tag_ja = models.CharField(max_length=255)

    class Meta:
        db_table = 'company'