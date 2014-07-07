# -*- coding: utf-8 -*-
#
## This file is part of Invenio.
## Copyright (C) 2014 CERN.
##
## Invenio is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 2 of the
## License, or (at your option) any later version.
##
## Invenio is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with Invenio; if not, write to the Free Software Foundation, Inc.,
## 59 Temple Place, Suite 330, Boston, MA 02D111-1307, USA.

PACKAGES = [
	"invenio_opendata.base.*",
    "invenio_opendata.modules.*",
    "invenio.modules.*",
]

DEPOSIT_TYPES = [
    'invenio_opendata.modules.deposit.workflows.article.article',
]

CFG_SITE_NAME = 'Open Data - CERN'

CFG_SITE_NAME_INTL = {
    "en": "Open Data - CERN", # Shouldn't be required.
    "fr": "Open Data - CERN",
    "de": "Open Data - CERN",
    "it": "Open Data - CERN"
}