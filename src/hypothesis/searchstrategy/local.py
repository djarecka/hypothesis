# coding=utf-8
#
# This file is part of Hypothesis, which may be found at
# https://github.com/HypothesisWorks/hypothesis-python
#
# Most of this work is copyright (C) 2013-2017 David R. MacIver
# (david@drmaciver.com), but it contains contributions by others. See
# CONTRIBUTING.rst for a full list of people who may hold copyright, and
# consult the git log if you need to determine who owns an individual
# contribution.
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file, You can
# obtain one at http://mozilla.org/MPL/2.0/.
#
# END HEADER

from __future__ import division, print_function, absolute_import

from hypothesis.searchstrategy import SearchStrategy
from hypothesis.internal.reflection import get_pretty_function_description


class DataWrapper(object):
    def __init__(self, data):
        self.draw = data.draw

    def __call__(self, strategy):
        return self.draw(strategy)


class LocalSearchStrategy(SearchStrategy):
    def __init__(self, definition):
        self.definition = definition

    def __repr__(self):
        return "local(%s)" % (
            get_pretty_function_description(self.definition),)

    def do_draw(self, data):
        return self.definition(DataWrapper(data))
