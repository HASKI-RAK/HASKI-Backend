import sys
import os

#from pyhugin94 import *
from Lib.hugin94.pyhugin94 import *
#from Lib.hugin92.pyhugin92 import *
#
# Parse listener for reading the network specification
#
def parse_listener(line, description):
    """A parse listener that prints the line number and error description."""
    print("Parse error line {}: {}".format(line, description))


#
# load an OOBN model into a class collection, find the main class, and create a Domain
#
# We assume the model is stored in a class collection
#
def load_model (cc_name, class_name):
    dom = None
    c = None
    #
    # a class collection holds a collection of classes
    #
    cc = ClassCollection ()

    try:
        # parse the file specification
        cc.parse_classes ("{}".format(cc_name), parse_listener)
        # get the main class
        c = cc.get_class_by_name (class_name)

        # we need a Domain object to perform inference
        dom = Domain (c)
        
        # we need to compile the model to perform inference
        dom.compile ()

    except HuginException:
        print("A Hugin Exception was raised!")
        raise

    return dom


#
# case 1: enter evidence, propagate, and print the probability distribution of the target node
#
def process_case_1 (dom, target):

    # get handles to evidence node. We use "dot" notation to find a node by name
    names = [ 'Active_Reflective.ILSF1AR1', 'Active_Reflective.ILSF5AR2', 'Active_Reflective.ILSF9AR3', 'Active_Reflective.ILSF13AR4', 'Active_Reflective.ILSF17AR4','Active_Reflective.ILSF17AR5','Active_Reflective.ILSF21AR6', 'Active_Reflective.ILSF25AR7', 'Active_Reflective.ILSF29AR8','Active_Reflective.ILSF33AR9','Active_Reflective.ILSF37AR10','Active_Reflective.ILSF37AR11']   
    labels = [ 'a', 'a', 'a', 'a', 'a','a','a','a','a', 'a', 'a' ]

    # enter some evidence    
    for name, label in zip (names, labels):
        nd = dom.get_node_by_name (name)
        if nd is not None:
            idx = nd.get_state_index_from_label (label)
            if idx < 0:
                print (f'{label} not found as state of {name}')
            else:
                nd.select_state (idx)
        else:
            print (f'{name} not found')

    # propagate the evidence to compute posterior beliefs
    dom.propagate ()

           
    # get local targets
    local_targets = []
    # we should test to None pointer, here we take the risk;-)
    local_targets.append(dom.get_node_by_name ('Active_Reflective.Score_active_reflective_11'))
    local_targets.append(dom.get_node_by_name ('Visual_verbal.Score_visual_verbal_11'))
    
    # print the belief for each learning dimension
    for nd in local_targets:
        print (f'{nd.get_name ()}')
        for i in range (nd.get_number_of_states ()):
            print (f'P({nd.get_state_value (i)}|e) = {nd.get_belief (i):.2f}')
        print ()    

    # print beliefs for target (it has uniform distribution though!)
    print (f'{target.get_name ()}')
    for i in range (target.get_number_of_states ()):
        print (f'P({target.get_state_label (i)}|e) = {target.get_belief (i):.2f}')
    
    # remember to remove any evidence and reset the domain
    dom.initialize ()
#
# Main procedure
#
if __name__ == "__main__":
    if len(sys.argv) == 0:
        print ('usage: <oobn> <class> <target>')
        exit ()

    # map input to identifiers
    specfile     = sys.argv[1]   #'LearnProfile_cc.oobn'
    cls_name     = sys.argv[2]   #'LearnProfile'
    target_name  = sys.argv[3]   #'Result'
    
    try:
        print ('Be patient. It is a large model;-)')
        # read model and compile it for inference
        dom = load_model (specfile, cls_name)
        
        # get target
        target = dom.get_node_by_name (target_name)
        if target is None:
            print (f'{target_name} not found')
            exit ()

        # we consider a case of evidence
        process_case_1 (dom, target)

        # clean up any memory allocations
        dom.delete ()
    except HuginException:
        print("A Hugin Exception was raised!")
        raise

    # all done
    print ('Done, thank you!')
