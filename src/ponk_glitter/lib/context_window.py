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


class GPTContextWindow(ContextWindow):
    """
    This class inherits from ContextWindow. It produces overlapping blocks of tokenized text.
    Window is tuple where first element is amount of relevant tokens from the end of window and second is the window.
    """

    def __init__(self, tokenized_text: [int], size: int):
        super().__init__(tokenized_text, size)
        self.tokenized_text: [int] = tokenized_text
        self.size: int = size
        self.index: int = 0
        self.end_reached: bool = False

    def __get_window__(self, index: int):
        # first window
        if self.index == 0:
            if self.size >= len(self.tokenized_text):
                self.end_reached = True
                return len(self.tokenized_text), self.tokenized_text
            return self.size, self.tokenized_text[0: self.size]

        # last window containing context length of self.size
        elif self.size + (self.index * (self.size // 2)) >= len(self.tokenized_text):
            self.end_reached = True
            end_i = self.size + (self.index - 1) * (self.size // 2)
            return len(self.tokenized_text) - end_i, self.tokenized_text[-self.size:]

        # window containing context length of self.size overlapping with the previous window
        window_start = self.index * (self.size // 2)
        if window_start + self.size >= len(self.tokenized_text):
            self.end_reached = True
        return self.size // 2, self.tokenized_text[window_start: window_start + self.size]

    def __iter__(self):
        return self

    def __next__(self):
        if self.end_reached:
            raise StopIteration
        window = self.__get_window__(self.index)
        self.index += 1
        return window

    def __len__(self):
        # TODO: This is slow, find a better way to calculate the length
        output = 0
        for _ in GPTContextWindow(self.tokenized_text, self.size):
            output += 1
        return output

    def __getitem__(self, index):
        return self.__get_window__(index)

    def __repr__(self):
        return repr(self.tokenized_text)
