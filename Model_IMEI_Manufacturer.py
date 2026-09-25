
import re

parcel = """
Result: Parcel(
  0x00000000: 00000000 0000000f 00310030 00310030 '........0.1.0.1.'
  0x00000010: 00380033 00320030 00390036 00320033 '3.8.0.2.6.9.3.2.'
  0x00000020: 00350039 00000030                   '9.5.0...        ')
"""


def parse_imei(text):
    result = ""

    # ចាប់ 0030 - 0039 ទាំងអស់
    codes = re.findall(r'003[0-9]', text)

    for code in codes:
        number = int(code, 16)

        if 0x30 <= number <= 0x39:
            result += chr(number)

    return result


imei = parse_imei(parcel)

print("IMEI:", imei)
