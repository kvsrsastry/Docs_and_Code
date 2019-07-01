st = 'ganesh is the pratham pujya'
print(st.capitalize())
print(st.title())
print(st.center(100, '#'))
print(len(st))
print(st.split())
print('@'.join(st.split()))
print(f'I always start with {st * 2}') # f-strings are available from Python 3.6

if st.startswith('ganesh '):
    print('Yes .. string starts with "ganesh "')

if st.endswith(' pratham pujya'):
    print('Yes .. string ends with "pratham pujya"')

print(st.isnumeric())
print(st.islower())
print(st.isupper())
st = '7'
print(st.isdigit())
print(st.isdecimal()) # isdecimal is same as isnumeric
