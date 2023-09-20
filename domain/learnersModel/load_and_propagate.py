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
def process_case_1(dom, target, names, labels, str_local_target, str_dim_output):
    """Process process_case_1"""
    # get handles to evidence node. We use "dot" notation to find a node by name
    #names = [ 'Active_Reflective.ILSF1AR1', 'Active_Reflective.ILSF5AR2', 'Active_Reflective.ILSF9AR3', 'Active_Reflective.ILSF13AR4', 'Visual_Verbal.ILSF3VV1' ]
    #labels = [ 'a', 'a', 'a', 'z', 'b']

    result = []

    print("\n\n===========")
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
    local_targets.append(dom.get_node_by_name (str_local_target))  #new
      
    current_belif = 0.0
    # print the belief for each learning dimension
    for nd in local_targets:
        print (f'{nd.get_name ()}')        
        for i in range (nd.get_number_of_states ()):
            
            print (f'P({nd.get_state_value (i)}|e) = {nd.get_belief (i):.2f}')
            if nd.get_belief (i)>0.30 and nd.get_belief (i)>current_belif :                                                  # new
                result.append(nd.get_state_value (i))                                   # new
                print(f'P({nd.get_state_value (i)}|e) = {nd.get_belief (i):.2f}')       # new
                current_belif = nd.get_belief (i)
        print ()    

    # print beliefs for target (it has uniform distribution though!)
    print (f'{target.get_name ()}')
    for i in range (target.get_number_of_states ()):
        print (f'P({target.get_state_label (i)}|e) = {target.get_belief (i):.2f}')

    print(range (nd.get_number_of_states ()), nd.get_state_label (0),"-",nd.get_belief (1))


    # print beliefs for dim_FSLSM
    # get local targets
    
    local_targets = []
    local_targets.append(dom.get_node_by_name (str_dim_output))

    # pole_1 = active_a     sentive_a    visual_a  sequential_b 
    # pole_2 = reflective_b intuitive_b  verbal_b  global_b

    pole_1 = False
    pole_2 = False
   
    print ()

    for nd in local_targets:
        print (f'{nd.get_name ()}')
        for i in range (nd.get_number_of_states ()):
            print (f'P({nd.get_state_label (i)}|e) = {nd.get_belief (i):.2f}')
            if nd.get_state_label (i) =='true' and nd.get_belief (i):
                 pole_1 = True
                 print("-----",nd.get_state_label (i))
                 print (f'P({nd.get_state_label (i)}|e) = {nd.get_belief (i):.2f}')

   
    result = get_dimension(pole_1,str_dim_output, result)
    print ("result:",result)
    # remember to remove any evidence and reset the domain
    dom.initialize ()
    return result



def get_dimension(pole_1,str_dim_output, result):
    """."""
    dim_str = "" 

    if (str_dim_output.__contains__("Active_") and result is not None): 
        if(pole_1):
           return "act:",result[0],","        
        else: return "ref:",result[0],","        
    if (str_dim_output.__contains__("Sensory_") ):
        if(pole_1): 
            return "sns:",result[0],"," 
        else: return "int:",result[0],"," 
    if (str_dim_output.__contains__("Visual_") ):
        if(pole_1):
            return "vis:",result[0],"," 
        else: return "verb:",result[0],"," 
    if (str_dim_output.__contains__("Sequenz_")):
        if(pole_1):
            return "seq:",result[0],"," 
        else: return "glo:",result[0],"," 
       
    #result.append( "ref") ; return result

#
# transformed der Input
#
def get_ils_answers(ils_answers):-> dict:
    """ assigne the answers of ILS """
    print("\n")    
    ils_input_answers = {}
    ils_perception_answers = {}
    ils_processing_answers = {}
    ils_understanding_answers = {}
    node_name = ""
    for id, answer in ils_answers.items():
        if id.startswith("vv"):
            str_vv = id.upper()
            pos = str_vv.split('_')
            str_vv = "ILS"+pos[2]+pos[0]+pos[1]
            node_name = "Visual_verbal"
            ils_answers_oobn[str_vv] = answer
            ils_input_answers[str_vv] = answer
        if id.startswith("si"):
            str_vv = id.upper()
            pos = str_vv.split('_')
            str_vv = "ILS"+pos[2]+pos[0]+pos[1]
            node_name = "Sensory_Intuitive."
            ils_perception_answers[str_vv] = answer
        if id.startswith("ar"):
            str_vv = id.upper()
            pos = str_vv.split('_')
            str_vv = "ILS"+pos[2]+pos[0]+pos[1]
            node_name = "Active_Reflective."
            ils_processing_answers[str_vv] = answer
        if id.startswith("sg"):
            str_vv = id.upper()
            pos = str_vv.split('_')
            str_vv = "ILS"+pos[2]+pos[0]+pos[1]
            node_name = "Sequenz_Global."           
            ils_understanding_answers[str_vv] = answer
    print("\t", ils_answers_oobn)
    return ils_answers_oobn

                 
