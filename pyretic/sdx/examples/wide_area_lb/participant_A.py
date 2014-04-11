################################################################################
#
#  <website link>
#
#  File:
#        core.py
#
#  Project:
#        Software Defined Exchange (SDX)
#
#  Author:        
#        Arpit Gupta
#        Muhammad Shahbaz
#        Laurent Vanbever
#
#  Copyright notice:
#        Copyright (C) 2012, 2013 Georgia Institute of Technology
#              Network Operations and Internet Security Lab
#
#  Licence:
#        This file is part of the SDX development base package.
#
#        This file is free code: you can redistribute it and/or modify it under
#        the terms of the GNU Lesser General Public License version 2.1 as
#        published by the Free Software Foundation.
#
#        This package is distributed in the hope that it will be useful, but
#        WITHOUT ANY WARRANTY; without even the implied warranty of
#        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#        Lesser General Public License for more details.
#
#        You should have received a copy of the GNU Lesser General Public
#        License along with the SDX source package.  If not, see
#        http://www.gnu.org/licenses/.
#

import json
import os
from pyretic.sdx.lib.corelib import *


cwd = os.getcwd()

def parse_config(config_file):
    participants = json.load(open(config_file, 'r'))
    
    for participant_name in participants:
        for i in range(len(participants[participant_name]["IPP"])):
            participants[participant_name]["IPP"][i] = IPPrefix(participants[participant_name]["IPP"][i])    
    return participants

def policy(participant, sdx):
    '''
        Specify participant policy
    '''
    
    #participants = parse_config(cwd + "/pyretic/sdx/examples/inbound_traffic_engineering_VNH/local.cfg")
    prefixes_announced=bgp_get_announced_routes(sdx,'1')
    
    #final_policy = ((match(dstport=80) >> sdx.fwd(participant.peers['B']))+
    #                (match(dstport=22) >> sdx.fwd(participant.peers['C']))+
    #                (match(dstport=1024) >> sdx.fwd(participant.peers['C']))+
    #                (match_prefixes_set(set(prefixes_announced)) >> sdx.fwd(participant.phys_ports[0]))
    #               )
    
    final_policy= (
                   (match_prefixes_set(set(prefixes_announced)) >> sdx.fwd(participant.phys_ports[0]))
                )            
    return final_policy