s = """
for x in range(10):
    print(x, end='')
print()
"""
code_exec = compile(s, '<string>', 'exec')

code_eval = compile('10 + 20', '<string>', 'eval')
code_single = compile('name = input("Input Your Name: ")', '<string>', 'single')

a = exec(code_exec)
b = eval(code_eval)

c = exec(code_single)
d = eval(code_single)

print('a: ', a)
print('b: ', b)
print('c: ', c)
print('name: ', name)
print('d: ', d)
print('name; ', name)