from django.db import models

# Create your models here.

class NotebookData(models.Model):
    brand = models.CharField(max_length=64,)
    descrition =models.CharField(max_length=64)
    typeNotebook =models.CharField(max_length=64)
    series = models.CharField(max_length=64)
    date = models.DateField()
    weight = models.CharField(max_length=64)
    def __str__(self):
        return f"brand = {self.brand} : descrition= {self.descrition} : type = {self.typeNotebook} : s = {self.series} : date = {self.date}"
    def getsearch(self):
        return f"{self.brand}{self.descrition}{self.typeNotebook}{self.series}{self.date}"
   
class Cpu (models.Model):
    brand = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    star =models.PositiveIntegerField()
    def __str__(self):
        return f"{self.brand} >> {self.name} >> {self.star}"
    def getsearch(self):
        return f"{self.brand}{self.name}{self.star}"

class Gpu (models.Model):
    brand = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    star =models.PositiveIntegerField()

    def __str__(self):
        return f"{self.brand} >> {self.name} >> {self.star}"
    def getsearch(self):
        return f"{self.brand}{self.name}{self.star}"

class Rom (models.Model):
    capacity = models.CharField(max_length=64)
    star =models.PositiveIntegerField()
    def __str__(self):
        return f"{self.capacity} >> {self.star}"
    def getsearch(self):
        return f"{self.capacity}{self.star}"

class Ram (models.Model):
    capacity = models.CharField(max_length=64)
    star =models.PositiveIntegerField()
    def __str__(self):
        return f"{self.capacity} >> {self.star}"
    def getsearch(self):
        return f"{self.capacity}{self.star}"

class Display (models.Model):
    size = models.CharField(max_length=64)
    resolution  = models.CharField(max_length=64)
    star = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.size} >>{self.resolution} >> {self.star}"
    def getsearch(self):
        return f"{self.size}{self.resolution}{self.star}"

class NoteBook (models.Model):
    notebookdata = models.ForeignKey(NotebookData,on_delete= models.CASCADE)
    cpu = models.ForeignKey(Cpu,on_delete= models.CASCADE)
    gpu = models.ForeignKey(Gpu,on_delete= models.CASCADE)
    rom = models.ForeignKey(Rom,on_delete= models.CASCADE)
    ram = models.ForeignKey(Ram,on_delete= models.CASCADE)
    display = models.ForeignKey(Display,on_delete= models.CASCADE)
    price = models.PositiveIntegerField()
    star = models.PositiveSmallIntegerField(default = 1)
    OStype = models.CharField(max_length = 64,default="") 
    
    def __str__(self):
        return f" data :: {self.notebookdata.brand} {self.notebookdata.series} | cpu :: {self.cpu.brand} {self.cpu.name} | gpu :: {self.gpu.brand} {self.gpu.name} | rom :: {self.rom.capacity} ram :: {self.ram.capacity}"

    def search(self,input):
        s = self.notebookdata.getsearch()+self.notebookdata.getsearch()+self.cpu.getsearch()+self.gpu.getsearch()+self.rom.getsearch()+self.ram.getsearch()+self.display.getsearch()
        s = s.lower()
        e = s.find(input)
        if e== -1:
            return False
        return True


class UserUn(models.Model):
    firstname = models.CharField(max_length = 64)
    lastname = models.CharField(max_length = 64)
    email = models.EmailField(max_length = 64)
    password = models.CharField(max_length = 32)
    favorite = models.ManyToManyField(NoteBook, related_name="userfavorite",blank=True)
    
    def __str__(self):
        return f"{self.firstname} {self.lastname} Email:{self.email}"
    
class Compare(models.Model):
    allstar = models.FloatField()
    notebook = models.OneToOneField(NoteBook,on_delete= models.CASCADE)
    
    def __str__(self):
        return f"{self.notebook} {self.allstar}"