from django.db import models

# Create your models here.

class NotebookData(models.Model):
    brand = models.CharField(max_length=64,)
    descrition =models.CharField(max_length=64)
    typeNotebook =models.CharField(max_length=64)
    series = models.CharField(max_length=64)
    date = models.DateField()
    def __str__(self):
        return f"{self.brand} >> {self.descrition}>> {self.typeNotebook} >> {self.series} >>{self.date}"

class Cpu (models.Model):
    brand = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    star =models.PositiveIntegerField()
    def __str__(self):
        return f"{self.brand} >>{self.name} >> {self.star}"

class Gpu (models.Model):
    brand = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    star =models.PositiveIntegerField()

    def __str__(self):
        return f"{self.brand} >>{self.name} >> {self.star}"


class Rom (models.Model):
    capacity = models.CharField(max_length=64)
    star =models.PositiveIntegerField()
    def __str__(self):
        return f"{self.capacity} >> {self.star}"

class Ram (models.Model):
    capacity = models.CharField(max_length=64)
    star =models.PositiveIntegerField()
    def __str__(self):
        return f"{self.capacity} >> {self.star}"

class Display (models.Model):
    size = models.CharField(max_length=64)
    resolution  = models.CharField(max_length=64)
    star = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.size} >>{self.resolution} >> {self.star}"

class NoteBook (models.Model):
    notebookdata = models.ForeignKey(NotebookData,on_delete= models.CASCADE)
    cpu = models.ForeignKey(Cpu,on_delete= models.CASCADE)
    gpu = models.ForeignKey(Gpu,on_delete= models.CASCADE)
    rom = models.ForeignKey(Rom,on_delete= models.CASCADE)
    ram = models.ForeignKey(Ram,on_delete= models.CASCADE)
    display = models.ForeignKey(Display,on_delete= models.CASCADE)
    price = models.PositiveIntegerField()
    def __str__(self):
        return f"{self.notebookdata} >>{self.cpu} >> {self.gpu} >>{self.rom}>>{self.ram}>>{self.display}>>{self.price}"




class UserUn(models.Model):
    firstname = models.CharField(max_length = 64)
    lastname = models.CharField(max_length = 64)
    email = models.EmailField(max_length = 64)
    password = models.CharField(max_length = 32)
    favarite = models.ManyToManyField(NoteBook, related_name="uerfavarite",blank=True)
    
    def __str__(self):
        return f"{self.firstname} {self.lastname} Email:{self.email}"



