import csv
import re

total = 0.0
pge_corp_total = 0.0
pge_utility_total = 0.0
engineering_companies = 0.0
construction_companies = 0.0

with open('claims.csv', 'r') as f:
    csv_r = csv.reader(f)
    csv_r = list(csv_r)
    for creditor, debtor, claim in csv_r[1:]:
        claim = float("".join([char for char in claim if char not in '$ ,']))
        total += claim
        total = round(total, 2)
        if 'PG&E Corporation' in debtor:
            pge_corp_total += claim
            pge_corp_total = round(pge_corp_total, 2)
        if 'Pacific Gas and Electric Company' in debtor:
            pge_utility_total += claim
            pge_utility_total = round(pge_utility_total, 2)
        if 'engineering' in creditor.lower() or 'consulting' in creditor.lower(
        ):
            engineering_companies += claim
            engineering_companies = round(engineering_companies, 2)
        if 'construction' in creditor.lower(
        ) or 'excavation' in creditor.lower():
            construction_companies += claim
            construction_companies = round(construction_companies, 2)

print({
    "total": total,
    "pge_corp_total": pge_corp_total,
    "pge_utility_total": pge_utility_total,
    "engineering_companies_total": engineering_companies,
    "construction_companies_total": construction_companies
})
