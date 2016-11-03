# -*- coding: utf-8 -*-

"""Pygments lexer for SISAL.

SISAL stands for Streams and Iteration In A Single-Assignment Language.

"""


from pygments.lexer import RegexLexer, Text, words, bygroups, include, default
from pygments.token import Comment, Name, Keyword, Number, Operator, String

__version__ = '0.1.0'
__author__ = 'Alexander Asp Bock'
__license__ = 'MIT'


class SisalLexer(RegexLexer):
    """Lexer for the SISAL programming language."""

    name = 'sisal'
    aliases = ['sis', 'sisal']
    filenames = ['*.sis', '*.sisal']
    tokens = {
        'root': [
            (r'\n', Text),
            (r'\\\n', Text),
            (r'\\', Text),
            (r'(define)(\s+)(.+)', bygroups(Comment.Preproc, Text, Text)),
            (r'(global)(\s+)(.+)', bygroups(Comment.Preproc, Text, Text)),
            (r'^%\$', Comment.Directive, 'directive'),
            (r'% .+$', Comment.Singleline),
            (r'\'', String.Single, 'singlequoted_string'),
            (r'"', String.Double, 'doublequoted_string'),
            (r'(function)(\s+)(.+)(\()',
             bygroups(Keyword, Text, Name.Function, Text)),
            (r'error', Name.Exception),
            (r'\(|\)', Text),
            include('keywords'),
            include('conversions'),
            include('types'),
            include('builtins'),
            include('numbers'),
            include('operators'),
            include('conditionals'),
            include('loops'),
            (r'[^\S\n]+', Text),
            (r'\w+', Text)
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
                    # 'define',
                    'old',
                    'of',
                    'nil',
                    'in',
                    'end let',
                    'end function'],
                   prefix=r'\b',
                   suffix=r'\b'),
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
                   suffix=r'\b'),
             Keyword.Type)
        ],
        'builtins': [
            (words(['abs',  # Standard functions
                    'exp',
                    'mod',
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
                    'stream_prefixsize',
                    # Record functions
                    'replace'],
                   suffix=r'\b'),
             Name.Builtin),
        ],
        'conversions': [
            (r'(integer)(\()',     bygroups(Keyword.Reserved, Text)),
            (r'(real)(\()',        bygroups(Keyword.Reserved, Text)),
            (r'(double_real)(\()', bygroups(Keyword.Reserved, Text)),
            (r'(character)(\()',   bygroups(Keyword.Reserved, Text))
        ],
        'numbers': [
            (r'-?\d+\.\d+([eEdD][+-]?\d+)?', Number.Float),
            (r'-?\d+',                       Number.Integer)
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
            (':',    Operator),
            ('\[',   Operator),
            ('\]',   Operator),
            (',',    Operator),
            (';',    Operator)
        ],
        'conditionals': [
            (words(['if',
                    'then',
                    'elseif',
                    'else',
                    'end if'],
                   suffix=r'\b'),
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
                   suffix=r'\b'),
             Keyword)
        ],
        'singlequoted_string': [
            (r'[^\'\\]+', String.Single),
            (r'\\.',       String.Escape),
            (r'\'',        String.Single, '#pop')
        ],
        'doublequoted_string': [
            (r'[^"\\]+', String.Double),
            (r'\\.',      String.Escape),
            (r'"',        String.Double, '#pop')
        ],
        'directive': [
            (words(['INCLUDE', 'SUBRANGE', 'PACKED', 'MAIN']),
             Comment.PreProc),
            default('#pop')
        ]}
