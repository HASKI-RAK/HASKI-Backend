import csv
import numpy as np

AR_names = []
labels_AR = []

SI_names = []
labels_SI = []

VV_names =[]
labels_VV = [] 


def read_student_Answers():
    
    #
    # we habe 21 student and for every 11 question for every dimension felder silverman
    #
    with open("Result_ILS_Answers.csv") as file:
        
        i = 0 
        labels = []

        csvreader = csv.reader(file)
        for row in csvreader:
            
            if(i==0 and row is not None):
                names = row.pop().split(';')
                
            elif (row is not None):
                labels.append(row.pop().split(';'))
                #print(len(labels), labels[0][:])
            i=i+1
    print(len(labels), labels[0][2])
    
    labels = np.array(labels) 
    #print("array size",labels[0,:] )


    #print(labels)
    AR_names, labels_AR = extract_subNames(names,labels, "AR", "Active_Reflective")
    SI_names, labels_SI = extract_subNames(names,labels, "SI", "Sensory_Intuitive")
    VV_names, labels_VV = extract_subNames(names,labels, "VV", "Visual_verbal")
    SG_names, labels_SG = extract_subNames(names,labels, "SG", "Sequenz_Global")
    
    return  AR_names, labels_AR, SI_names, labels_SI, VV_names, labels_VV,  SG_names, labels_SG


def extract_subNames(names, labels, str_dim, Node_name):
    subNames = []
    sub_idx = []
    labels_ =[]
    i = 0   
   
    for subName in names:
        if subName.__contains__(str_dim):
            subName = Node_name+"."+subName
            subNames.append(subName)
            sub_idx.append(i)
            #labels_ .append([labels[l][i] for l in range(len(labels))])  
            
        i=i+1

    
    sub_labels_ = labels[:,sub_idx[:]]
   
    print("---", sub_idx)
    print("array size",sub_labels_.shape)
    print("array size",sub_labels_[2,:])
    print("names", subNames)
    print("====================")
    
    if(len(subNames) == len(sub_labels_[0,:])):
       return subNames, sub_labels_

    return None, None 


# def get_student_answers(student_idx):

#  AR_names, 
#  labels_AR,
#  SI_names, 
#  labels_SI,
#  VV_names, 
#  labels_VV,  SG_names, labels_SG





read_student_Answers()


