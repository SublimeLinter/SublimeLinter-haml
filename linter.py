from SublimeLinter.lint import RubyLinter


class Haml(RubyLinter):
    # haml has no check-only mode any more. `haml compile` prints the generated
    # Ruby code and always exits with status 0, but a template that does not
    # parse produces `raise Haml::SyntaxError.new(%q[message], line)` in that
    # code. The line is zero-based.
    cmd = 'haml compile -'
    regex = (
        r'^.*?raise Haml::SyntaxError\.new\(%q\[(?P<message>.*)\], (?P<line>\d+)\)'
    )
    line_col_base = (0, 0)
    defaults = {
        'selector': 'text.haml'
    }
