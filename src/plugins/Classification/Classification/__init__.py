"""
This is where the implementation of the plugin code goes.
The Classification-class is imported from both run_plugin.py and run_debug.py
"""
import sys
import logging
from webgme_bindings import PluginBase

# Setup a logger
logger = logging.getLogger('Classification')
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)  # By default it logs to stderr..
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


class Classification(PluginBase):
    def main(self):
        core = self.core
        root_node = self.root_node
        META = self.META
        active_node = self.active_node
        logger = self.logger
            
            
        states = []
        statePaths = []
        transitions = []
        transitionPaths = []
        arcs = []
        arcPaths = []

        nodes = core.load_sub_tree(active_node)
        for node in nodes:
          meta_node = core.get_base_type(node)
          if core.get_attribute(meta_node, 'name') in ("S2T", "T2S"):
            arcs.append(node)
            arcPaths.append([(core.get_pointer_path(node,'src')),(core.get_pointer_path(node,'dst'))])
          elif core.get_attribute(meta_node, 'name') in ("Transition"):
            transitions.append(node)
          elif core.get_attribute(meta_node, 'name') in ("State","Init", "End"):
            states.append(node)

        for transition in transitions:
          transitionPaths.append(core.get_path(transition))
            
        for state in states:
          statePaths.append(core.get_path(state))
        
        
        # Determine whether it is free-choice petri net
        inplace = set()
        is_free_choice = "True"
        for i in arcPaths:
          if i[0] in inplace:
            is_free_choice = "False"
          else:
            inplace.add(i[0])
        
        # Determine whether it is State machine
        is_state_machine = "True"
        for i in transitionPaths:      
          in_count = 0
          out_count = 0
          for k in arcPaths:
            if k[0] == i:
              in_count += 1
            if k[1] == i:
              out_count += 1
          if (in_count > 1 or out_count > 1):
            is_state_machine = "False"

        # Determine whether it is Marked Graph
        is_marked_graph = "True"
        for i in statePaths:      
          in_count = 0
          out_count = 0
          for k in arcPaths:
            if k[0] == i:
              in_count += 1
            if k[1] == i:
              out_count += 1
          if (in_count > 1 or out_count > 1):
            is_marked_graph = "False"
            
            
        if (is_marked_graph == "True" and is_state_machine == "True"):
          is_workflow = "True"
        else:
          is_workflow = "False"
            
            
        logger.info('Free-choice petri net: {0}'.format(is_free_choice))
        logger.info('State Machine: {0}'.format(is_state_machine))
        logger.info('Marked graph: {0}'.format(is_marked_graph))
        logger.info('Workflow net: {0}'.format(is_workflow))


        self.send_notification("Free Choice{0}: ".format(is_free_choice))    
        self.send_notification("StateMachine{0}: ".format(is_state_machine))
        self.send_notification("Marked Graph{0}: ".format(is_marked_graph))
        self.send_notification("Workflow Net{0}: ".format(is_workflow))
