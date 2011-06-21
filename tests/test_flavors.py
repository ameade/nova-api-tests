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

from domainobjects import openstack
from domainobjects import flavors
import utils


class FlavorsTest(utils.TestCase):

    def setUp(self):
        self.os = openstack.OpenStack()
        #TODO (ameade): get actual flavors from db
        self.expected_flavors = flavors.EXPECTED_FLAVORS

    def test_get_flavor_details(self):
        """
        Verify the expected details are returned for a flavor
        """
        expected_flavor = self.expected_flavors[0]
        if expected_flavor is None:
            return

        flavor = self.os.flavors.get(expected_flavor["id"])
        self.assertIsInstance(flavor, flavors.Flavor)
        self.assertEqual(flavor.name, expected_flavor["name"])
        self.assertEqual(flavor.ram, expected_flavor["ram"])
        self.assertEqual(flavor.disk, expected_flavor["disk"])
        self.assertEqual(200, flavor.status_code)

    def test_get_flavors(self):
        """
        Verify the expected flavors are returned
        """

        flavors_list = sorted(self.os.flavors.list(), key=lambda k: k.id)
        self.assertEqual(len(self.expected_flavors), len(flavors_list))
        for i in range(len(flavors_list)):
            expected_flavor = self.expected_flavors[i]

            flavor = flavors_list[i]
        
            self.assertIsInstance(flavor, flavors.Flavor)
            self.assertEqual(flavor.name, expected_flavor["name"])
            self.assertEqual(200, flavor.status_code)

    def test_get_flavors_details(self):
        """
        Verify the detailed expected flavors are returned
        """

        flavors_list = sorted(self.os.flavors.list_details(), key=lambda k: k.id)
        self.assertEqual(len(self.expected_flavors), len(flavors_list))
        for i in range(len(flavors_list)):
            expected_flavor = self.expected_flavors[i]

            flavor = flavors_list[i]
        
            self.assertIsInstance(flavor, flavors.Flavor)
            self.assertEqual(flavor.name, expected_flavor["name"])
            self.assertEqual(flavor.ram, expected_flavor["ram"])
            self.assertEqual(flavor.disk, expected_flavor["disk"])
            self.assertEqual(200, flavor.status_code)
