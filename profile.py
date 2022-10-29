
"""
WIP profile, using for now just to set up image.

Instructions:
Under development, do not use.
"""

# Import the Portal object.
import geni.portal as portal
# Import the ProtoGENI library.
import geni.rspec.pg as pg
# Emulab specific extensions.
import geni.rspec.emulab as emulab

IMAGE='urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU20-64-STD'

# Create a portal context, needed to defined parameters
pc = portal.Context()

# Create a Request object to start building the RSpec.
request = pc.makeRequestRSpec()

node = request.RawPC("node0")
node.disk_image = IMAGE
node.hardware_type = "m510"

pc.printRequestRSpec()
