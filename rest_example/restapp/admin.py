from django.contrib.gis import admin
from .models import *
admin.site.register(random, admin.OSMGeoAdmin )
admin.site.register(village,admin.OSMGeoAdmin )
admin.site.register(Households, admin.OSMGeoAdmin )
admin.site.register(dumb, admin.OSMGeoAdmin )
admin.site.register(person, admin.OSMGeoAdmin )
admin.site.register(farm, admin.OSMGeoAdmin )
admin.site.register(points, admin.OSMGeoAdmin )
admin.site.register(well, admin.OSMGeoAdmin )
admin.site.register(wateryield, admin.OSMGeoAdmin )
# Register your models here.
