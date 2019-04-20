import sys
import CARE.CARE_Parse as parse

print("Welcome to CARE")
print("")

while True:
    try:
        s = input('CARE >>')

    except EOFError:
        break
    print("")
    parse.do_parse(s)
    print("")

