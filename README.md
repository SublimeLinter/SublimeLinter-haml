SublimeLinter-haml
=========================

[![Build Status](https://travis-ci.org/SublimeLinter/SublimeLinter-haml.svg?branch=master)](https://travis-ci.org/SublimeLinter/SublimeLinter-haml)

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) provides an interface to [haml](http://haml.info). It will be used with files that have the “Ruby Haml” syntax.

## Installation
SublimeLinter must be installed in order to use this plugin. 

Please use [Package Control](https://packagecontrol.io) to install the linter plugin.

Before using this plugin, you must ensure that `haml` (4.0.0 or later) is installed on your system. To install `haml`, do the following:

1. Install [Ruby](http://www.ruby-lang.org).

1. Install `haml` by typing the following in a terminal:
   ```
   [sudo] gem install haml
   ```

1. If you are using `rbenv` or `rvm`, ensure that they are loaded in your shell’s correct startup file. See [here](http://sublimelinter.readthedocs.org/en/latest/troubleshooting.html#shell-startup-files) for more information.

In order for `haml` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. The docs cover [troubleshooting PATH configuration](http://sublimelinter.readthedocs.io/en/latest/troubleshooting.html#finding-a-linter-executable).


## Settings
- SublimeLinter settings: http://sublimelinter.readthedocs.org/en/latest/settings.html
- Linter settings: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html
