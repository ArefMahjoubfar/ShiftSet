#Libraries
import random
import datetime
import csv

#-----------------------------------------------------------------------------------------------------------------------
def ID_Generator(Start:int)->int:
    counter=Start
    while True:
        counter+=1
        yield counter
# Creating an ID_Generator obj. we use it in case of need.
ID_generator=ID_Generator(100)
#-----------------------------------------------------------------------------------------------------------------------
class Individual():
    '''Lorem Ipsum'''
    def __init__(self, *, Name, Limit_Days:list, Team_Tags:list, Break_Limitations_Priority:list, Individual_Sex:str, N_Shifts:int, Abs_limitation_days:list) -> None:
       
        self.ID='I'+ str(next(ID_Generator)+'M' if Individual_Sex=='M' else 'F')
        self.N_Shifts= N_Shifts
        self.Limit_Days= Limit_Days     # a list of days that the individual has limitation to have shift.
        self.N_Limit_Days=len(Limit_Days)
        self.TeamTags=Team_Tags     # a list of individuals ID who prefer to be in a team.
        self.Break_Limitations_Priority= Break_Limitations_Priority     # a list of preferations of that specific individual 
                                                                            # in situations which some limitations must break. break Tags or Limitation Days?
        self.sex=Individual_Sex     # being able to distribute the shifts according to the individuals' sex. it is shown in ID too.
        self.Name=Name # Name of the individual
        self.Limit_Score_Cal=len(Team_Tags)+len(Limit_Days)     # it returns an integer which shows overall view of how much limitation an individual has.
        self.Abs_limitation_days=Abs_limitation_days        # a list of absolute limitation days for that individual. it is unbreakable.
    
#-----------------------------------------------------------------------------------------------------------------------
class Team():
    '''Lorem Ipsum'''
    def __init__(self, Members:list) -> None:
        self.ID='T'+str(next(ID_Generator))
        self.Members= Members
        self.sex=[Members[i].sex for i in Members]      # a list of individuals' sex in the team.

#-----------------------------------------------------------------------------------------------------------------------
class Course():
    '''Lorem Ipsum'''
    def __init__(self, *, N_Of_Indiv: int, Days:dict, Position_Categories:dict) -> None:
        self.N_Of_Indiv=N_Of_Indiv
        self.Days=Days      # a dict of key: DayID, Value: a dict of that Day specific information.
        self.Position_Categories=Position_Categories        # a dict of key:Postion, value:a list of position difficulty, number of individuals in that position
        self.N_Position_Categories=len(Position_Categories)

#-----------------------------------------------------------------------------------------------------------------------
class Day():
    '''Lorem Ipsum'''
    def __init__(self, *,Difficulty:int, Is_Holiday:bool, N_assigned_Indiv:int, Individuals_In_Pos:dict={} ) -> None:
        self.ID='D'+ str(next(ID_Generator))
        self.Meta={'Difficulty':Difficulty,
                   'Is_Holiday':Is_Holiday,
                   'N_assigned_Indiv':N_assigned_Indiv,
                   }
        self.Individuals=Individuals_In_Pos     # a dict of key:position category, value: list of individuals for that position for that specific day
        

