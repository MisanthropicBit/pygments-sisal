# pygments-sisal [![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/MisanthropicBit/pygments-sisal/master/LICENSE)

A [Pygments](http://pygments.org/) lexer for **S**treams and **I**teration In A
**S**ingle-**A**ssignment **L**anguage (SISAL).

LaTeX screenshot (lovelace style):
![Example LaTeX highlighting with the lovelace style](/latex_screenshot.png)

Terminal screenshot (lovelace style):

<img src="/terminal_screenshot.png" alt="Example terminal highlighting with the lovelace style" width="478">
<!--![Example terminal highlighting with the lovelace style](/terminal_screenshot.png)-->

## Install

Either run `pip install pygments-sisal` or `git clone` this repository and run
`python setup.py install` from the command line.

The setup script installs the necessary entry point for `pygments`. You can
verify the install by running:

```bash
pygmentize -L lexers | grep 'sisal'
```
