#########################################################
#                   Name: Julia Tierman                 #
#               College Name: Adrian College            #
#########################################################

#persons information
firstName = input('What is your first name? ')
lastName = input('What is your last name? ')
streetNum = input('What is your street number and the name of your street? ')
cityState = input('What is your city and state seperated by a comma? ')
zipp = input ('What is your zip? ')

#meter readings
start = input('What is your starting meter reading? (use whole numbers) ')
end = input('What is your ending meter reading? (use whole numbers) ')

try:
    starting = int(start)
    ending = int(end)
except:
    print('This is not a number')
    quit()

#Kwh Consumed    
electConsumed = ending - starting

#Average daily
dailyAverage = electConsumed / 30
dailyPeak = dailyAverage * .20
dailyMid = dailyAverage * .45
dailyOff = dailyAverage * .35

#daily price
dailypeakPrice = dailyPeak * .17
dailymidPrice = dailyMid * .11
dailyoffPrice = dailyOff * .08

averagedaily = dailypeakPrice + dailymidPrice + dailyoffPrice

#percentage use
onPeak = electConsumed * .20
midPeak = electConsumed * .45
offPeak = electConsumed * .35

#price per KWh
peakprice = onPeak * .17
midprice = midPeak * .11
offprice = offPeak * .08
onpeakPrice = float(peakprice)
midpeakPrice = float(midprice)
offpeakPrice = float(offprice)

#fixed charges
fee = 23.05
charge = 11.9
tax = float(.065)
fixed = float(fee)
Reg = float(charge)

#monthly consumption price 
monthlyPrice = onpeakPrice + midpeakPrice + offpeakPrice 
b4tax =  onpeakPrice + midpeakPrice + offpeakPrice  + fixed + Reg
taxPrice = tax * b4tax
total = taxPrice + b4tax

def clearz():
    import os
    os.system('cls')

def header():  
    #first line is blank to bring the bill down one line to see better
    print('                                                                       ')
    print('***********************************************************************')
    print('Name:    ',firstName + ' '+ lastName)
    print('Address: ',streetNum)
    print('         ',cityState + ' ' + zipp)
    print('***********************************************************************')
    print('-----------------------------------------------------------------------')
    print('---------------------------Electricity Bill----------------------------')
    print('Start Meter Reading:          ',starting)
    print('End Meter Reading:            ',ending)
    print('Monthly Electricity Consumption:          ',electConsumed,' KWh')
    print('Daily Electricity Consumption:           ',"%.2f"%dailyAverage,' KWh')
    print('Price per KWh:   $0.1125')
    print('Monthly electricity consumption price:                      $ ',"%.2f"%monthlyPrice)
    print('Fixed delivery fee:                                         $  23.05')
    print('Regulatory Charge:                                          $  11.9')
    print('Total electricity price:                                    $ ',"%.2f"%b4tax)
    print('Tax 6.5%:                                                   $ ',"%.2f"%taxPrice)
    print('Total Actual Electricty Charges:                            $ ',"%.2f"%total)
    print('-----------------------------------------------------------------------')
    print('----------------Detailed Monthly Electricity Consumption---------------')
    print('On Peak: 07:00 AM - 12:00 PM- consumption = ',"%.2f"%onPeak, 'KWh: $ ',"%.2f"%onpeakPrice)
    print('On Peak: 12:01 PM - 07:00 PM- consumption = ',"%.2f"%midPeak, 'KWh: $ ',"%.2f"%midpeakPrice)
    print('On Peak: 07:01 PM - 06:59 AM- consumption = ',"%.2f"%offPeak, 'KWh: $ ',"%.2f"%offpeakPrice)
    print('Total Monthly Consumption                                $ ',"%.2f"%monthlyPrice)
    print('-----------------------------------------------------------------------')
    print('----------------Average Daily Electricity Consumption------------------')
    print('On Peak: 07:00 AM - 12:00 PM- consumption = ',"%.2f"%dailyPeak, 'KWh:  $ ',"%.2f"%dailypeakPrice)
    print('On Peak: 12:01 PM - 07:00 PM- consumption = ',"%.2f"%dailyMid,  'KWh: $ ',"%.2f"%dailymidPrice)
    print('On Peak: 07:01 PM - 06:59 AM- consumption = ',"%.2f"%dailyOff,  'KWh: $ ',"%.2f"%dailyoffPrice)
    print('Average Daily Consumption                               $ ',"%.2f"%averagedaily)
    
clearz()
header()