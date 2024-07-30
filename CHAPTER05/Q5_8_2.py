members = [
        ['01', '0001', 'Male', 'Yamada', 'Tarou', 25, 'Tokyo'],
        ['01', '0002', 'Male', 'Satou', 'Takeshi', 27, 'Kanagawa'],
        ['01', '0003', 'Female', 'Tanaka', 'Yuko', 25, 'Saitama'],
        ['02', '0001', 'Male', 'Smith', 'Mike', 22, 'NewJersey'],
        ['02', '0002', 'Male', 'Turner', 'Tom', 27, 'Kansas'],
        ['02', '0003', 'Male', 'Jackson', 'David', 25, 'Florida'],
]
print(members)

member_dict = {}
for member in members:
    key =( member[0], member[1])
    info = member[2:]
    member_dict[key] = info

print('number', 'infomation', sep='\t')
for key, info in member_dict.items():
    print(key, info)
