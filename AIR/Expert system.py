#Name:- Omkar Bhagwat
#Rollno:-11
#AIR Assignment No-1

diseases={ 'Common Cold':['runny_nose','headache','fatigue','cough','fever','sore_throat'],
            'Flu':['fever','runny_nose','fatigue','headache','cough','muscle_ache'],
            'Diarrhea':['stomach_pain','watery_stool','nausea'],
            'Malaria':['fever','headache','nausea','tiredness','body-aches'],
            'Chickenpox':['red_spots','fever','fatigue','headache'],
            'Typhoid':['stomach_pain','headache','cough','loss_of_appetite','weakness'],
            'Jaundice':['stomach_pain','dark_coloured_urine','change_in_skin_color'],
            'Ear Infection':['fever','ear_pain','trouble_sleep'],
            'Skin Infection':['fluid_leaking_out_of_cut','red_skin','swelling'],
            'Dengue':['vomitting','tiredness','rash','joint_pain']
            }
def home_remedy(d):
    print("Home remedies:-\n")
    if d=="Common Cold":
        print("\n1.Warm bath can reduce cold symptoms in adults.")
        print("\n2.Take few slices of raw ginger and root in boiling water.")
        print("\n3.Drinking honey in tea with lemon can cause sore throat.")
    elif d=="Flu":
        print("\n1.Drint water and fluids to keep your nose, mouth and throat moist.")
        print("\n2.Get plenty of rest.")
        print("\n3.Rinse with salt water.")
    elif d=="Diarrhea":
        print("\n1.Rehydrating:-Drinking water or a person can also create an ORS.")
        print("\n2.A diet of small, frequent meals.")
        print("\n3.Have foods rich in pectin, potassium,cooked and soft vegeables.")
    elif d=="Malaria":
        print("\nMinor Malaria can be cured:")
        print("\n1.Boil ginger in water and drink 1-2 cups on a daily basis.")
        print("\n2.Have 2 cups of herbal tea or turmeric milk everyday.")
        print("\n3.Consume 2-3 glasses of orange juice, sweet lime juice or grapefruit juice on daily basis.")
    elif d=="Chickenpox":
        print("\n1.Don't scratch that itch.")
        print("\n2.Use a cool,wet washcloth on super-itchy areas to clam your skin.")
        print("\n3.Drink lots of fluids to help your body rif itself of the virus faster.")
    elif d=="Typhoid":
        print("\n1.Drink ORS")
        print("\n2.Add basil(tulsi) to boiled water and drink 3 to 4 cups daily.")
        print("\n3.Garlic speeds up recovery from typhoid due to its antioxidative properties.")
    elif d=="Jaundice":
        print("\n1.Taking lot of fluids like radish juice,gooseberry juice and lemon,fresh sugarcane juice")
        print("\n2.Papaya leaves help in eliminating toxins from bloodstream.")
        print("\n3.Take natural sunlight.")
    elif d=="Ear Infection":
        print("\n1.Heat from an electric hot pack can redice inflammation and pain in the ear.")
        print("\n2.Gentle massage can help with ear pain.")
        print("\n3.Try eating a clove of garlic each day.")
    elif d=="Skin Infecion":
        print("\n1.Apply cold compresses to your skin several times a day to reduce itching and inflammation.")
        print("\n2.Use topical creams and ointment to reduce itching and discomfort.")
    elif d=="Dengue":
        print("\n1.Drink sufficient water.")
        print("\n2.Drinking papaya juice.")
        print("\n3.Steep neem leaves and drink the brew to increase platelet and white blood cell count.")
    else:
        print("Consult a doctor...")

