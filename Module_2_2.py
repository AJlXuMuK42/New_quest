first=123
second=122
third=124
if first==second==third:
    print('3')
elif first==second or second==third or first==third:
    print('2')
elif first!=second!=third:
    print('0')


