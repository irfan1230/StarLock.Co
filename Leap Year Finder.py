year = int(input('Type the Year :- '))
if year % 4 != 0 :
    print('Sorry',year ,'is Not a leap year')
elif year % 100  != 0:
    print('wow',year, 'is Leap year')
elif year % 400==0:
    print('wow',year,'is Leap year')
elif year % 400 != 0:
    print('Sorry',year, 'is Not a leap year')
  