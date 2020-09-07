from django.contrib import admin
from home.models import Contact
from home.models import Admission_details,Gallery,LatestNews_TopImage,LatestNews_column,LatestNews_box1,LatestNews_box2,Index_Profile1
# from home.models import Index_Profile2,Index_Profile3,Index_Profile4



admin.site.register(LatestNews_TopImage)
admin.site.register(LatestNews_column)
admin.site.register(LatestNews_box1)
admin.site.register(Index_Profile1)
# admin.site.register(Index_Profile2)
# admin.site.register(Index_Profile3)
# admin.site.register(Index_Profile4)


class Activitiy(admin.ModelAdmin):
   list_display = ('Img_title','Image')
   search_fields = ('Img_title','Image')

admin.site.register(Gallery, Activitiy)


class Admission_c(admin.ModelAdmin):
   list_display = ('name','EmailID','Mob_No')
   list_display_links = ('name','EmailID','Mob_No')
   search_fields = ('name','EmailID','Mob_No')


admin.site.register(Admission_details, Admission_c)


class Contact_c(admin.ModelAdmin):
    list_display = ('name1','email1','phone1')
    list_display_links = ('name1','email1','phone1')
    search_fields = ('name1','email1','phone1')


admin.site.register(Contact,Contact_c)



