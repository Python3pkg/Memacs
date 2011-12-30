#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time-stamp: <2011-12-30 03:38:09 armin>

import sys
import os
import logging
import time
# needed to import common.*
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common.orgproperty import OrgProperties
from common.orgformat import OrgFormat
from common.memacs import Memacs


PROG_VERSION_NUMBER = u"0.0"
PROG_VERSION_DATE = u"2011-12-18"
PROG_SHORT_DESCRIPTION = u"Memacs for ... "
PROG_TAG = u"mytag"
PROG_DESCRIPTION = u"""
this class will do ....

Then an Org-mode file is generated that contains ....

if youre module needs a config file please give information about usage:

sample config:
[memacs-example]           <-- has to be CONFIG_PARSER_NAME
foo = 0
bar = 1

"""
#CONFIG_PARSER_NAME="memacs-example"  # set this at Ctor see bottom
COPYRIGHT_YEAR = "2011-2012"
COPYRIGHT_AUTHORS = """Karl Voit <tools@Karl-Voit.at>,
Armin Wieser <armin.wieser@gmail.com>"""


class Foo(Memacs):
    def _parser_add_arguments(self):
        """
        overwritten method of class Memacs

        add additional arguments
        """
        Memacs._parser_add_arguments(self)

        #self._parser.add_argument(
        #   "-e", "--example", dest="example",
        #   action="store_true",
        #   help="path to a folder to search for filenametimestamps, " +
        #   "multiple folders can be specified: -f /path1 -f /path2")
        
        #self._parser.add_argument(
        #   "-i", "--int", dest="example_int",
        #   action="store_true",
        #   help="example2",
        #   type=int)


    def _parser_parse_args(self):
        """
        overwritten method of class Memacs

        all additional arguments are parsed in here
        """
        Memacs._parser_parse_args(self)
        # if self._args.example == ...:
        #     self._parser.error("could not parse foo")

    def _main(self):
        """
        get's automatically called from Memacs class
        """
        # do all the stuff

        # if you need something from config:
        # attention: foo will be unicode
        # foo = self._get_config_option("foo")

        logging.info("foo started")

        # use logging.debug() for debug messages
        # use logging.error() for error messages
        # use logging.info() instead of print for informing user
        #
        # on an fatal error:
        # use logging.error() and sys.exit(1)

        timestamp = OrgFormat.datetime(time.gmtime(0))
        # note: timestamp has to be a struct_time object
        self._writer.write_org_subitem(timestamp=timestamp,
                                       output="foo")

        # writes following:
        #** <1970-01-01 Thu 00:00> foo
        #   :PROPERTIES:
        #   :ID:             da39a3ee5e6b4b0d3255bfef95601890afd80709
        #   :END:

        notes = "bar notes\nfoo notes"

        p = OrgProperties(data_for_hashing="read comment below")
        # if a hash is not unique only with its :PROPERTIES: , then
        # set data_for_hasing string additional information i.e. the output
        # , which then makes the hash really unique
        #
        # if you *really*, *really* have already a unique id,
        # then you can call following method:
        # p.set_id("unique id here")

        p.add("DESCRIPTION", "foooo")
        p.add("foo-property", "asdf")

        tags = [u"tag1", u"tag2"]

        self._writer.write_org_subitem(timestamp=timestamp,
                                       output="bar",
                                       note=notes,
                                       properties=p,
                                       tags=tags)
        # writes following:
        #** <1970-01-01 Thu 00:00> bar    :tag1:tag2:
        #   bar notes
        #   foo notes
        #   :PROPERTIES:
        #   :DESCRIPTION:    foooo
        #   :FOO-PROPERTY:   asdf
        #   :ID:             97521347348df02dab8bf86fbb6817c0af333a3f
        #   :END:


if __name__ == "__main__":
    memacs = Foo(
        prog_version=PROG_VERSION_NUMBER,
        prog_version_date=PROG_VERSION_DATE,
        prog_description=PROG_DESCRIPTION,
        prog_short_description=PROG_SHORT_DESCRIPTION,
        prog_tag=PROG_TAG,
        copyright_year=COPYRIGHT_YEAR,
        copyright_authors=COPYRIGHT_AUTHORS
#        use_config_parser_name=CONFIG_PARSER_NAME
        )
    memacs.handle_main()
