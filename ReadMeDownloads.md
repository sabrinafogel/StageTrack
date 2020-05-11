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

```brew install pocketsphinx```


You will need SphinxBase, which is the support library required by Pocketsphinx and Sphinxtrain. This can be installed by running:

```brew install sphinxbase```

or by downloading it from http://cmusphinx.sourceforge.net. Download and unpack it to the same parent directory as PocketSphinx, so that the configure script and project files can find it.

