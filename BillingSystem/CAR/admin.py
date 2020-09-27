from django.contrib import admin
from .models import customer,car

# Register your models here.
@admin.register(customer)
class customerAdmin(admin.ModelAdmin):
    list_display =[ 'CUS_ID','CUS_NAME','CUS_CITY','CUS_MO','CUS_EMAIL','CUS_STATE','CUS_Zip','date_modified']


@admin.register(car)
class carAdmin(admin.ModelAdmin):
     list_display =[
         'CAR_ID','CAR_MODEL','CAR_COLOUR','CAR_COMPANY','CAR_PRICE_OR','CAR_PRICE_EX','CAR_BOOKING_AMT','CAR_BOOKING_DATE', 'INS_COMPANY_NAME', 
    'INS_TYPE','INS_TOTAL_AMT','INS_TO_DATE','INS_FROM_DATE','RTO_REG_CHARGE','RTO_NUM_PLT_CHARGE','RTO_NUM_PLT_NO','RTO_ENG_NO','RTO_CHESSISE_NO','RTO_KEY_NO',   
    'RTO_BATTERY_NO', 'OTH_TRANS_CHARGE', 'OTH_DELIVERY_DATE', 'OTH_EXPENSE_NAME', 'OTH_EXPENSE_PRICE','date_modified','CUS_ID']