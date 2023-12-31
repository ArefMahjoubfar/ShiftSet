from random import randrange

class Individual():
    '''Lorem Ipsum'''
    def __init__(self, Limit_Days:list, Team_Tags:list, Reserve_Limitations_Priority:list, Individual_Sex) -> None:
        self.ID='I'+ str(randrange(100,1000)+'M' if Individual_Sex=='M' else 'F')
        self.Limit_Days= Limit_Days     # a list of days that the individual has limitation to have shift.
        self.N_Limit_Days=len(Limit_Days)
        self.TeamTags=Team_Tags     # a list of individuals ID who prefer to be in a team.
        self.Reserve_Limitations_Priority= Reserve_Limitations_Priority     # a list of preferations of that specific individual 
                                                                            # in situations which some limitations must break. break Tags or Limitation Days?
        self.sex=Individual_Sex     # being able to distribute the shifts according to the individuals' sex. it is shown in ID too.


class Course():
    '''Lorem Ipsum'''
    def __init__(self, N_Of_Indiv: int, Days:dict, Position_Categories:dict) -> None:
        self.N_Of_Indiv=N_Of_Indiv
        self.N_Of_Days=len(Days)
        self.Days=Days      # a dict of key: DayID, Value: a dict of that Day specific information.
        self.Position_Categories=Position_Categories        # a dict of key:Postion, value:a list of position difficulty, number of individuals in that position
        self.N_Position_Categories=len(Position_Categories)




class Day():
    '''Lorem Ipsum'''
    def __init__(self, Difficulty:int, Is_Holiday:bool, N_assigned_Indiv:int, Individuals_In_Pos:dict ) -> None:
        self.ID='D'+ str(randrange(100,1000))
        self.Meta={'Difficulty':Difficulty,
                   'Is_Holiday':Is_Holiday,
                   'N_assigned_Indiv':N_assigned_Indiv,
                   }
        self.Individuals=Individuals_In_Pos     # a dict of key:position categories, value: list of individuals for that position for that specific day
        


class DataLoader():
    '''from csv files. data of individuals, course days, coefficients and ...'''
    pass

class SetShift():
    
    pass


if __name__=='__main__':
    pass


