#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Aparajita Fishman
# Copyright (c) 2013 Aparajita Fishman
#
# License: MIT
#

"""This module exports the Haml plugin class."""

from SublimeLinter.lint import RubyLinter, util


class Haml(RubyLinter):

    """Provides an interface to haml."""

    syntax = 'ruby haml'
    cmd = 'haml -c --stdin'
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 4.0'
    regex = r'^(?:Syntax error on line (?P<line>\d+):|.+?[^:]:) (?P<message>.+)'
    error_stream = util.STREAM_STDERR

    def split_match(self, match):
        """
        Return the components of the match.

        We override this to set the line/col to 0, 0 if a linter error occurs
        and there is no line number.

        """

        match, line, col, error, warning, message, near = super().split_match(match)

        if line is None:
            line = col = 0

        return match, line, col, error, warning, message, near
