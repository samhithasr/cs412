from django.db import models

# Create your models here.
class Voter(models.Model):
    '''
    Store/represent the data from one runner at the Chicago Marathon 2023.
    BIB,First Name,Last Name,CTZ,City,State,Gender,Division,
    Place Overall,Place Gender,Place Division,Start TOD,Finish TOD,Finish,HALF1,HALF2
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
    voter_score = models.IntegerField()
    # partyString = ""

    

    def __str__(self):
        '''Return a string representation of this model instance.'''
        return f'{self.first} {self.last} | Party: {self.party} | Voter score: {self.voter_score}'

def load_data():
    '''Load data records from a CSV file into model instances.'''

    Voter.objects.all().delete()
    # open the file for reading:
    # filename = "\Users\samso\Downloads\2023_chicago_results.csv"
    filename = "C:/Users/samso/django/newton_voters.csv"

    f = open(filename)
    headers = f.readline() # read/discard headers
    print(headers)
    # line = f.readline() # read a line for processing
    # fields = line.split(',') # create a list of fields
    # print(fields)

    # show the elements in this list of fields with index numbers
    # for i in range(len(fields)):
    #     print(f'fields[{i}] = {fields[i]}')

    # loop to read all the lines in the file
    for line in f:

        # provide protection around code that might generate an exception
        try:
            fields = line.split(',')

            # create a new instance of Result object with this record from CSV
            voter = Voter(last=fields[1].title(), first=fields[2].title(), adNumber=fields[3],
                            street=fields[4].title(), aptNum=fields[5], zipCode=fields[6], 
                            dob=fields[7], dor=fields[8], party=fields[9].strip(), 
                            precinct=fields[10], voter_score=fields[16])
   
            voter.save() # save to database
            print(f'Created result: {voter}')
        # handles the exception
        except Exception as e:
            print(f"Exception on {fields}: {e}")