from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=70)

    latitude = models.CharField(max_length=70)
    longitude = models.CharField(max_length=70)

    street = models.CharField(max_length=70)
    city = models.CharField(verbose_name='City/Suburb', max_length=70)
    state = models.CharField(verbose_name='State/Region', max_length=70)
    postal = models.CharField(verbose_name='Zip/Postcode', max_length=70)

    phone = models.CharField(max_length=70, blank=True)
    website = models.CharField(max_length=70, blank=True)
    hours = models.CharField(max_length=70, blank=True)

    def __unicode__(self):
        return ''.join([
            self.name,
            ' (',
            self.city,
            ', ',
            self.state,
            ')',
        ])

