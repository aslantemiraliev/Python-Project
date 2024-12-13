Geeks = {
    'address': 'Toktogula 175',
    'courses': ['Android', 'Backend', 'Frontend'],
    'bag': {'fails', 'errors', 'stack'}
}
del Geeks['bag']
Geeks['address'] = ('Ибраимово 103,БЦ Victory')
Geeks['instagram'] = ('@geeks_edu')
Geeks['phone']= ('+996 507 052 018')
Geeks['courses'].extend(['Frontend', 'UX/UI', 'Android/IOS'])
Geeks['courses'] = set(Geeks['courses'])
Geeks['foundation_date'] = '2018-05-21'
print(f"Количество курсов: {len(Geeks['courses'])}")
for key, value in Geeks.items():
    print(f"{key}: {value}")
