import sys
import os
from domain.learnersModel.Lib.hugin94.pyhugin94 import *
import domain.learnersModel.read_answers as files
#from Lib.hugin94.pyhugin94 import *

#
# Parse listener for reading the network specification
#
def parse_listener(line, description):
    """A parse listener that prints the line number and error description."""
    print('Parse error line {}: {}'.format(line, description))


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
        print('A Hugin Exception was raised!')
        raise

    return dom


#
# case 1: enter evidence, propagate, and print the probability distribution of the target node
#
def process_case_1(dom, dimDict, str_local_target, bool_target, poles):
    """Process process_case_1"""
    # get handles to evidence node. We use "dot" notation to find a node by name

    print('\n===========================')
    print('===== process_case_1 ======')
    print('===========================\n')
    #
    # 1. Enter some evidence
    #  
    for name, label in dimDict.items():
        nd = dom.get_node_by_name(name)
        if nd is not None:
            idx = nd.get_state_index_from_label(label)
            if idx < 0:
                print(f'{label} not found as state of {name}')
            else:
                nd.select_state(idx)
                
        else:
            print(f'{name} not found')

    # propagate the evidence to compute posterior beliefs
    dom.propagate()
    print('\n') 
           
    # get local targets
    local_targets = []

    # we should test to None pointer, here we take the risk;-)
    local_targets.append(dom.get_node_by_name(str_local_target))  #new

    high_belif = 0.0
    high_score = 0.0

    # print the belief for each learning dimension
    for nd in local_targets:
        print(f'{nd.get_name ()}')        
        for i in range (nd.get_number_of_states()):            
            print(f'P({nd.get_state_value (i)}|e) = {nd.get_belief (i):.2f}')
            if nd.get_belief(i) > 0.30 and nd.get_belief(i) > high_belif :
                print(f'P({nd.get_state_value (i)}|e) = {nd.get_belief(i):.2f}')
                high_belif = nd.get_belief(i)
                high_score = nd.get_state_value(i)

        print ()

    # print beliefs for dim_FSLSM
    # get local targets

    bool_local_targets = []
    bool_local_targets.append(dom.get_node_by_name(bool_target))

    print ()
    Pole_of_Dim = ''
    for nd in bool_local_targets:
        print (f'{nd.get_name ()}')
        for i in range (nd.get_number_of_states ()):
            print (f'P({nd.get_state_label (i)}|e) = {nd.get_belief (i):.2f}')
            if nd.get_state_label (i) =='true' and nd.get_belief (i):
                Pole_of_Dim = poles['pole1']
            else:
                Pole_of_Dim = poles['pole2']
 
    # remember to remove any evidence and reset the domain
    dom.initialize()
    print('\nMit eine Probability: ', high_belif,' ist: ', Pole_of_Dim,':', high_score )
    result = {}
    result['Probability'] = high_belif
    result['Dimension_pole'] = Pole_of_Dim
    result['Dim_Score'] = high_score
    return result


# #
# # Main procedure
# #
# if __name__ == "__main__":
#     if len(sys.argv) == 0:
#         print ('usage: <oobn> <class> <target>')
#         exit ()

#     # map input to identifiers
#     specfile     = 'LearnProfile_cc.oobn' #sys.argv[1]   'LearnProfile_cc.oobn'
#     cls_name     = 'LearnProfile' #sys.argv[2]
#     target_name  = 'Result' # sys.argv[3]
    
     

#     try:
#         print ('Be patient. It is a large model;-)')
#         # read model and compile it for inference
#         dom = load_model (specfile, cls_name)
        
#         # get target
#         target = dom.get_node_by_name (target_name)
#         if target is None:
#             print (f'{target_name} not found')
#             exit ()

       

#         # we consider a case of evidence
#         AR_names, labels_AR, SI_names, labels_SI, VV_names, labels_VV,  SG_names, labels_SG = files.read_student_Answers()
#         result_stud =[]

