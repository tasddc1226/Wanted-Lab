import os, django, csv

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wanted_lab.settings")
django.setup()

from company.models import *

CSV_PATH_POS_RESULT_DATA = './wanted_temp_data.csv'

with open(CSV_PATH_POS_RESULT_DATA) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        company_ko = row[0] 
        company_en = row[1] 
        company_ja = row[2] 
        tag_ko = row[3] 
        tag_en = row[4] 
        tag_ja = row[5] 
        Company.objects.create(
            company_ko = company_ko,
            company_en = company_en,
            company_ja = company_ja,
            tag_ko = tag_ko,
            tag_en = tag_en,
            tag_ja = tag_ja
        )