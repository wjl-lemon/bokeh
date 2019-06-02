# -*- coding: utf-8 -*-
#
# Bokeh documentation build configuration file, created by
# sphinx-quickstart on Sat Oct 12 23:43:03 2013.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = '1.8'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.ifconfig',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    'bokeh.sphinxext.bokeh_autodoc',
    'bokeh.sphinxext.bokeh_color',
    'bokeh.sphinxext.bokeh_enum',
    'bokeh.sphinxext.bokeh_gallery',
    'bokeh.sphinxext.bokeh_github',
    'bokeh.sphinxext.bokeh_jinja',
    'bokeh.sphinxext.bokeh_model',
    'bokeh.sphinxext.bokeh_options',
    'bokeh.sphinxext.bokeh_palette',
    'bokeh.sphinxext.bokeh_palette_group',
    'bokeh.sphinxext.bokeh_plot',
    'bokeh.sphinxext.bokeh_prop',
    'bokeh.sphinxext.bokeh_releases',
    'bokeh.sphinxext.bokeh_sitemap',
    'bokeh.sphinxext.bokehjs_content',
    'bokeh.sphinxext.collapsible_code_block',
]

napoleon_include_init_with_doc = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'Bokeh'
copyright = '© Copyright 2015-2019, Anaconda and Bokeh Contributors.'

# Get the standard computed Bokeh version string to use for |version|
# and |release|
from bokeh import __version__

# The short X.Y version.
version = __version__
# The full version, including alpha/beta/rc tags.
release = __version__

# Check for version override (e.g. when re-deploying a previously released
# docs, or when pushing test docs that do not have a corresponding BokehJS
# available on CDN)
from bokeh.settings import settings
if settings.docs_version():
    version = release = settings.docs_version()

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# Whether to allow builds to succeed if a Google API key is not defined and plots
# containing "GOOGLE_API_KEY" are processed
bokeh_missing_google_api_key_ok = False

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
add_module_names = False

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# Sort members by type
autodoc_member_order = 'groupwise'

# patterns to exclude
exclude_patterns = ['docs/releases/*']

# This would more properly be done with rst_epilog but something about
# the combination of this with the bokeh-gallery directive breaks the build
rst_prolog = """
.. |Color|              replace:: :py:class:`~bokeh.core.properties.Color`
.. |DataSpec|           replace:: :py:class:`~bokeh.core.properties.DataSpec`
.. |Document|           replace:: :py:class:`~bokeh.document.Document`
.. |HasProps|           replace:: :py:class:`~bokeh.core.has_props.HasProps`
.. |Model|              replace:: :py:class:`~bokeh.model.Model`
.. |Property|           replace:: :py:class:`~bokeh.core.property.bases.Property`
.. |PropertyDescriptor| replace:: :py:class:`~bokeh.core.property.descriptor.PropertyDescriptor`
.. |PropertyContainer|  replace:: :py:class:`~bokeh.core.property.wrappers.PropertyContainer`
.. |UnitsSpec|          replace:: :py:class:`~bokeh.core.properties.UnitsSpec`

.. |field|              replace:: :py:func:`~bokeh.core.properties.field`
.. |value|              replace:: :py:func:`~bokeh.core.properties.value`
"""

# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'bokeh_theme'
html_theme_path = ['.']

html_context = {
    'SITEMAP_BASE_URL': 'https://bokeh.pydata.org/en/', # Trailing slash is needed
    'DESCRIPTION': 'Bokeh visualization library, documentation site.',
    'AUTHOR': 'Bokeh contributors',
    'VERSION': version,
    'NAV': (
        ('Github', '//github.com/bokeh/bokeh'),
    ),
    'ABOUT': (
        ('Roadmap', 'https://bokeh.org/roadmap'),
        ('Team',            'https://bokeh.org/team'),
        ('Citation',        'https://bokeh.org/citation'),
        ('Contact',         'https://bokeh.org'),
    ),
    'SOCIAL': (
        ('Contribute', 'contribute'),
        ('Discourse', 'https://discourse.bokeh.org'),
        ('Github', '//github.com/bokeh/bokeh'),
        ('Twitter', '//twitter.com/BokehPlots'),
    ),
    'NAV_DOCS': (
        ('Installation', 'docs/installation'),
        ('User Guide', 'docs/user_guide'),
        ('Gallery', 'docs/gallery'),
        ('Tutorial', 'https://mybinder.org/v2/gh/bokeh/bokeh-notebooks/master?filepath=tutorial%2F00%20-%20Introduction%20and%20Setup.ipynb'),
        ('Reference', 'docs/reference'),
        ('Releases', 'docs/releases'),
        ('Developer Guide', 'docs/dev_guide'),
        ('Search', 'search'),
    ),
}

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = True

