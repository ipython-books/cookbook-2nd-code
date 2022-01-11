
from traitlets import Int, Float, Unicode, Bool
from IPython.core.magic import (Magics, magics_class,
                                line_magic)
import numpy as np

@magics_class
class RandomMagics(Magics):
    text = Unicode(u'{n}', config=True)
    max = Int(1000, config=True)
    seed = Int(0, config=True)

    def __init__(self, shell):
        super(RandomMagics, self).__init__(shell)
        self._rng = np.random.RandomState(
            self.seed or None)

    @line_magic
    def random(self, line):
        return self.text.format(
            n=self._rng.randint(self.max))

def load_ipython_extension(ipython):
    ipython.register_magics(RandomMagics)
