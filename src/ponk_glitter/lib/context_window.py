class ContextWindow:
    """
    This class is a generator that takes a text and a window size as input and 
    returns a window of words of the given size. It starts with window of size 1
    and it grows to defined size.
    """

    def __init__(self, text: str, size: int):
        self.text = text.strip().split()
        self.size = size
        self.index = 0

    def __get_window__(self, index: int):
        if self.index < self.size:
            return self.text[0: index]
        else:
            return self.text[self.index - self.size: index]

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.text):
            raise StopIteration
        window = self.__get_window__(self.index)
        self.index += 1
        return window

    def __len__(self):
        return len(self.text) - 1  # nejsem si jistej tou -1

    def __getitem__(self, index):
        return self.__get_window__(index)

    def __repr__(self):
        return repr(self.text)


class MaskedContextWindow(ContextWindow):

    def __init__(self, text: str, size: int, mask: str = "[MASK]"):
        super().__init__(text, size)
        self.mask = mask

    def __iter__(self):
        return self

    def __next__(self):
        window = super().__next__()
        return " ".join(window) + " " + self.mask

    def __len__(self):
        return super().__len__()

    def __getitem__(self, index):
        return super().__get_window__(index)

    def __repr__(self):
        return repr(self.mask)
