import cgen as C
test = C.cgen('test.c')
test.code.append(C.sysinclude('stdio.h'))
test.code.append(C.blank())
test.code.append(C.function('main', 'void',).add_param(C.variable('', '')))
body = C.block(innerIndent=3)
body.append(C.statement(C.variable('num1, num2', 'int')))
body.append(C.statement(C.fcall('printf').add_arg(r'"Enter two numbers:\n"')))
body.append(C.statement(C.fcall('scanf').add_arg(r'"%d %d"').add_arg(r'&num1').add_arg(r'&num2')))
body.append(C.statement('return 0'))
test.code.append(body)
print(str(test))