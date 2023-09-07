import sys
import os
import read_answers as files
from Lib.hugin94.pyhugin94 import *
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
def load_model(cc_name, class_name):
    """load modell."""
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
# Main procedure
#
if __name__ == "__main__":
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

       

        # we consider a case of evidence
        AR_names, labels_AR, SI_names, labels_SI, VV_names, labels_VV,  SG_names, labels_SG = files.read_student_Answers()
        result_stud =[]

        score_node = ['Active_Reflective.Active_A_highest_11', 
                      'Sensory_Intuitive.Sensitive_A_highest_11',
                      'Visual_verbal.Visual_A_highest_11',
                      'Sequenz_Global.Sequential_A_highest_11']

        for i in range (6):
            
            
            AR = process_case_1 (dom, target, AR_names, labels_AR[i,:], str_local_target = 'Active_Reflective.Score_active_reflective_11',str_dim_output = score_node[0])            
            SI = process_case_1 (dom, target, SI_names, labels_SI[i,:], str_local_target = 'Sensory_Intuitive.Score_Sensory_Intuitive_11',str_dim_output = score_node[1])
            VV = process_case_1 (dom, target, VV_names, labels_VV[i,:], str_local_target = 'Visual_verbal.Score_visual_verbal_11',str_dim_output = score_node[2])
            SG = process_case_1 (dom, target, SG_names, labels_SG[i,:], str_local_target = 'Sequenz_Global.Score_sequenz_Global_11', str_dim_output = score_node[3])
             
            r = str(('Student_',i,':{',AR,SI,VV,SG,'}' ))
            result_stud.append(r) 
        #result_stud.append(str('Student_'+str(i)+'AR:'+AR+'SI:'+SI+'VV:'+VV+'SG:'+SG)) 
        # clean up any memory allocations

        print("\n\n",result_stud[0] )
        dom.delete ()
    except HuginException:
        print("A Hugin Exception was raised!")
        raise

    # all done
    print ('Done, thank you!')
