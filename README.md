# Code of the IPython Cookbook, Second Edition (2018)

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/ipython-books/cookbook-2nd-code/master)

This repository contains the Jupyter notebooks of the 100+ recipes of [*IPython Interactive Computing and Visualization Cookbook, Second Edition (2018)*](https://www.packtpub.com/big-data-and-business-intelligence/ipython-interactive-computing-and-visualization-cookbook-second-e), by [Cyrille Rossant](http://cyrille.rossant.net), *Packt Publishing*.

This repository is read-only: the source files are on the [cookbook-2nd](https://github.com/ipython-books/cookbook-2nd) repository.


## Running the code in the cloud

With [Binder](https://mybinder.org/), you can run most of the Jupyter notebooks directly from your web browser without installing anything. Just click on the `launch binder` button above. A temporary Jupyter Notebook server with all dependencies will be automatically launched in the cloud. It is not persistent: all your changes will be lost after some time.


## Running the code on your computer

1. [**Install** git](https://git-scm.com/downloads).

2. [**Download and install** Anaconda](https://www.anaconda.com/download/): choose the **Python 3.6, 64-bit** version for your operating system (macOS, Linux, or Windows).

3. **Open** a terminal (`cmd` on Windows).

4. **Clone** the repository:

```bash
$ git clone https://github.com/ipython-books/cookbook-2nd-code.git
$ cd cookbook-2nd-code
```

5. **Create** the `cookbook` [conda environment](https://conda.io/docs/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file):

```bash
conda env create -f environment.yml
```

6. **Activate** the environment:

    * On macOS and Linux:

    ```bash
    source activate cookbook
    ```

    * On Windows:

    ```bash
    activate cookbook
    ```

7. **Launch** the [Jupyter Notebook](http://jupyter.org/install.html):

```bash
$ jupyter notebook
```
