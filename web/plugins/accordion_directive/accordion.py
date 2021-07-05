# -*- coding: utf-8 -*-

# Copyright © 2015 Manuel Kaufmann & Leandro E. Colombo Viña

# Permission is hereby granted, free of charge, to any
# person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the
# Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the
# Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice
# shall be included in all copies or substantial portions of
# the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY
# KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
# PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS
# OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import uuid

from docutils import nodes
from docutils.parsers.rst import Directive, directives

from nikola.plugin_categories import RestExtension

"""Accordion and Collapse group directive for reStructuredText"""


class Plugin(RestExtension):
    """Plugin for accordion and collapse reST directive"""

    name = "accordion"

    def set_site(self, site):
        """Set Nikola site."""
        self.site = site
        directives.register_directive('accordion', Accordion)
        return super(Plugin, self).set_site(site)


class Accordion(Directive):
    """ reStructuredText extension for inserting collapsible groups or accordion."""

    required_arguments = 0
    optional_arguments = 9999
    final_argument_whitespace = False
    option_spec = {
        'class': directives.class_option,
        'id': directives.unchanged,
        'role': directives.unchanged,
        'aria-multiselectable': directives.unchanged,
        }

    has_content = True

    def run(self):
        self.assert_has_content()
        text = '\n'.join(self.content)
        options = {
            'class': self.arguments[0] if self.arguments else 'panel-group',
            'id': 'accordion',
            'role': 'tablist',
            'aria-multiselectable': 'true'
        }
        options.update(self.options)

        node = nodes.container(text)
        node['classes'] = directives.class_option(options['class'])
        self.add_name(node)
        self.state.nested_parse(self.content, self.content_offset, node)

        return [node]
