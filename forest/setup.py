from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

extensions = [
    Extension("libtree",
              [
                  "libtree.pyx",
                  "../tree/classifier.c",
                  "../tree/dataset.c",
                  "../tree/dictionary.c",
                  "../tree/visualizer.c",
                  "../tree/criterions.c",
                  "../tree/node.c",
                  "../random/random.c",
                  "../error/error.c"
              ]
              )
]

setup(ext_modules=cythonize(extensions))
