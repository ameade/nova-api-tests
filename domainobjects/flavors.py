# Copyright 2011 OpenStack LLC.
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
Flavor interface.
"""


import base

#Stubbed until db interaction is impl
EXPECTED_FLAVORS = [
    {"id" : 1, "name" : "m1.tiny", "ram" : 512, "disk" : 0},
    {"id" : 2, "name" : "m1.small", "ram" : 2048, "disk" : 20},
    {"id" : 3, "name" : "m1.medium", "ram" : 4096, "disk" : 40},
    {"id" : 4, "name" : "m1.large", "ram" : 8192, "disk" : 80},
    {"id" : 5, "name" : "m1.xlarge", "ram" : 16384, "disk" : 160},
]


class Flavor(base.Resource):
    """
    A flavor is an available hardware configuration for a server.
    """
    def __repr__(self):
        return "<Flavor: %s>" % self.name


class FlavorManager(base.ManagerWithFind):
    """
    Manage :class:`Flavor` resources.
    """
    resource_class = Flavor

    def list(self):
        """
        Get a list of all flavors.

        :rtype: list of :class:`Flavor`.
        """
        return self._list("/flavors", "flavors")
        
    def list_details(self):
        """
        Get a list of all flavors.

        :rtype: list of :class:`Flavor`.
        """
        return self._list("/flavors/detail", "flavors")

    def get(self, flavor):
        """
        Get a specific flavor.

        :param flavor: The ID of the :class:`Flavor` to get.
        :rtype: :class:`Flavor`
        """
        return self._get("/flavors/%s" % base.getid(flavor), "flavor")