#-----------------------------------------------------------------------------------------------------------------------
class SetShift():
    '''Lorem Ipsum'''
    def __init__(self) -> None:
        #Parameters
        self.datetime=datetime.datetime.now()
        self.seed = 999 ###
        self.Storage_Address=r'' # where to store generated data(shifts)

        ### key: Position Category, Value: list: [number of individual for that position, difficuly score of that position]
        self.Position_Categories={'ICU':[1,2], 'Endocrinology':[2,2], 'Pulmonology':[1,2], 'Hematology':[1,1]}   # for now we have to input it manually.

        #Sources
        
        pass
    
    def Setter():

        pass
    
    def log():      # to show the status of setting shifts.
        pass

    def Counter(elements:dict)-> set:     # in-progress
        def update():
            updated_counter= None       # for now
            return updated_counter
        frequencies=None        # for now
        return frequencies,(weights:=None)    # for now: based on the individual's count of shifts. 

    def Permission_Checker(Temp_ID_Picked:str)->(bool, bool, bool, dict):       ### In-Progress # dont forget to inhibit selecting absolute limitation days
        pass

    def Compromiser():


        pass

    def Difficulty_Variance():
        pass

    def Difficulty_Cal():
        pass

    def Repair_Team():
        pass

    def Repair_Day_limit():
        pass

    def Plot():
        pass

    def Start():
        pass

    def Random_ID_Picker(elements):     #Done
        _, weights=SetShift.Counter(elements)
        return(random.choices(elements, weights=(weights), k=1))
    
    def Store(self,Day,Team_Picked):

        Shifts_Board=open(r'.csv','w', encoding='utf8') ### In-Progress
        Shifts_Board.write('\n',Day, ', ',Team_Picked)
        pass

    def Day_Capacity_status():      ###In-Progress
        
        pass
    
    def find_greatest_team(Teams):      # this func finds the the team with most members.
        # turn the Teams dict into a list, sort it based on the length of the values which are lists of members:
        Teams_ListForm_Sorted=sorted(list(Teams.items()), key= lambda x:len(x[1]), reverse=True)
        return Teams_ListForm_Sorted[0]     # returns the greatest team in a tuple of TeamID and Members 
    

    def Team_breaker(Team):    # this function breaks a team
        new_Team_ID = 'T'+ str(next(ID_generator))  # this ID belongs to the new team(members, n=2) that will be created.

        # randomly select two members of the team: -> a list
        Temp_selected_2_indiv=random.sample(Team, k=2)
        Temp_New_Team= {new_Team_ID:Temp_selected_2_indiv}  # 1st newly derived team. member number: 2
        Temp_Updated_Teams = Teams.copy()

        # it removes the 2 individuals(1st new derived team) we selected before from the Temp_Updated_Teams: i,e: the second new team derived:
        [Temp_Updated_Teams[0][1].remove(i) for i in Temp_selected_2_indiv]

        # Update Temp_Updated_Teams
        Temp_Updated_Teams.update(Temp_New_Team)

        return Temp_Updated_Teams
             

    def Early_Set():
        for Day in Days:
            Temp_Individuals=Individuals.copy()
            Remained_in_Lottery=Teams.copy()
            Remained_but_Partial_limitation=[]
            Individuals_picked_for_the_day=[]
            while True:
                if Remained_in_Lottery!={}:                                             #check if we can still find teams that satisfies reserving all limitation.
                    Temp_Team_Picked=SetShift.Random_ID_Picker(Remained_in_Lottery)
                    Is_Abs_limitation, Is_partial_limitation, Is_some_member_selected_yesterday, limited_indiv = SetShift.Permission_Checker(Temp_Team_Picked)
                    
                    if Is_some_member_selected_yesterday==True:     # if any member of that chosen temp_team was selected yesterday, we remove it from the temp team.
                        new_temp_team = Temp_Team_Picked.copy()
                        for indiv in limited_indiv:
                            new_temp_team.pop(indiv)
                    else:       # else just double name the Temp_Team_picked.
                        new_temp_team = Temp_Team_Picked

                    if Is_Abs_limitation == False and Is_partial_limitation==False:     #False and False: With considering all the limitation days and tags: OK
                        if SetShift.Day_Capacity_status>=len(new_temp_team):  # Be happy:)
                                SetShift.Store(Day,new_temp_team)
                                Individuals_picked_for_the_day.append(new_temp_team)
                        
                        if SetShift.Day_Capacity_status()=='Zero':
                            break
                    elif Is_Abs_limitation==True and Is_partial_limitation==False:   #True, False: absolute limitations: OK, but other limitation days not totally OK.
                        Remained_but_Partial_limitation.append(new_temp_team)
                        Remained_in_Lottery.pop(new_temp_team)

                    else:                                                                # False, False: when even absolute limitation days are not OK.
                        Remained_in_Lottery.pop(new_temp_team)
                else:                                                                    # now we try the teams whom have this day in their limitation days.
                    for Partial_limited_team in Remained_but_Partial_limitation:
                        while True:
                            if SetShift.Day_Capacity_status>=len(Partial_limited_team):  # Be happy:)
                                SetShift.Store(Day,Partial_limited_team)
                                Individuals_picked_for_the_day.append(Partial_limited_team)

                            if SetShift.Day_Capacity_status()=='Zero':
                                break

                            else:                                                        # this is when we should break some teams. :(
                                Teams_sorted =sorted(list(dict.items()),key=lambda x:len(x[1]),reverse=True)     # a list of key values of teams to sort them and find the team with most memebers.
                                Greatest_team = Teams_sorted[0][1]      # members of the team with most members
                                new_2_indiv_team = random.sample(Greatest_team[0][1],k=2)
                                new_remained_members_as_a_team=  for i in Greatest_team.pop(new) 

                                pass        ### in-progress: decide what tags should be broken
                                
            SetShift.Counter().update()     #updating the counter with this specific day information.
            for indiv in Temp_Individuals:
                Temp_Individuals.pop(indiv)        # this line is to prevent 48 hour shifts.    :)








#-----------------------------------------------------------------------------------------------------------------------
def DataLoader(Individuals_File_Address, Days_File_Address, Teams_File_Address):
    '''from csv files. data of individuals, course days, Difficulty coefficients and ...'''
    global Individuals
    Individuals={}  # Total Individuals dict
    with open(Individuals_File_Address, encoding="utf8", newline='') as Individual_csvfile:
        Individuals_reader = csv.reader(Individual_csvfile, delimiter=',', quotechar='|')
        for row in Individuals_reader:
            Individual=Individual(Name=row[0],
                                  Limit_Days=[row[1],row[2]],       # this is for n=2. it can be replaced by a list callable by an specific index.
                                  Team_Tags=[row[3]],
                                  Break_Limitations_Priority=[row[4]], 
                                  Individual_Sex=[row[5]], 
                                  N_Shifts=row[6],
                                  Abs_limitation_days=row[7])
            Individuals.update({Individual.ID:Individual})   # adding the specific Individual to the Total Individuals Dict
    global Days
    Days=[] # list of total Days of the course
    with open(Days_File_Address, encoding="utf8", newline='') as Days_csvfile:
        Day_reader= csv.reader(Days_csvfile, delimiter=',',quotechar='|')
        for row in Day_reader:
            Day=Day(Difficulty=row[1], 
                    Is_Holiday=[2], 
                    N_assigned_Indiv=row[3])
            Days.append(Day)        # adding the specific Day to the Total Individuals Dict
    

    global Teams
    Teams={}  # Total Individuals dict
    with open(Teams_File_Address, encoding="utf8", newline='') as Teams_csvfile:
        Teams_reader = csv.reader(Teams_csvfile, delimiter=',', quotechar='|')
        for row in Teams_reader:
            Team=Team(Members=row[0])
            Teams.update({Team.ID:Team})   # adding the specific Individual to the Total Individuals Dict
    Course = Course(N_Of_Indiv=len(Individuals), Days=Days, Position_Categories=SetShift.Position_Categories)

# Loading Data
DataLoader(r"C:\Users\Aref Mahjoubfar\Desktop\Data_sample-ShiftSet1.csv", r"C:\Users\Aref Mahjoubfar\Desktop\Data_sample-ShiftSet2.csv")



#-----------------------------------------------------------------------------------------------------------------------
if __name__=='__main__':
    pass
