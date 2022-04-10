class Anagram:
    def __init__(self):
        with open("../resources/fiveLetterWords.txt") as file:
            words = [line.rstrip() for line in file]
        self.__dict__ = {}
        for word in words:
            key = self.make_key_from(word)
            if key in self.__dict__:
                self.__dict__[key].append(word)
            else:
                self.__dict__[key] = [word]

    def make_key_from(self, word):
        return ''.join(sorted(word))

    def unjumble(self, anagram):
        return self.__dict__[self.make_key_from(anagram)]

if __name__ == '__main__':
    anagram = input("enter word to unscramble: ")
    words = Anagram().unjumble(anagram)
    for word in words:
        print(word)