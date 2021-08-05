text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb " \
       "rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj "

result = []
for ch in text:
    result.append(chr(ord(ch) + 2))
text = ''.join(result)
print(text, '\n', '-' * 45)

text = text.replace('"', ' ')
text = text.replace('{', 'a')
text = text.replace('|', 'b')
text = text.replace('0', ',')
text = text.replace(')', '\'')
text = text.replace('*', '(')
text = text.replace('+', ')')
text = text.replace(',', '.')
print(text)
