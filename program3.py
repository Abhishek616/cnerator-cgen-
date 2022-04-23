import cgen as C
test = C.cgen('test.c')
test.code.append(C.sysinclude('stdio.h'))
test.code.append(C.blank())
test.code.append(C.function('main', 'void',).add_param(C.variable('', '')))
body = C.block(innerIndent=3)
body.append(C.statement(C.variable('i', 'int')))
body.append(C.line(C.fcall('for').add_arg(r'i = 1; i < 11; ++i')))
body1 = C.block(innerIndent=3)
body1.append(C.statement(C.fcall('printf').add_arg(r'"%d"').add_arg(r'i')))
body.code.append(body1)
test.code.append(body)
print(str(test))