**IN PROGRESS**

This ReadMeDownloads.md will describe what packages are needed in order to successfully install and run pocketsphinx for Python code. 
Additionally, a lot of information related to this can be found at https://github.com/cmusphinx/.

Dependencies:
- python
- python-dev
- python-pip
- build-essential
- swig
- git
- libpulse-dev

Install:

```brew install -y python python-dev python-pip build-essential swig git libpulse-dev```

You will need SphinxBase, which is the support library required by Pocketsphinx and Sphinxtrain. This can be installed by running:

```brew install sphinxbase```

or by downloading it from http://cmusphinx.sourceforge.net. Download and unpack it to the same parent directory as PocketSphinx, so that the configure script and project files can find it.

After that, you can install Pocketsphinx and Pocketsphinx-python. Pocketsphinx is the recognizer itself, and Pocketsphinx-python is the wrapper that allows us to use Pocketsphinx in Python.

```brew install pocketsphinx```

```
git clone --recursive https://github.com/cmusphinx/pocketsphinx-python/
cd pocketsphinx-python
python setup.py install
```
Check out https://github.com/cmusphinx/pocketsphinx and https://github.com/cmusphinx/pocketsphinx-python for more information about those two downloads.
