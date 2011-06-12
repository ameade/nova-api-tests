# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2010 United States Government as represented by the
# Administrator of the National Aeronautics and Space Administration.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""
Package-level global flags are defined here, the rest are defined
where they're used.
"""


from gflags import *

# This keeps pylint from barfing on the imports
FLAGS = FLAGS
DEFINE_string = DEFINE_string
DEFINE_integer = DEFINE_integer

# __GLOBAL FLAGS ONLY__
# Define any app-specific flags in their own files, docs at:
# http://code.google.com/p/python-gflags/source/browse/trunk/gflags.py#39

DEFINE_string('username', 'admin', 'Username to use for authentication')
DEFINE_string('api_key', 'admin', 'API key to use for authentication')
DEFINE_string('auth_url', 'http://localhost:8774/v1.0/',
              'URL to use for authentication')
DEFINE_string('glance_host', 'localhost', 'Host of glance server')
DEFINE_integer('glance_port', 9292, 'Port of glance server')
