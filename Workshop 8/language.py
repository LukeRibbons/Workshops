from ProgrammingLanguage import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
vb = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
languages = [""]*3
languages[0] = ruby
languages[1] = python
languages[2] = vb

print("The dynamically typed languages are:")
for x in range(len(languages)):
    if languages[x].is_dynamic():
        print(languages[x].name)
