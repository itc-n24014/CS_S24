import pathlib

p = pathlib.Path('.')
for pf in p.glob('a*'):
    if pf.is_file():
        print(pf)
