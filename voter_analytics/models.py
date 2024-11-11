# File: voter_analytics/models.py
# Author: Samhitha Somavarapu (samhitha@bu.edu), 11/11/2024
# Define the data objects for the voter_analytics application.
from django.db import models

# Create your models here.
class Voter(models.Model):
    '''
    Store/represent the data from one voter in Newton, MA.
    Last name, first name, address number, street name, 
    apartment number, ZIP code, date of birth, date of 
    registration, party affiliation, precinct number, whether
    or not voted in v20state; v21town; v21primary; v22general;
    v23town, and voter score.
    '''
    # identification
    last = models.TextField()
    first = models.TextField()
    adNumber = models.IntegerField()
    street = models.TextField()
    aptNum = models.CharField(max_length=6, blank=True, null=True)
    zipCode = models.IntegerField()
    dob = models.DateField()
    dor = models.DateField()
    party = models.CharField(max_length=2)
    precinct = models.CharField(max_length=2)
    v20state = models.BooleanField(default=False) 
    v21town = models.BooleanField(default=False)
    v21primary = models.BooleanField(default=False)
    v22general = models.BooleanField(default=False)
    v23town = models.BooleanField(default=False)
    voter_score = models.IntegerField(blank=True, null=True)
    

    def __str__(self):
        '''Return a string representation of this model instance.'''
        return f'{self.first} {self.last} | Party: {self.party} | Voter score: {self.voter_score}'

def load_data():
    '''Load data records from a CSV file into model instances.'''

    # Delete previous values (clean slate)
    Voter.objects.all().delete()
    filename = "C:/Users/samso/django/newton_voters.csv"

    f = open(filename)
    headers = f.readline() # read/discard headers
    print(headers)

    # loop to read all the lines in the file
    for line in f:

        # provide protection around code that might generate an exception
        try:
            fields = line.split(',')

            # create a new instance of Voter object with this info from CSV
            voter = Voter(last=fields[1].title(), first=fields[2].title(), adNumber=fields[3],
                            street=fields[4].title(), aptNum=fields[5].strip(), zipCode=fields[6], 
                            dob=fields[7], dor=fields[8], party=fields[9].strip(), 
                            precinct=fields[10], v20state=(fields[11]=="TRUE"), v21town=(fields[12]=="TRUE"),
                            v21primary=(fields[13]=="TRUE"), v22general=(fields[14]=="TRUE"),
                            v23town=(fields[15]=="TRUE"), voter_score=fields[16])
   
            voter.save() # save to database
            print(f'Created voter: {voter}')
        # handles the exception and prints what it is
        except Exception as e:
            print(f"Exception on {fields}: {e}")