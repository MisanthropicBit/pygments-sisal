# -*- coding: utf-8 -*-

"""Pygments lexer for SISAL.

SISAL stands for Streams and Iteration In A Single-Assignment Language.

"""


from pygments.lexer import RegexLexer, Text, words, bygroups, include
from pygments.token import Comment, Name, Keyword, Number, Operator, String

__version__ = '0.1.0'
__author__ = 'Alexander Asp Bock'
__license__ = 'MIT'


class SisalLexer(RegexLexer):
    """Lexer for the SISAL programming language."""

    name = 'sisal'
    aliases = ['sis']
    filenames = ['*.sis', '*.sisal']
    tokens = {
        'root': [
            ('(define) (.+)', bygroups(Keyword.Namespace, Text)),
            ('(global) (.+)', bygroups(Keyword.Namespace, Text)),
            ('% .+$', Comment.Singleline),
            ('^%$ .+$', Comment.Directive, 'directive'),
            ('\'', String.Single, 'singlequoted_string'),
            ('"', String.Double, 'doublequoted_string'),
            ('(function) (.+?)\(', bygroups(Keyword, Name.Function)),
            ('error\b', Name.Exception),
            include('keywords'),
            include('types'),
            include('builtins'),
            include('conversions'),
            include('numbers'),
            include('operators'),
            include('conditionals'),
            include('loops')
        ],
        'keywords': [
            (words(['sum',
                    'product',
                    'greatest',
                    'least',
                    'catenate',
                    'let',
                    'is',
                    'tagcase',
                    'otherwise',
                    'type',
                    'returns',
                    'forward',
                    'define',
                    'old',
                    'of',
                    'nil',
                    'in',
                    'end let'],
                   suffix='\b'),
             Keyword.Reserved)
        ],
        'types': [
            (words(['integer',
                    'real',
                    'double_real',
                    'character',
                    'null',
                    'boolean',
                    'array',
                    'stream',
                    'record',
                    'union'],
                   suffix='\b'),
             Keyword.Type)
        ],
        'builtins': [
            ('sum',  # Standard functions
             'product',
             'greatest',
             'least',
             'catenate',
             'floor',
             'trunc',
             'max',
             'min',
             # Array functions
             'array_fill',
             'array_limh',
             'array_liml',
             'array_size',
             'array_prefixsize',
             'array_adjust',
             'array_addh',
             'array_addl',
             'array_remh',
             'array_reml',
             'array_setl',
             # Stream functions
             'stream_append',
             'stream_first',
             'stream_rest',
             'stream_empty',
             'stream_size',
             'stream_prefixsize'
             # Record functions
             'replace', Name.Builtin)
        ],
        'conversions': [
            ('(integer)(\()',     bygroups(Keyword.Reserved, Text)),
            ('(real)(\()',        bygroups(Keyword.Reserved, Text)),
            ('(double_real)(\()', bygroups(Keyword.Reserved, Text)),
            ('(character)(\()',   bygroups(Keyword.Reserved, Text))
        ],
        'numbers': [
            ('-?\d+', Number.Integer),
            ('-?\d+\.\d+([eE][+-]*\d+)?', Number.Float),
            ('-?\d+\.\d+([dD][+-]*\d+)?', Number.Float)
        ],
        'operators': [
            ('\*',   Operator),
            ('\/',   Operator),
            ('\+',   Operator),
            ('-',    Operator),
            ('\|\|', Operator),
            ('~',    Operator),
            ('&',    Operator),
            ('=',    Operator),
            ('~=',   Operator),
            ('<',    Operator),
            ('>',    Operator),
            ('<=',   Operator),
            ('>=',   Operator),
            (':=',   Operator),
        ],
        'conditionals': [
            (words(['if',
                    'then',
                    'elseif',
                    'else',
                    'end if'],
                   suffix='\b'),
             Keyword)
        ],
        'loops': [
            (words(['for',
                    'while',
                    'initial',
                    'repeat',
                    'until',
                    'when',
                    'dot',
                    'cross',
                    'left',
                    'right',
                    'tree',
                    'end for'],
                   suffix='\b'),
             Keyword)
        ],
        'singlequoted_string': [
            ('[^\'\\]+', String.Single)
            ('\\.',      String.Escape),
            ('\'',       String.Single, '#pop'),
        ],
        'doublequoted_string': [
            ('[^"\\]+', String.Double)
            ('\\.',     String.Escape),
            ('"',       String.Double, '#pop'),
        ],
        'directive': [
            (words(['INCLUDE', 'SUBRANGE', 'PACKED', 'MAIN']), '?'),
            ('\n', '#pop')
        ]}
