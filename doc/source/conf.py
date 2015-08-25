# -*- coding: utf-8 -*-
#
# pypet documentation build configuration file, created by
# sphinx-quickstart on Wed Sep  4 12:12:59 2013.
#
# This file is execfile()d with the current directory f_set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath('.'))
sys.path.append(os.path.abspath('../../'))

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.autosummary','sphinx.ext.autodoc', 'sphinx.ext.doctest',
              'sphinx.ext.coverage', 'sphinx.ext.viewcode', 'sphinx.ext.pngmath']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# Autogenerate stubs
#autosummary_generate = True

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'pypet'
copyright = u'2013, Robert Meyer'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '0.1'
# The full version, including alpha/beta/rc tags.
release = '0.1.0'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you f_set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['cookbook/concept.rst',
                    'other/to_new_tree.rst',
                    'contact_license.rst']

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
# try:
#     import sphinx_rtd_theme
#
#     html_theme = "sphinx_rtd_theme"
#
#     html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
# except ImportError:
html_theme = 'agogo'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
css_gradient = '''background: rgb(23,49,119); /* Old browsers */
background: -moz-linear-gradient(top, rgba(23,49,119,1) 0%, rgba(32,124,202,1) 65%, rgba(41,137,216,1) 82%, rgba(125,185,232,1) 100%); /* FF3.6+ */
background: -webkit-gradient(linear, left top, left bottom, color-stop(0%,rgba(23,49,119,1)), color-stop(65%,rgba(32,124,202,1)), color-stop(82%,rgba(41,137,216,1)), color-stop(100%,rgba(125,185,232,1))); /* Chrome,Safari4+ */
background: -webkit-linear-gradient(top, rgba(23,49,119,1) 0%,rgba(32,124,202,1) 65%,rgba(41,137,216,1) 82%,rgba(125,185,232,1) 100%); /* Chrome10+,Safari5.1+ */
background: -o-linear-gradient(top, rgba(23,49,119,1) 0%,rgba(32,124,202,1) 65%,rgba(41,137,216,1) 82%,rgba(125,185,232,1) 100%); /* Opera 11.10+ */
background: -ms-linear-gradient(top, rgba(23,49,119,1) 0%,rgba(32,124,202,1) 65%,rgba(41,137,216,1) 82%,rgba(125,185,232,1) 100%); /* IE10+ */
background: linear-gradient(to bottom, rgba(23,49,119,1) 0%,rgba(32,124,202,1) 65%,rgba(41,137,216,1) 82%,rgba(125,185,232,1) 100%); /* W3C */
filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#173177', endColorstr='#7db9e8',GradientType=0 ); /* IE6-9 */'''

html_theme_options = {'documentwidth': '55em',
                      'pagewidth': '75em',
                      'nosidebar': False,
                      'headerbg': css_gradient}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this f_set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'pypetdoc'


# -- Options for LaTeX output --------------------------------------------------

fh = open('latex/latex_preamble.tex', 'r+')
PREAMBLE = fh.read()
fh.close()
latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
'papersize': 'a4paper',

# The font size ('10pt', '11pt' or '12pt').
'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
'preamble': PREAMBLE,
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('latex', 'pypet.tex', u'pypet Documentation',
   u'Robert Meyer', 'manual', True),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'pypet', u'pypet Documentation',
     [u'Robert Meyer'], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output ------------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'pypet', u'pypet Documentation',
   u'Robert Meyer', 'pypet', 'One line description of project.',
   'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'


# For read the docs
class Mock(object):
    def __init__(self, *args, **kwargs):
        pass

    def __call__(self, *args, **kwargs):
        return Mock()

    @classmethod
    def __getattr__(cls, name):
        if name in ('__file__', '__path__'):
            return '/dev/null'
        elif name == '__version__':
            # To mock the call to pt.__version__ in pypet.utils.ptcompat
            return '2'
        elif name[0] == name[0].upper():
            mockType = type(name, (), {})
            mockType.__module__ = __name__
            return mockType
        else:
            return Mock()

MOCK_MODULES = ['tables', 'numpy', 'brian' ,'pandas', 'brian.units', 'brian.fundamentalunits',
                'brian.monitor', 'scipy', 'scipy.sparse', 'tables.parameters']
for mod_name in MOCK_MODULES:
    sys.modules[mod_name] = Mock()

# Monkey-patch functools.wraps
import functools

def no_op_wraps(func):
    """Replaces functools.wraps in order to undo wrapping.

    Can be used to preserve the decorated function's signature
    in the documentation generated by Sphinx.

    """
    def wrapper(decorator):
        return func
    return wrapper

functools.wraps = no_op_wraps


# Avoid double documentation
import pypet
all = pypet.__all__
for name in all:
    item = getattr(pypet, name)
for name in pypet.__all__:
    item = getattr(pypet, name)
    if hasattr(item, '__api__'):
        for api_name in item.__api__:
            try:
                delattr(item, api_name)
            except AttributeError:
                pass