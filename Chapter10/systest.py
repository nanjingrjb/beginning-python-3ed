import sys
args = sys.argv[1:]
t=args.reverse()
print('t:',t)
print('final1:',' '.join(args))
print('args:',args)
#reversed()对某个列表进行操作，返回一个对象
#而字符串操作是可以join对象的。
vs=reversed(args)
print('vs:',vs)
print('final:',' '.join(vs))

