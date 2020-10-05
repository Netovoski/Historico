from django.db import models
import datetime
# Create your models here.

class Historico(models.Model):

    sigla = models.CharField(max_length=4, blank=False)
    numVoo = models.CharField(max_length=200, null=True)
    type = models.CharField(max_length=200, blank=False)

    choices = (
        ('Realizada', 'Viagem Realizada'),
        ('Cancelada', 'Viagem Cancelada'),
    )

    status = models.CharField(max_length=10, choices=choices, default='Sem conhecimento')
    tipoLinha = models.CharField(max_length=50, default="Sem Dados")
    data_prevista = models.CharField(max_length=50)
    origem = models.CharField(max_length=50, null=False,blank=False)
    destino = models.CharField(max_length=50, null=False,blank=False)

    # class Meta:
    #     abstract = True

    def __str__(self):
        return 'Sigla: {0} numVoo: {1}'.format(self.sigla, self.numVoo)

class Hist_voo2015(Historico):
    pass

class Hist_voo2015_2(Historico):
    pass

class Hist_voo2015_3(Historico):
    pass

class Hist_voo2015_4(Historico):
    pass

class Hist_voo2015_5(Historico):
    pass

class Hist_voo2015_6(Historico):
    pass

class Hist_voo2015_7(Historico):
    pass

class Hist_voo2015_8(Historico):
    pass

class Hist_voo2015_9(Historico):
    pass

class Hist_voo2015_10(Historico):
    pass

class Hist_voo2015_11(Historico):
    pass

class Hist_voo2015_12(Historico):
    pass

class Hist_voo2016(Historico):
    pass

class Hist_voo2016_2(Historico):
    pass

class Hist_voo2016_3(Historico):
    pass

class Hist_voo2017(Historico):
    pass

class Hist_voo2018(Historico):
    pass

class Hist_voo2019(Historico):
    pass