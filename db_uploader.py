import os, django, csv

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wanted_lab.settings")
django.setup()

from company.models import *

CSV_PATH_POS_RESULT_DATA = './wanted_temp_data.csv'

# step 1 : language code
code_list = ["ko", "en", "ja"]
for code in code_list:
    Language.objects.create(
        code = code
    )

# step 2 : insert unique companies ID
with open(CSV_PATH_POS_RESULT_DATA) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        Company.objects.create()


# step 3 : insert company name & language code & tags
with open(CSV_PATH_POS_RESULT_DATA) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for i, row in enumerate(data_reader):
        company_ko = row[0]
        tag_ko = row[3]
        CompanyName.objects.create(
            name = company_ko,
            code_id = 1,
            company_id = i+1,
            tags = tag_ko
        )

with open(CSV_PATH_POS_RESULT_DATA) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for i, row in enumerate(data_reader):
        company_en = row[1]
        tag_en = row[4]
        CompanyName.objects.create(
            name = company_en,
            code_id = 2,
            company_id = i+1,
            tags = tag_en
        )

with open(CSV_PATH_POS_RESULT_DATA) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for i, row in enumerate(data_reader):
        company_ja = row[2]
        tag_ja = row[5]
        CompanyName.objects.create(
            name = company_ja,
            code_id = 3,
            company_id = i+1,
            tags = tag_ja
        )