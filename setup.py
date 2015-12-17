#!/usr/bin/env python

from setuptools import setup

from gerbmerge.gerbmerge import VERSION_MAJOR, VERSION_MINOR

setup (name = "gerbmerge",
       license = "GPL",
       version = "%s.%s" % (VERSION_MAJOR, VERSION_MINOR),
      long_description=\
r"""GerbMerge is a program that combines several Gerber
(i.e., RS274-X) and Excellon files into a single set
of files. This program is useful for combining multiple
printed circuit board layout files into a single job.

For more details on installation or running GerbMerge, see the
URL below.
""",
       description = "Merge multiple Gerber/Excellon files",
       author = "Rugged Circuits LLC",
       author_email = "support@ruggedcircuits.com",
       url = "http://ruggedcircuits.com/gerbmerge",
       packages = ['gerbmerge'],
       platforms = ['all'],
       entry_points={
           "console_scripts":[
                 "gerbmerge = gerbmerge.gerbmerge"
           ]
        }
)
