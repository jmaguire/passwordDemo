
from zxcvbn import zxcvbn ## see https://github.com/dwolfhub/zxcvbn-python

blacklist = ['nEMvXyHeqDd5OQxyXYZI', 'c7e4f8EzqH', '23WKoa0FP78dk',
             'NICK1234-rem936', 'lk9slwGh3x', 'JwHw6N1742', 'e6pz84qfCJ',
             'xxPa33bq.aDNA', 'W1408776w', 'vEf6g55frZ', 'sS6z2sw6lU',
             'Hd764nW5d7E1vbv', 'H1Y4dUa229', 'Findaupair007',
             'BhRh0h2Oof6XbqJEH', 'yK66o2kzpZ', 'Soso123bbb', 'ProductId20F',
              'PolniyPizdec1102', 'p9uJkuf36D', 'jNe990pQ23', 'Jhon@ta2011',
              'IdeDeviceP0T', 'Gankutsuou1989', 'F64579820f', 'Efwe5tgwa5twhgd',
              'CzPS5NYNDWCkSC', '92k2cizCdP', 'Vsavb7rtUI', 'VHpuuLf2K',
              'Tojiik85521133', 'Soso12eec', 'seo21SAAfd23', 'Red7Stork',
              'Oap9UTO293', 'Nicrasow212', 'l0sk2e8S7a', 'Krzysiek12',
              'H2Tmc4g358', 'eqeS606898', 'ekx1x3k9BS', 'a58Wtjuz4U',
              '68iypNeg6U']

print('Reading data')

with open('100k.txt', 'r') as f:
    data = f.read().splitlines()

rules = [lambda s: any(x.isupper() for x in s),
         lambda s: any(x.islower() for x in s),
         lambda s: any(x.isdigit() for x in s),
         lambda s: any(not x.isalpha() for x in s),
         lambda s: len(s) >= 8,
         lambda s: len(s) <= 64
         ]

def password_check(s, level=3, blacklist = []):
    if all(rule(s) for rule in rules):
        return zxcvbn(s, user_inputs=blacklist)['score'] >= level  # faster this way
    return False

print('Applying rules to', len(data), 'passwords')

pass_at_3 = sum([1 for elem in data if password_check(elem, 3)])
pass_at_4 = sum([1 for elem in data if password_check(elem, 4)])

print('Pass at 3:', pass_at_3, 'out of ', len(data))
print('Pass at 4:', pass_at_4, 'out of ', len(data))

print('Testing with blacklist')
print('Applying rules to', len(data), 'passwords')
pass_at_3 = sum([1 for elem in data if password_check(elem, 3, blacklist)])
pass_at_4 = sum([1 for elem in data if password_check(elem, 4, blacklist)])

print('Pass at 3:', pass_at_3, 'out of ', len(data))
print('Pass at 4:', pass_at_4, 'out of ', len(data))
