
from ipykernel.kernelbase import Kernel
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import urllib, base64

def _to_png(fig):
    """Return a base64-encoded PNG from a
    matplotlib figure."""
    imgdata = BytesIO()
    fig.savefig(imgdata, format='png')
    imgdata.seek(0)
    return urllib.parse.quote(
        base64.b64encode(imgdata.getvalue()))

_numpy_namespace = {n: getattr(np, n)
                    for n in dir(np)}
def _parse_function(code):
    """Return a NumPy function from a
    string 'y=f(x)'."""
    return lambda x: eval(code.split('=')[1].strip(),
                          _numpy_namespace, {'x': x})

class PlotKernel(Kernel):
    implementation = 'Plot'
    implementation_version = '1.0'
    language = 'python'  # will be used for
                         # syntax highlighting
    language_version = '3.6'
    language_info = {'name': 'plotter',
                     'mimetype': 'text/plain',
                     'extension': '.py'}
    banner = "Simple plotting"

    def do_execute(self, code, silent,
                   store_history=True,
                   user_expressions=None,
                   allow_stdin=False):

        # We create the plot with matplotlib.
        fig, ax = plt.subplots(1, 1, figsize=(6,4),
                               dpi=100)
        x = np.linspace(-5., 5., 200)
        functions = code.split('\n')
        for fun in functions:
            f = _parse_function(fun)
            y = f(x)
            ax.plot(x, y)
        ax.set_xlim(-5, 5)

        # We create a PNG out of this plot.
        png = _to_png(fig)

        if not silent:
            # We send the standard output to the
            # client.
            self.send_response(
                self.iopub_socket,
                'stream', {
                    'name': 'stdout',
                    'data': ('Plotting {n} '
                             'function(s)'). \
                            format(n=len(functions))})

            # We prepare the response with our rich
            # data (the plot).
            content = {
                'source': 'kernel',

                # This dictionary may contain
                # different MIME representations of
                # the output.
                'data': {
                    'image/png': png
                },

                # We can specify the image size
                # in the metadata field.
                'metadata' : {
                      'image/png' : {
                        'width': 600,
                        'height': 400
                      }
                    }
            }

            # We send the display_data message with
            # the contents.
            self.send_response(self.iopub_socket,
                'display_data', content)

        # We return the exection results.
        return {'status': 'ok',
                'execution_count':
                    self.execution_count,
                'payload': [],
                'user_expressions': {},
               }

if __name__ == '__main__':
    from ipykernel.kernelapp import IPKernelApp
    IPKernelApp.launch_instance(
        kernel_class=PlotKernel)

class PlotKernel(Kernel):
    implementation = 'Plot'
    implementation_version = '1.0'
    language = 'python'  # will be used for
                         # syntax highlighting
    language_version = '3.6'
    language_info = {'name': 'plotter',
                     'mimetype': 'text/plain',
                     'extension': '.py'}
    banner = "Simple plotting"

    def do_execute(self, code, silent,
                   store_history=True,
                   user_expressions=None,
                   allow_stdin=False):

        # We create the plot with matplotlib.
        fig, ax = plt.subplots(1, 1, figsize=(6,4),
                               dpi=100)
        x = np.linspace(-5., 5., 200)
        functions = code.split('\n')
        for fun in functions:
            f = _parse_function(fun)
            y = f(x)
            ax.plot(x, y)
        ax.set_xlim(-5, 5)

        # We create a PNG out of this plot.
        png = _to_png(fig)

        if not silent:
            # We send the standard output to the
            # client.
            self.send_response(
                self.iopub_socket,
                'stream', {
                    'name': 'stdout',
                    'data': ('Plotting {n} '
                             'function(s)'). \
                            format(n=len(functions))})

            # We prepare the response with our rich
            # data (the plot).
            content = {
                'source': 'kernel',

                # This dictionary may contain
                # different MIME representations of
                # the output.
                'data': {
                    'image/png': png
                },

                # We can specify the image size
                # in the metadata field.
                'metadata' : {
                      'image/png' : {
                        'width': 600,
                        'height': 400
                      }
                    }
            }

            # We send the display_data message with
            # the contents.
            self.send_response(self.iopub_socket,
                'display_data', content)

        # We return the exection results.
        return {'status': 'ok',
                'execution_count':
                    self.execution_count,
                'payload': [],
                'user_expressions': {},
               }

if __name__ == '__main__':
    from ipykernel.kernelapp import IPKernelApp
    IPKernelApp.launch_instance(
        kernel_class=PlotKernel)
