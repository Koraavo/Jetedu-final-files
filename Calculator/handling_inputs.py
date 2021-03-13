# string_input = '3 + 8 * ((42 + 3) * 2 + 1) - 6 / (2 + 1)'
# string_input = '1 +++ 2 * 3 --- 4 - 2'
string_input = '33 + 20 + 11 + 49 - 32 - 9 + 1 - 80 + 4'
out = ''.join(string_input.split())
while '++' in out:
    out = out.replace('++', '+')
while '---' in out:
    out = out.replace('---', '-')
while '--' in out:
    out = out.replace('--', '+')

if '+' in out:
    out = out.replace('+', ' + ')
if '-' in out:
    out = out.replace('-', ' - ')
if '*' in out:
    out = out.replace('*', ' * ')
if '/' in out:
    out = out.replace('/', ' / ')
if '(' in out:
    out = out.replace('(', ' ( ')
if ')' in out:
    out = out.replace(')', ' ) ')
else:
    out = out
out = out.replace('  ', ' ')
print(out)