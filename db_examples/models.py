from django.db import models

# Create your models here.
### banking application

class AccountOwner(models.Model):
    '''A person who owns zero to many bank accounts.'''

    name = models.CharField(max_length=120)
    ssn = models.CharField(max_length=9)

    def __str__(self):
        return self.name

    def get_accounts(self):
        return BankAccount.objects.filter(owner=self)

class BankAccount(models.Model):

    number = models.IntegerField()
    balance = models.FloatField()
    owner = models.ForeignKey(AccountOwner, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.number} ({self.owner})' # use of ForeignKey

###### courses and students ######

class Course(models.Model):

    number = models.CharField(max_length=12)
    name = models.CharField(max_length=120)
    # students = models.ManyToManyField('Student')

    def __str__(self):
        return f'{self.number}: {self.name}'

class Student(models.Model):

    name = models.CharField(max_length=120)
    # courses = models.ManyToManyField('Course')

    def __str__(self):
        return self.name

class Registration(models.Model):
    '''Represent the many-to-many relationship between Students and Courses
    as two one-to-many relationships: one Course to many Students;
                                      one Student to many Courses.
    '''

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    reg_date = models.DateField(auto_now_add=True)
    grade = models.CharField(max_length=2, blank=True)

    def __str__(self):
        return f'{self.course.number}, {self.student.name}'


###### geneology example ######

class Person(models.Model):

    name = models.CharField(max_length=120)
    mother = models.ForeignKey('Person', related_name='mother_person', null=True, blank=True, on_delete=models.CASCADE)
    father = models.ForeignKey('Person', related_name='father_person', null=True, blank=True, on_delete=models.CASCADE)
    # null is for the database definition; blank is for the Model form definition

    def __str__(self):
        if self.father and self.mother:
            return f'{self.name}, child of {self.mother.name} and {self.father.name}'
        elif self.father:
            return f'{self.name}, child of {self.father.name}'
        elif self.mother:
            return f'{self.name}, child of {self.mother.name}'
        else:
            return self.name