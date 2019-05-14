from CARE import care_parse

print("Welcome to CARE")
print("")

while True:
    try:
        s = input('CARE >> ')

    except EOFError:
        break
    print("")
    care_parse.do_parse(s)
    print("")