# Output file base name for HTML help builder.
htmlhelp_basename = 'Bokehdoc'

# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
    ('index', 'Bokeh.tex', u'Bokeh Documentation', u'Anaconda', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

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
    ('index', 'bokeh', u'Bokeh Documentation',
     [u'Anaconda'], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output ------------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    ('index', 'Bokeh', u'Bokeh Documentation', u'Anaconda', 'Bokeh', 'Interactive Web Plotting for Python', 'Graphics'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# intersphinx settings
intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'pandas': ('http://pandas.pydata.org/pandas-docs/stable/', None),
    'numpy': ('https://docs.scipy.org/doc/numpy/', None)
}


import os
import subprocess

# Do not use Bokeh CDNs to serve JS files when building latest version
# of docs (and/or unreleased versions). We want to serve the compiled
# JS files from Read the Docs servers itself to match the
# documentation with the JS version. Although, when using a tagged
# release, we want to use Bokeh CDN.
def _get_current_commit():
    result = subprocess.run(
        ['git', 'rev-parse', '--verify', 'HEAD'],
        stdout=subprocess.PIPE,
    )
    return result.stdout.decode('utf8').strip()

def is_tagged_version():
    commit = _get_current_commit()
    print('Bokeh commit: {commit}'.format(commit=commit))
    result = subprocess.run(
        ['git', 'tag', '--points-at', commit],
        stdout=subprocess.PIPE,
    )
    tagged = result.stdout.decode('utf8').strip()
    print('Bokeh tagged version: {tagged}'.format(tagged=tagged))
    return bool(tagged)

if os.environ.get('READTHEDOCS') == 'True':
    readthedocs_version = os.environ.get('READTHEDOCS_VERSION')
    if is_tagged_version():
        # Use Bokeh Resources from CDN
        os.environ['BOKEH_DOCS_CDN'] = readthedocs_version
    else:
        # Use Bokeh Resources from Read the Docs
        os.environ['BOKEH_DOCS_CDN'] = 'test:{readthedocs_version}'.format(
            readthedocs_version=readthedocs_version,
        )

    bokeh_docs_cdn = os.environ.get('BOKEH_DOCS_CDN')
    print('BOKEH_DOCS_CDN: {bokeh_docs_cdn}'.format(
        bokeh_docs_cdn=bokeh_docs_cdn,
    ))

    # Set the proper ``BOKEH_DOCS_VERSION`` based on the version being
    # built on Read the Docs
    os.environ['BOKEH_DOCS_VERSION'] = readthedocs_version
    print('BOKEH_DOCS_VERSION: {readthedocs_version}'.format(
        readthedocs_version=readthedocs_version,
    ))

    build_js = os.environ.get('BOKEH_BUILD_JS')
    print('BOKEH_BUILD_JS: {build_js}'.format(build_js=build_js))

    # Download all the sample data to plot
    import bokeh
    bokeh.sampledata.download(progress=False)

    # Create the proper structure to serve CSS and JS files compiled by
    # Bokeh. We can't use ``html_static_path`` here because the URLs are
    # hardcoded to ``static/js`` instead of ``_static/js``, etc
    os.system('mkdir -p bokehJSbuildstatic')
    os.system('cd bokehJSbuildstatic; ln -s ../../../bokehjs/build static')

    html_extra_path = [
        'bokehJSbuildstatic',
    ]

    # Ignore Google API key
    bokeh_missing_google_api_key_ok=True

    # To deal with ``/scripts/`` URLs
    bokeh_plot_use_relative_paths = True