f=0
flag=0
symp_list=[]
print("Do you have any health-related issues?")
inpt=input('Enter y/n or Y/N:')
if(inpt=="y" or inpt=="Y"):
    print("Are you suffering from fever?")
    fever=input()
    if fever=="y" or fever=="Y":
        symp_list.append('fever')

    print("Are you suffering from headache?")
    headache=input()
    if headache=="y" or headache=="Y":
        symp_list.append('headache')

    print("Are you suffering from runny-nose?")
    runny_nose=input()
    if runny_nose=="y" or runny_nose=="Y":
        symp_list.append('runny_nose')

    print("Are you suffering from fatigue(extreme tiredness)?")
    fatigue=input()
    if fatigue=="y" or fatigue=="Y":
        symp_list.append('fatigue')

    print("Do you have cough?")
    cough=input()
    if cough=="y" or cough=="Y":
        symp_list.append('cough')

    print("Are you suffering from Muscle ache?")
    muscle_ache=input()
    if muscle_ache=="y" or muscle_ache=="Y":
        symp_list.append('muscle_ache')

    print("Are you suffering from sore_throat?")
    sore_throat=input()
    if sore_throat=="y" or sore_throat=="Y":
        symp_list.append('sore_throat')

    print("Do you have weakness?")
    weakness=input()
    if weakness=="y" or weakness=="Y":
        symp_list.append('weakness')

    print("Do you have pain in your ears?")
    ear_pain=input()
    if ear_pain=="y" or ear_pain=="Y":
        symp_list.append('ear_pain')

    print("Are you facing trouble while sleeping and losing your balance?")
    trouble_sleep=input()
    if trouble_sleep=="y" or trouble_sleep=="Y":
        symp_list.append('trouble_sleep')

    print("Is the fluid leaking out of your cut?")
    fluid_leaking_out_of_cut=input()
    if fluid_leaking_out_of_cut=="y" or fluid_leaking_out_of_cut=="Y":
        symp_list.append('fluid_leaking_out_of_cut')

    print("Is skin red around the injury?")
    red_skin=input()
    if red_skin=="y" or red_skin=="Y":
        symp_list.append('red_skin')

    print("Do you have swelling?")
    swelling=input()
    if swelling=="y" or swelling=="Y":
        symp_list.append('swelling')

    print("Do you feel loss of appetite?")
    loss_of_appetite=input()
    if loss_of_appetite=="y" or loss_of_appetite=="Y":
        symp_list.append('loss_of_appetite')

    print("Do you have red-spots on your body?")
    red_spots=input()
    if red_spots=="y" or red_spots=="Y":
        symp_list.append('red_spots')

    print("Are you suffering from stomach/abdominal pain?")
    stomach_pain=input()
    if stomach_pain=="y" or stomach_pain=="Y":
        symp_list.append('stomach_pain')

    print("Are you suffering from nausea?")
    nausea=input()
    if nausea=="y" or nausea=="Y":
        symp_list.append('nausea')

    print("Are you suffering from watery stools?")
    watery_stool=input()
    if watery_stool=="y" or watery_stool=="Y":
        symp_list.append('watery_stool')

    print("Are you suffering from dark colored urine?")
    dark_coloured_urine=input()
    if dark_coloured_urine=="y" or dark_coloured_urine=="Y":
        symp_list.append('dark_coloured_urine')

    print("Is there any change in skin color?")
    change_in_skin_color=input()
    if change_in_skin_color=="y" or change_in_skin_color=="Y":
        symp_list.append('change_in_skin_color')

    print("Are you suffering from vomitting?")
    vomitting=input()
    if vomitting=="y" or vomitting=="Y":
        symp_list.append('vomitting')

    print("Do you feel like tiredness?")
    tiredness=input()
    if tiredness=="y" or tiredness=="Y":
        symp_list.append('tiredness')

    print("Do you have rashes on your skin?")
    rash=input()
    if rash=="y" or rash=="Y":
        symp_list.append('rash')

    print("Are you suffering from joint pain?")
    joint_pain=input()
    if joint_pain=="y" or joint_pain=="Y":
        symp_list.append('joint_pain')

else:
    flag=1
    print("Great! Stay Safe and Stay Healthy....")

symp_list.sort()
for d in diseases.keys():
    diseases[d].sort()
    if diseases[d]==symp_list:
        print('\nOkay,You may be suffering from',d)
        print('\nDo you need any home remedy?')
        remedy=input('Enter y/n:')
        if(remedy=="y" or remedy=="Y"):
            home_remedy(d)
        else:
            print("Consult a Doctor...")
        f=0
        break
    else:
        f=1
if flag==0 and f==1:
    print("\nMay disease with these symptoms is not there in this list. I recommend you to go to Hospital and consult a doctor...\n\n")
