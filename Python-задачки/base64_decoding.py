import base64

text1 = 'LHQu9CwLdCx0LvQsCAK0L/QsNGA0L7Qu9GMINC+0YIg0LDRgNGF0LjQstCwIFZqa2psdHdEajNtdmJDR3R4cmJHYmhqO2py'

text2 = 'UEsDBBQACQAIAEiIT0xujSeMdwAAAHQAAAALABwAd2VsY29tZS50e' \
        'HRVVAkAA+iShVr8koVadXgLAAEE6AMAAAToAwAAPpowfjGE59Cr4GvIf' \
        '7bgd/cNXEVmbF62ajB1ewKWreExErJyjpZSbBEohQxrneurmUwmpa0T3A' \
        'aVfJD7ZFq51DV9+hiISDDPswsd8DtnKURzJuIGNX5arykNO4pFFK9xJm/ITns' \
        'DgZxNsqEs5nMvvLWBjA4Wvt9QSwcIbo0njHcAAAB0AAAAUEsBAh4DFAA' \
        'JAAgASIhPTG6NJ4x3AAAAdAAAAAsAGAAAAAAAAQAAAKSBAAAAAHdlb' \
        'GNvbWUudHh0VVQFAAPokoVadXgLAAEE6AMAAAToAwAAUEsFBgAAAAA' \
        'BAAEAUQAAAMwAAAAAAA=='

# --- Настройки здесь --------------
base64_message = text2
# ----------------------------------

message_encoding = ['UTF-8', 'ASCII', 'Windows-1252', 'ISO-8859-1', 'ISO-8859-2', 'ISO-8859-6', 'ISO-8859-15',
                    'ArmSCII-8', 'BIG-5', 'CP850', 'CP866', 'CP932', 'CP936', 'CP950', 'CP50220', 'CP50221',
                    'CP50222', 'CP51932', 'EUC-CN', 'EUC-JP', 'EUC-KR', 'EUC-TW', 'GB18030', 'HZ', 'ISO-2022-JP',
                    'ISO-2022-KR', 'ISO-8859-4', 'ISO-8859-7', 'ISO-8859-8', 'ISO-8859-9', 'ISO-8859-10',
                    'ISO-8859-13', 'ISO-8859-14', 'ISO-8859-16', 'JIS', 'KOI8-R', 'KOI8-U', 'SJIS', 'UCS-2',
                    'UCS-2BE', 'UCS-2LE', 'UCS-4', 'UCS-4BE', 'UCS-4LE', 'UHC', 'UTF-7', 'UTF-16', 'UTF-16BE',
                    'UTF-16LE', 'UTF-32', 'UTF-32BE', 'UTF-32LE', 'UTF7-IMAP', 'Windows-1251', 'Windows-1254']

print('Исходное сообщение:\n', base64_message)

# Если количество символово не кратно 4, то дописываем вперёд нули
if len(base64_message) % 4 != 0:
    base64_message = '0' * (4 - (len(base64_message) % 4)) + base64_message

# Standard Base64 Decoding
for coding in message_encoding:
    try:
        message_bytes = base64.b64decode(base64_message.encode(coding))
        message = str(message_bytes, coding)
    except:
        pass
    try:
        print('\nКодировка', coding, ':')
        print(message)
    except:
        print('Это не', coding, '.')