#         score_nodes = ['Active_Reflective.Active_A_highest_11', 
#                       'Sensory_Intuitive.Sensitive_A_highest_11',
#                       'Visual_verbal.Visual_A_highest_11',
#                       'Sequenz_Global.Sequential_A_highest_11']
        
#         print('\n',AR_names,'\n');

#         for i in range (1):
            
#             print()           
            
#             AR = process_case_1 (dom, target, AR_names, labels_AR[i,:], str_local_target = 'Active_Reflective.Score_active_reflective_11',str_dim_output = score_nodes[0])            
#             SI = process_case_1 (dom, target, SI_names, labels_SI[i,:], str_local_target = 'Sensory_Intuitive.Score_Sensory_Intuitive_11',str_dim_output = score_nodes[1])
#             VV = process_case_1 (dom, target, VV_names, labels_VV[i,:], str_local_target = 'Visual_verbal.Score_visual_verbal_11',str_dim_output = score_nodes[2])
#             SG = process_case_1 (dom, target, SG_names, labels_SG[i,:], str_local_target = 'Sequenz_Global.Score_sequenz_Global_11', str_dim_output = score_nodes[3])
             
#             r = str(('Student_',i,':{',AR,SI,VV,SG,'}' ))
#             result_stud.append(r) 
#         #result_stud.append(str('Student_'+str(i)+'AR:'+AR+'SI:'+SI+'VV:'+VV+'SG:'+SG)) 
#         # clean up any memory allocations

#         print('\n\n',result_stud[0] )
#         dom.delete ()
#     except HuginException:
#         print('A Hugin Exception was raised!')
#         raise

#     # all done
#     print ('Done, thank you!')


