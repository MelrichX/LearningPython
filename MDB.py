

#region Project Descriptions

#Medical Diagnosis Bot (For Hydration)

###DESCRIPTION 1
#Diagnose users state of hydration based on questionnaire.
#Yes No questions
#Previous responses determine next questions
#Severe/some/no dehydration

###DESCRIPTION 2
#Be able to retrieve and add dehydration diagnoses
#Display a list of patients and diagnoses
#Store new diagnoses in the list

#endregion

#region Prompts & Variables
welcome_prompt = "Welcome Doctor, what would you like to do today?\n -To list all patients, press 1\n -To run a new diagnosis, press 2\n -To quit, press Q\n"
name_prompt = "What is the patient's name?\n"
appearance_prompt = "How is the patient's general appearance?\n 1: Normal\n 2: Irritable/Lethargic\n"
eye_prompt = "How is the patient's eyes?\n 1: Normal\n 2: Sunken/Dry\n"
skin_prompt = "How does the patient's skin react to a pinch?\n 1: Normal\n 2: Slowly\n"
prev_patients = {}

#endregion

def list_patients():
    print("Listing previous patients and diagnoses")
    for n, v in prev_patients.items():
        print(n, v)
    
#region Assesments
def assess_appearance():
    appearance = input(appearance_prompt)
    if appearance == "1":
        assess_eyes()

    elif appearance == "2":
        assess_skin()



def assess_eyes():
    eyes = input(eye_prompt)
    if eyes == "1":
        print("Patient is well Hydrated")
        prev_patients[name + ":"] = "Hydrated"

    elif eyes == "2":
        print("Patient is Severely Dehydrated")
        prev_patients[name + ":"] = "Severely Dehydrated"



def assess_skin():
    skin = input(skin_prompt)
    if skin == "1":
        print("Patient is Somewhat Dehydrated")
        prev_patients[name + ":"] = "Somewhat Dehydrated"

    
    elif skin == "2":
        print("Patient is Severely Dehydrated")
        prev_patients[name + ":"] = "Severely Dehydrated"
    
    else:
        return
#endregion


def new_diagnosis():
    global name
    name = input(name_prompt)
    assess_appearance()
    
    

def main():
    while(True):
        selection = input(welcome_prompt)
    
        if selection == "1":
            list_patients()
        elif selection == "2":
            new_diagnosis() 
        elif selection == "Q" or selection == "q":
            print("Goodbye!")
        else:
            return

main()