def calulated_ILS ():
#'if __name__ == "__main__":
    if len(sys.argv) == 0:
        print ('usage: <oobn> <class> <target>')
        exit ()

    # map input to identifiers
    specfile     = 'LearnProfile_cc.oobn' #sys.argv[1]   'LearnProfile_cc.oobn'
    cls_name     = 'LearnProfile' #sys.argv[2]
    target_name  = 'Result' # sys.argv[3]
    
    try:
        print ('Be patient. It is a large model;-)')
        # read model and compile it for inference
        dom = load_model (specfile, cls_name)
        
        # get target
        target = dom.get_node_by_name (target_name)
        if target is None:
            print (f'{target_name} not found')
            exit ()

        score_nodes = ['Active_Reflective.Active_A_highest_11',
                       'Sensory_Intuitive.Sensitive_A_highest_11',
                       'Visual_verbal.Visual_A_highest_11',
                       'Sequenz_Global.Sequential_A_highest_11']

        AR_names = ['Active_Reflective.ILSF1AR1',
                    'Active_Reflective.ILSF5AR2',
                    'Active_Reflective.ILSF9AR3',
                    'Active_Reflective.ILSF13AR4',
                    'Active_Reflective.ILSF17AR5',
                    'Active_Reflective.ILSF21AR6',
                    'Active_Reflective.ILSF25AR7',
                    'Active_Reflective.ILSF29AR8',
                    'Active_Reflective.ILSF33AR9',
                    'Active_Reflective.ILSF37AR10',
                    'Active_Reflective.ILSF41AR11']

        SI_names = ['Sensory_Intuitive.ILSF2SI1',
                    'Sensory_Intuitive.ILSF6SI2',
                    'Sensory_Intuitive.ILSF10SI3',
                    'Sensory_Intuitive.ILSF14SI4',
                    'Sensory_Intuitive.ILSF18SI5',
                    'Sensory_Intuitive.ILSF22SI6',
                    'Sensory_Intuitive.ILSF26SI7',
                    'Sensory_Intuitive.ILSF30SI8',
                    'Sensory_Intuitive.ILSF34SI9',
                    'Sensory_Intuitive.ILSF38SI10',
                    'Sensory_Intuitive.ILSF42SI11']

        VV_names = ['Visual_verbal.ILSF3VV1',
                    'Visual_verbal.ILSF7VV2',
                    'Visual_verbal.ILSF11VV3',
                    'Visual_verbal.ILSF15VV4',
                    'Visual_verbal.ILSF19VV5',
                    'Visual_verbal.ILSF23VV6',
                    'Visual_verbal.ILSF27VV7',
                    'Visual_verbal.ILSF31VV8',
                    'Visual_verbal.ILSF35VV9',
                    'Visual_verbal.ILSF39VV10',
                    'Visual_verbal.ILSF3VV11']

        SG_names = ['Sequenz_Global.ILSF4SG1',
                    'Sequenz_Global.ILSF8SG2',
                    'Sequenz_Global.ILSF12SG3',
                    'Sequenz_Global.ILSF16SG4',
                    'Sequenz_Global.ILSF20SG5',
                    'Sequenz_Global.ILSF24SG6',
                    'Sequenz_Global.ILSF28SG7',
                    'Sequenz_Global.ILSF32SG8',
                    'Sequenz_Global.ILSF36SG9',
                    'Sequenz_Global.ILSF40SG10',
                    'Sequenz_Global.ILSF44SG11']

        # local node of AR to get results
        str_local_target = 'Active_Reflective.Score_active_reflective_11'
        labels_AR = ['a' 'a' 'a' 'a' 'a' 'b' 'a' 'a' 'a' 'a' 'b']

        # we consider a case of evidence
        #process_case_1 (dom, target)


        AR = process_case_1(dom, target, AR_names, labels_AR,
                            str_local_target=str_local_target,
                            str_dim_output=score_nodes[0])
        # clean up any memory allocations
        dom.delete ()
    except HuginException:
        print("A Hugin Exception was raised!")
        raise

    # all done
    print ('Done, thank you!')
