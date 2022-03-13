passports = open('input.txt').read().split('\n\n')
fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
valid = 0

for passport in passports:
    if all(field in passport for field in fields):
        valid += 1

print(valid)

import re

fields = {
    'byr': lambda v: 1920 <= int(v) <= 2002,
    'iyr': lambda v: 2010 <= int(v) <= 2020,
    'eyr': lambda v: 2020 <= int(v) <= 2030,
    'hgt': lambda v: v[-2:] == 'cm' and 150 <= int(v[:-2]) <= 193 or v[-2:] == 'in' and 59 <= int(v[:-2]) <= 76,
    'hcl': lambda v: bool(re.fullmatch('^#[a-f0-9]{6}$', v)),
    'ecl': lambda v: v in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
    'pid': lambda v: bool(re.fullmatch('^[0-9]{9}$', v))
}

trues = 0
for line in re.sub(r'\n(\S)', r' \1', open('input.txt').read()).splitlines():
    doc = {value.split(':')[0]: value.split(':')[1] for value in line.split()}
    trues += int(all([f in doc for f in fields]) and all([k == 'cid' or fields[k](v) for k, v in doc.items()]))
print(trues)
