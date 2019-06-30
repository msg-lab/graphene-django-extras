# -*- coding: utf-8 -*-
from graphql.type.directives import specified_directives as default_directives

from .date import *
from .list import *
from .numbers import *
from .string import *

all_directives = (
    # date
    DateGraphQLDirective,
    # list
    ShuffleGraphQLDirective,
    SampleGraphQLDirective,
    # numbers
    FloorGraphQLDirective,
    CeilGraphQLDirective,
    # string
    DefaultGraphQLDirective,
    Base64GraphQLDirective,
    NumberGraphQLDirective,
    CurrencyGraphQLDirective,
    LowercaseGraphQLDirective,
    UppercaseGraphQLDirective,
    CapitalizeGraphQLDirective,
    CamelCaseGraphQLDirective,
    SnakeCaseGraphQLDirective,
    KebabCaseGraphQLDirective,
    SwapCaseGraphQLDirective,
    StripGraphQLDirective,
    TitleCaseGraphQLDirective,
    CenterGraphQLDirective,
    ReplaceGraphQLDirective,
)


all_directives = [d() for d in all_directives] + default_directives
