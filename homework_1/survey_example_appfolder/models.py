from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

author = 'Lina Jeannot'
doc = 'This is my Homework 1 submission.'

class Constants(BaseConstants):
    name_in_url = 'Homework-1'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    counter = models.IntegerField(initial = 0)
    #this is how you can implement variables that can be used by every player
    #they are called group variables and useful for example when quota checking


class Player(BasePlayer):
    #this is the most important feature of this file. We can collect all the variables used on the html pages here
    
#The Variables are structured on the base of pages
    name_question = models.StringField(blank = True) #this is an optional field through blank = True
    seezeit_question = models.IntegerField(max=10, min=0)  #we can also have max and min guidelines
    lunch = models.IntegerField(initial=-999)  #we can add an initial value


    #custom error message
        #has to: 
        #1) be in the class Player (important to indent the right way)
        #2) have a specific name "variablename"_error_message
    def seezeit_question_error_message(player, value):
        if value > 5:
            return 'Did they let you eat more than 5 portions? Go and write them some nice feedback!'
                        