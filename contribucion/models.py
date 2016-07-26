from django.db import models

# Create your models here.

class Autor(models.Model):
    orden = models.CharField(max_length=2)
    nombre = models.CharField(max_length=40)
    primer_apellido = models.CharField(max_length=40)
    segundo_apellido = models.CharField(max_length=40,blank=True)
    correo = models.EmailField(blank=True)
    institucion = models.CharField(max_length=200)

    class Meta:
        ordering = ["primer_apellido"]
        verbose_name_plural ="Autores"

    def __str__(self):
            return '%s %s %s' %(self.nombre, self.primer_apellido, self.segundo_apellido)


class Trabajo(models.Model):
    Areas_Tematicas_Choices = (
            ('1', 'Currículo médico'),
            ('2', 'Educación en ciencias básicas'),
            ('3', 'Formación clínica'),
            ('4', 'Desarrollo del profesionalismo y del comportamiento ético'),
            ('5', 'Educación orientada por competencias'),
            ('6', 'Procesos sociocognitivos y diseños instruccionales para el aprendizaje'),
            ('7', 'Internado médico de pregrado y Servicio Social'),
            ('8', 'Simulación en la formación de médicos'),
            ('9', 'Tecnologías de la información y las telecomunicaciones en la educación médica'),
            ('10', 'Evaluación del aprendizaje'),
            ('11', 'Alumnos como actores del proceso formativo'),
            ('12', 'Docentes como actores del proceso formativo'),
            ('13', 'Posgrado'),
            ('14', 'Desarrollo profesional continuado'),
            ('15',
             'Planeación, gestión, operación y evaluación, calidad y excelencia de las facultades y escuelas de medicina'),
            ('16', 'Internacionaliación de la educación médica'),
            ('17', 'Innovación y liderazco en educación médica'),
    )

    registro = models.CharField(max_length=4)
    titulo = models.CharField(max_length=250)
    area_tematica = models.CharField(max_length=2, choices=Areas_Tematicas_Choices)
    participantes = models.ManyToManyField(Autor, through = 'Contribucion')

    def __str__(self):
        return self.titulo


class Contribucion(models.Model):
    autores = models.ForeignKey(Autor)
    orden_autor = models.ForeignKey(Autor.orden)
    trabajo = models.ForeignKey(Trabajo)


