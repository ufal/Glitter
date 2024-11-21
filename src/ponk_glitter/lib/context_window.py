from torch import tensor

class ContextWindow:
    """
    This class is a generator that takes a text and a window size as input and
    returns a window of words of the given size. It starts with window of size 1,
    and it grows to defined size.
    """

    def __init__(self, tokenized_text: [str], size: int):
        self.tokenized_text = tokenized_text
        self.size = size
        self.index = 1

    def __get_window__(self, index: int):
        if self.index < self.size:
            return self.tokenized_text[0: index]
        else:
            return self.tokenized_text[self.index - self.size: index]

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.tokenized_text):
            raise StopIteration
        window = self.__get_window__(self.index)
        self.index += 1
        return window

    def __len__(self):
        return len(self.tokenized_text) - 1  # nejsem si jistej tou -1

    def __getitem__(self, index):
        return self.__get_window__(index)

    def __repr__(self):
        return repr(self.tokenized_text)


class MaskedContextWindow(ContextWindow):
    """
    This class inherits from ContextWindow. The difference is that it appends a mask token
    to the end of the window.
    """

    def __init__(self, tokenized_text: str, size: int, mask: str = "[MASK]"):
        super().__init__(tokenized_text, size)
        self.mask = mask

    def __iter__(self):
        return self

    def __next__(self):
        window = super().__next__()
        window.append(self.mask)

    def __len__(self):
        return super().__len__()

    def __getitem__(self, index):
        return super().__get_window__(index)

    def __repr__(self):
        return repr(self.mask)


class TokenizedContextWindow(ContextWindow):
    """
    This class inherits from ContextWindow. The difference is that it works on to
    tokenized text (list of integers).
    """

    def __init__(self, tokenized_text: [int], size: int):
        super().__init__(tokenized_text, size)
        self.tokenized_text: [int] = tokenized_text
        self.size: int = size
        self.index: int = 1
    
    def __create_output__(self, window: [int]):
        return {"input_ids": window.unsqueeze(0), "attention_mask": tensor([[1] * (len(window))])}

    def __get_window__(self, index: int):
        if self.index < self.size:
            window = self.tokenized_text[0: index]
            return self.__create_output__(window)
        else:
            window = self.tokenized_text[self.index - self.size: index]
            return self.__create_output__(window)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.tokenized_text):
            raise StopIteration
        window = self.__get_window__(self.index)
        self.index += 1
        return window

    def __len__(self):
        return len(self.tokenized_text)

    def __getitem__(self, index):
        return self.__get_window__(index)

    def __repr__(self):
        return repr(self.tokenized_text)


class TokenizedMaskedContextWindow(TokenizedContextWindow):
    """
    This class inherits from ContextWindow. The difference is that it works on to 
    tokenized text (list of integers). It appends a mask token to the end of the window.
    """

    def __init__(self, tokenized_text: [int], size: int, mask_token: int = 103):
        super().__init__(tokenized_text, size)
        self.tokenized_text: [int] = tokenized_text
        self.size: int = size
        self.index: int = 0
        self.mask_token: int = mask_token

    def __create_output__(self, window: [int]):
        return {"input_ids": window, "attention_mask": [1] * (len(window))}

    def __get_window__(self, index: int):
        if self.index < self.size:
            window = self.tokenized_text[0: index] + [self.mask_token]
            return self.__create_output__(window)
        else:
            window = self.tokenized_text[self.index - self.size: index] + [self.mask_token]
            return self.__create_output__(window)

