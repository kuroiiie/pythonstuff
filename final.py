#name = input('Please enter a sentence: ')
#print('Your sentence has',len(name),'characters')
def foo(a, b):
 print('in foo()')
 return a+b
# end foo
def bar(a, b):
 print('in bar()')
 return a*b
# end bar
# -- main----------------------------------------------------
x = 'aa'
y = 'bbb'
z = 4
s = 'foo({0},{1})={2}'.format(x,y,foo(x,y))
t = 'bar({0},{1})={2}'.format(z,y,bar(z,y))
u = 'foo(bar({0},{1}),{2})={3}'.format(z,x,y,foo(bar(z,x),y))
print(s)
print(t)