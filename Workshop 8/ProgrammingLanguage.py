class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        """ initialise a ProgrammingLanguage instance
        name: string, name of the language
        typing: string, whether the language is static or dynamic
        reflection: string, yes or no on reflection
        year: integer, year the language first appeared """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """ is the typing dynamic"""
        if self.typing == "Dynamic":
            return True
        else:
            return False

    def __str__(self):
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.name, self.typing, self.reflection,
                                                                           self.year)
