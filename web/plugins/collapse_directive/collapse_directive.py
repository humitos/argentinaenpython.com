# -*- coding: utf-8 -*-

# Copyright © 2015 Manuel Kaufmann

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

from __future__ import unicode_literals

from docutils import nodes
from docutils.parsers.rst import Directive, directives

from nikola.plugin_categories import RestExtension


class Plugin(RestExtension):

    name = "collapse_directive"

    def set_site(self, site):
        self.site = site
        Collapse.site = site
        return super(Plugin, self).set_site(site)


class Collapse(Directive):
    """ Restructured text extension for inserting collapsible groups or accordion."""

    # TODO: http://www.tutorialspoint.com/bootstrap/bootstrap_collapse_plugin.htm
    option_spec = {
    }
    has_content = True
    required_arguments = 1  # title
    optional_arguments = 999

    def _sanitize_options(self):
        # TODO: validate options here and (maybe) display an error
        defaults = {}
        for option in defaults.keys():
            assert option in self.option_spec

        return defaults

    def run(self):
        if len(self.content) == 0:
            return

        # from nikola.plugins.compile.rest import rst2html
        # content = rst2html('\n'.join(self.content))

        # TODO: use nikola.plugins.compile.rest.rst2html to compile this
        import uuid
        from docutils.core import publish_parts
        content = publish_parts('\n'.join(self.content), writer_name='html')['html_body']

        output = self.site.template_system.render_template(
            'collapse.tmpl',
            None,
            {
                'uuid': uuid.uuid4().hex,
                'title': ' '.join(self.arguments),
                'content': content,
            }
        )
        return [nodes.raw('', output, format='html')]


directives.register_directive('collapse', Collapse)
