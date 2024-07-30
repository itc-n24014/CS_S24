members = [
        ['0001', 'Male', 'Yamada', 'Tarou', 25, 'Tokyo'],
        ['0002', 'Male', 'Satou', 'Takeshi', 27, 'Kanagawa'],
        ['0003', 'Female', 'Tanaka', 'Yuko', 25, 'Saitama'],
        ['0004', 'Male', 'Suzuki', 'Ichirou', 35, 'Hokkaido'],
]
print(members)

member_dict = {}
for member in members:
    key = member[0]
    info = member[1:]

    member_dict[key] = info

print('number', 'infomation', sep='\t')
for key, info in member_dict.items():
    print(key, info)

