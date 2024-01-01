#Libraries
from random import randrange
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
    def __init__(self, *, Name, Limit_Days:list, Team_Tags:list, Break_Limitations_Priority:list, Individual_Sex:str, N_Shifts:int) -> None:
       
        self.ID='I'+ str(next(ID_Generator)+'M' if Individual_Sex=='M' else 'F') # RAndom has to be edited... it can create identical IDs.#
        self.N_Shifts= N_Shifts
        self.Limit_Days= Limit_Days     # a list of days that the individual has limitation to have shift.
        self.N_Limit_Days=len(Limit_Days)
        self.TeamTags=Team_Tags     # a list of individuals ID who prefer to be in a team.
        self.Break_Limitations_Priority= Break_Limitations_Priority     # a list of preferations of that specific individual 
                                                                            # in situations which some limitations must break. break Tags or Limitation Days?
        self.sex=Individual_Sex     # being able to distribute the shifts according to the individuals' sex. it is shown in ID too.
        self.Name=Name # Name of the individual
        self.Limit_Score_Cal=len(Team_Tags)+len(Limit_Days)     # it returns an integer which shows overall view of how much limitation an individual has.
    
#-----------------------------------------------------------------------------------------------------------------------
class Team():
    '''Lorem Ipsum'''
    def __init__(self, Members:list) -> None:
        self.ID='T'+str(next(ID_Generator)) # RAndom has to be edited... it can create identical IDs.#
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
        self.Position_Categories={'ICU':[1,2], 'Endocrinology':[2,2], 'Pulmonology':[1,2], 'Hematology':[1,1]}   

        #Sources
        
        pass
    
    def Setter():

        pass

    def Counter():
        pass

    def Permission_Checker():
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

    def Early_Set(self, ):

        pass

    def Plot():
        pass

    def Start():
        pass



#-----------------------------------------------------------------------------------------------------------------------
def DataLoader(Individuals_File_Address, Days_File_Address):
    '''from csv files. data of individuals, course days, Difficulty coefficients and ...'''

    Individuals={}  # Total Individuals dict
    with open(Individuals_File_Address, encoding="utf8", newline='') as Individual_csvfile:
        Individuals_reader = csv.reader(Individual_csvfile, delimiter=',', quotechar='|')
        for row in Individuals_reader:
            Individual=Individual(Name=row[0],
                                  Limit_Days=[row[1],row[2]],       # this is for n=2. it can be replaced by a list callable by an specific index.
                                  Team_Tags=[row[3]],
                                  Break_Limitations_Priority=[row[4]], 
                                  Individual_Sex=[row[5]], 
                                  N_Shifts=row[6])
            Individuals.update({Individual.ID:Individual})   # adding the specific Individual to the Total Individuals Dict
    
    Days=[] # list of total Days of the course
    with open(Days_File_Address, encoding="utf8", newline='') as Day_csvfile:
        Day_reader= csv.reader(Day_csvfile, delimiter=',',quotechar='|')
        for row in Day_reader:
            Day=Day(Difficulty=row[1], 
                    Is_Holiday=[2], 
                    N_assigned_Indiv=row[3])
            Days.append(Day)        # adding the specific Day to the Total Individuals Dict
    

    Course = Course(N_Of_Indiv=len(Individuals), Days=Days, Position_Categories=SetShift.Position_Categories)

# Loading Data
DataLoader(r"C:\Users\Aref Mahjoubfar\Desktop\Data_sample-ShiftSet1.csv", r"C:\Users\Aref Mahjoubfar\Desktop\Data_sample-ShiftSet2.csv")



#-----------------------------------------------------------------------------------------------------------------------
if __name__=='__main__':
    pass

