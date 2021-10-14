class TextWork:
    def __init__(self):
        self.__text = str()

    @property
    def text(self):
        return self.__text

    def read_file(self, path: str):
        with open(path, 'r') as file:
            self.__text = file.read()

    def write_file(self, path: str):
        with open(path, 'w') as file:
            file.write(self.__text)

    def invert_case(self):
        self.__text = ''.join(c.lower() if c.isupper() else c.upper() for c in self.__text)

    def replace_punctuation_to_star(self):
        punctuation_characters = ('.', ',', ';', ':', '!', '?', '"', "'", '(', ')', '-', '`')
        result_str = str()
        for i in range(len(self.__text)):
            if self.__text[i] in punctuation_characters:
                result_str += '*'
            else:
                result_str += self.__text[i]
        self.__text = result_str


if __name__ == '__main__':
    o = TextWork()
    o.read_file('in.txt')
    print(o.text)
    o.invert_case()
    print(o.text)
    o.replace_punctuation_to_star()
    print(o.text)
    o.write_file('out.txt')