class OOBN_model:

    def __init__(self, ils_answers) -> None:
        print('\n\n\n=========== Start! ================\n')
        
        self_result_ils_oobn ={}

        self.ils_answers_oobn = {}
        self.poles = {}
        self.ils_answers_oobn = self.get_ils_answers(ils_answers['ils_input_answers'])
        #print("\nVisual_verbal ils_input_answers:",  self.ils_answers_oobn)
        result = self.calulated_ILS('Visual_verbal',
                        'Score_visual_verbal',
                        'Visual_A_highest')
        
        self_result_ils_oobn['ils_input_answers'] = result
       
        #---------------------------------
        self.ils_answers_oobn = {}
        self.poles = {}
        self.ils_answers_oobn = self.get_ils_answers(
            ils_answers['ils_perception_answers'])

        #print("\n Sensory_Intuitive ils_perception_answers:", self.ils_answers_oobn)
        result = self.calulated_ILS('Sensory_Intuitive',
                           'Score_Sensory_Intuitive',
                           'Sensitive_A_highest')

        self_result_ils_oobn['ils_perception_answers'] = result

        #---------------------------------
        self.ils_answers_oobn = {}
        self.poles = {}
        self.ils_answers_oobn = self.get_ils_answers(
            ils_answers['ils_processing_answers'])
        #print('\nActive Reflective ils_processing_answers:', self.ils_answers_oobn)   
        
        result = self.calulated_ILS('Active_Reflective',
                           'Score_active_reflective',
                           'Active_A_highest')
        
        self_result_ils_oobn['ils_processing_answers'] = result

        #---------------------------------
        self.ils_answers_oobn = {}
        self.poles = {}
        self.ils_answers_oobn = self.get_ils_answers(
            ils_answers['ils_understanding_answers'])
        #print('\nGlobal_Secuential ils_understanding_answers:', self.ils_answers_oobn)
        result = self.calulated_ILS('Sequenz_Global',
                           'Score_sequenz_Global',
                           'Sequential_A_highest')
        self_result_ils_oobn['Sequenz_Global'] = result           

       
        print('\nResult:', self_result_ils_oobn) 
        print('Done Thank you!')
        print ('-----------------')

  

    def get_dimension(self,pole_1,str_dim_output, result):
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
    def get_ils_answers(self,ils_answers):
        """ assigne the answers of ILS """
         
        ils_answers_oobn = {}      
        node_name = ""
        for id, answer in ils_answers.items():
            if id.startswith("vv"):
                str_vv = id.upper()
                pos = str_vv.split('_')
                str_vv = "ILS"+pos[2]+pos[0]+pos[1]
                str_vv = "Visual_verbal."+str_vv       
                ils_answers_oobn[str_vv] = answer
                self.poles['pole1'] = 'Visual'
                self.poles['pole2'] = 'Verbal'
            if id.startswith("si"):
                str_si = id.upper()
                pos = str_si.split('_')
                str_si = "ILS"+pos[2]+pos[0]+pos[1]                
                str_si = "Sensory_Intuitive."+str_si
                ils_answers_oobn[str_si] = answer
                self.poles['pole1'] = 'Sensory'
                self.poles['pole2'] = 'Intuitive'
            if id.startswith("ar"):
                str_ar = id.upper()
                pos = str_ar.split('_')
                str_ar = "ILS"+pos[2]+pos[0]+pos[1]               
                str_ar = "Active_Reflective."+str_ar   
                ils_answers_oobn[str_ar] = answer
                self.poles['pole1'] = 'Active'
                self.poles['pole2'] = 'Reflective'
            if id.startswith("sg"):
                str_sg = id.upper()
                pos = str_sg.split('_')
                str_sg = "ILS"+pos[2]+pos[0]+pos[1]                
                str_sg = "Sequenz_Global."+str_sg     
                ils_answers_oobn[str_sg] = answer
                self.poles['pole1'] = 'Sequenz'
                self.poles['pole2'] = 'Global'        
       
        return ils_answers_oobn


    def get_list(DimDictionary):
        # Traversing through all the keys of the dictionary
        for dictKey in DimDictionary.keys():
            # appending each key to the list
            dictKeysList.append(dictKey)


    def get_score_name(self, name_dimension_ils,
                       Score_dimension,
                       Bool_first_pole):

        if(len(self.ils_answers_oobn) == 11):
            str_local_target = name_dimension_ils+'.'+Score_dimension+'_11'
            bool_local_target = name_dimension_ils+'.'+Bool_first_pole+'_11'
        else:
            str_local_target = name_dimension_ils+'.'+Score_dimension+'_5'
            bool_local_target = name_dimension_ils+'.'+Bool_first_pole+'_5'
        return str_local_target, bool_local_target

    def calulated_ILS(self, name_dimension_ils, Score_dimension, Bool_first_pole):
        """ calculate the answers of ILS """
      

        # map input to identifiers
        specfile = '../../domain/learnersModel/LearnProfile_cc.oobn'
        cls_name = 'LearnProfile'  # sys.argv[2]
        target_name = 'Result'  # sys.argv[3]

        try:
            print('Be patient. It is a large model;-)')
            # read model and compile it for inference
            dom = load_model(specfile, cls_name)

            # get target Booolean Result
            str_local_target, bool_target = self.get_score_name(name_dimension_ils,
                                                                Score_dimension,
                                                                Bool_first_pole)

            #print('\n\n====  Output Nodes: ====')

            #print('\n', 'str_local_target:', str_local_target,
            #      '\n', 'bool_target:', bool_target)

            # Validierung
            input_boolean_target = dom.get_node_by_name(target_name)
            if input_boolean_target is None:
                print(f'{input_boolean_target} not found')
                exit()

            score_nodes = ['Active_Reflective.Active_A_highest_11',
                           'Sensory_Intuitive.Sensitive_A_highest_11',
                           'Visual_verbal.Visual_A_highest_11',
                           'Sequenz_Global.Sequential_A_highest_11']

            Dimdict = self.ils_answers_oobn

            result = process_case_1(dom,
                                dimDict=Dimdict,
                                str_local_target=str_local_target,
                                bool_target=bool_target,
                                poles=self.poles)
            #clean up any memory allocations
            dom.delete()

        except HuginException:
            print('A Hugin Exception was raised!')
            raise

        # all done
        print('Done, thank you!')
        print('\n')
        return  result
