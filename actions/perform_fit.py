# (C) Copyright 2019 Hewlett Packard Enterprise Development LP.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#  http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# __author__ = "@netwookie"
# __credits__ = ["Rick Kauffman"]
# __license__ = "Apache2.0"
# __version__ = "1.0.0"
# __maintainer__ = "Rick Kauffman"
# __email__ = "rick.a.kauffman@hpe.com"

# A python script for getting a dictionary of switches

from pyhpecfm.auth import CFMClient
from pyhpecfm import fabric


from st2common.runners.base_action import Action


class fabricfit(Action):
    def run(self, ipaddress=None, username=None, password=None, fab_uuid=None, name=None, description=None):

        # Create client connection
        client = CFMClient(ipaddress, username, password)

        # Get switches from plexxi controller
        try:
            cfm_fit = fabric.perform_fit(client, fab_uuid, name, description)
        except:
            error = "ERR-LOGIN - Failed to perfor fit on CFM controller"
            return error

        return
