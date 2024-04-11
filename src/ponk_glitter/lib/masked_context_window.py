from context_window import ContextWindow


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

