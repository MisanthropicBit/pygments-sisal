# pygments-sisal [![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/MisanthropicBit/vim-analog/master/LICENSE)

A [Pygments](http://pygments.org/) lexer for **S**treams and **I**teration In A
**S**ingle-**A**ssignment **L**anguage (SISAL).

![Example highlighting with the lovelace style](/screenshot_lovelace.png)

## Install

Either run `pip install pygments-sisal` or `git clone` this repository and run
`python setup.py install` from the commandline.

The setup script installs the necessary entry point for `pygments`. You can
verify the install by running:

```bash
pygmentize -L lexers | grep 'sisal'
```
