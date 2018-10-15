x = 5

if x > 2:
    print('Bigger than 2')
    print('Still bigger')
print('Done with 2')

for i in range(5):
    print(i)
    if i > 2:
        print('Bigger than 2')
    print('Done with i',i)
print('All Done')

x = 42
if x > 1:
    print('More than one')
    if x < 100:
        print('Less than 100')
    print('All done')
x = 20
if x > 2:
    print('Bigger')
else:
    print('Smaller')

    print('All done')

if x < 2:
    print('small')
elif x < 10:
    print('Medium')
else:
    print('Large')
print('All done')

#No else
x = 12
if x < 2:
    print('Small')
elif x < 10:
    print('Medium')
elif x < 20:
    print('Big')
elif x < 40:
    print('Large')
elif x < 100:
    print('Huge')
else:
    print('your mom')

print ('All done')

x = 2
if x < 2:
    print('Below 2')
elif x >= 2:
    print('Two or more')
else:
    print('Something else')
