from django.db import models
from django.conf import settings


class HolidayHousing(models.Model):

    class HousingType(models.TextChoices):
        FLAT = 'F', 'flat'
        HOUSE = 'H', 'house'
        SPECIALLOCATION = 'S', 'special location'

    type = models.CharField(
        max_length=1,
        choices=HousingType
    )

    class CostType(models.TextChoices):
        CHEAP = 'C', 'cheap'
        AFFORDABLE = 'A', 'affordable'
        EXPENSIVE = 'E', 'expensive'
        LUXURY = 'L', 'luxury'

    costs = models.CharField(
        max_length=1,
        choices=CostType
    )

    class LocationType(models.TextChoices):
        METROPOLIS = 'M', 'metropolis'
        VILLAGE = 'V', 'village'
        NATURE = 'N', 'nature'

    location = models.CharField(
        max_length=1,
        choices=LocationType
    )

    title = models.CharField(max_length=50)

    rooms = models.IntegerField()

    specials = models.CharField(max_length=50)

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='holiday_housings',  # -> user.holiday_housings.all()
        related_query_name='holiday_housing',  # -> User.objects.filter(holiday_housing__location='N')
    )

    class Meta:
        ordering = ['costs', 'type', 'location']
        verbose_name = 'Holiday Housing'
        verbose_name_plural = 'Holiday Housings'

    def __str__(self):

        def get_str_for_rooms():

            if self.rooms > 1:
                return 'rooms'

            return 'room'

        return f'{self.title} - {self.get_costs_display()} {self.rooms} {get_str_for_rooms()} {self.get_type_display()} in {self.get_location_display()}'

    def __repr__(self):
        return f'{self.title} / Location: {self.get_location_display()} / Costs: {self.get_costs_display()} / Type: {self.get_type_display()} / Rooms: {self.rooms} / Specials: {self.specials}'
