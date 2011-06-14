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
import utils


class TestServers(utils.TestCase):
    
    def setUp(self):
        self.os = openstack.OpenStack()
        self.server = self.os.servers.create(name="testserver",
                                image="http://glance1:9292/v1/images/3",
                                flavor="http://172.19.0.3:8774/v1.1/flavors/3")
        #NOTE: Do we really want to wait for the server to build?
        #self.server.waitForStatus('ACTIVE')
    
    def tearDown(self):
	    self.server.delete()

    def test_list_servers(self):
        """	    
        Verify that a new server is returned in the list of
        servers for the user
        """
        serverList = self.os.servers.list()
        found = False
        for s in serverList:
            if s.name == 'testserver':
                found = True
        assert found

    def test_create_delete_server(self):
        """
        Verify that a server instance can be created and deleted        
        """
        
        newServer = self.os.servers.create(name="testserver2", 
                                image="http://glance1:9292/v1/images/3",
                                flavor="http://172.19.0.3:8774/v1.1/flavors/3")
        
        self.assertEqual(202, newServer.status_code)        
        #newServer.waitForStatus('ACTIVE')
        createdServer = self.os.servers.get(newServer.id)
        self.assertEqual('testserver2', createdServer.name)                
        newServer.delete()
	#TODO: assert something here
    
    def test_update_server_name(self):
        """         
        Verify the name of an instance can be changed
        """
    
        self.server.update_name(name='modifiedName')
        #self.server.waitForStatus('ACTIVE')

        updatedServer = self.os.servers.get(self.server.id)
        self.assertEqual('modifiedName', updatedServer.name)

    def test_create_server_invalid_image(self):
        """
        Verify that creating a server with an unknown image ref will fail
        """
        newServer = self.os.servers.create(name="testserver2", 
	    image="http://glance1:9292/v1/images/9999",
	    flavor="http://172.19.0.3:8774/v1.1/flavors/3")

    def test_create_server_invalid_flavor(self):
        """
        Verify that creating a server with an unknown image ref will fail
        """
        
        newServer = self.os.servers.create(name="testserver2", 
	    image="http://glance1:9292/v1/images/1",
	    flavor="http://172.19.0.3:8774/v1.1/flavors/99999999")
