#!/usr/bin/env python

# This is an automatically generated script to run your query
# to use it you will require the intermine python client.
# To install the client, run the following command from a terminal:
#
#     sudo easy_install intermine
#
# For further documentation you can visit:
#     http://intermine.readthedocs.org/en/latest/web-services/

# The line below will be needed if you are running this script with python 2.
# Python 3 will ignore it.
from __future__ import print_function

# The following two lines will be needed in every python script:
from intermine.webservice import Service
service = Service("http://production-intermine-app.alliancegenome.org:8080/alliancemine/service")

# Get a new query on the class (table) you will be querying:
query = service.new_query("Gene")

# The view specifies the output columns
query.add_view("primaryIdentifier", "symbol", "name")
