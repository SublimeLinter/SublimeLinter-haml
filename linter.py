from SublimeLinter.lint import RubyLinter, util


class Haml(RubyLinter):
    cmd = 'haml -c --stdin'
    regex = r'^(?:Syntax error on line (?P<line>\d+):|.+?[^:]:) (?P<message>.+)'
    error_stream = util.STREAM_STDERR
    defaults = {
        'selector': 'text.haml'
    }

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
