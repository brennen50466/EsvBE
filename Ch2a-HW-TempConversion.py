#------------------------------------------------------------
#Name: Esval, Brennen
#MIS 3301 – Fall 2022 
#Purpose: Temperature Conversion
#File: Ch2a-HW-TempConversion 
#--------------------------------------------------------------------

#------Constant------------------------------------------------------
CURRENT_YEAR = 2022


#---Title------------------------------------------------------------
print()
print('*******************************************************************')
print("       Victorino's Temperature Conversion Tool")
print()
print('Please input the values below...')
print()


#---Input------------------------------------------------------------
first_name = input('Enter first name: ')
last_name = input('Enter last name: ')
city = input('Enter city: ')
state = input('Enter state: ')
temp = int(input('Enter temperature (in Fahrenheit) : '))


#---Process---------------------------------------------------------
temp_cel = int((temp - 32) * (5/9))


#---Output----------------------------------------------------------
print()
print('----------------------------------------------------------------------')
print("Thank you for using Victorino's Temperature Conversion Tool!")
print()
print('The current temperature in ',city,' is...')
print('     ',temp,' (Fahrenheit)')
print('     ',temp_cel,' (Celcius)')
print()
print('>', CURRENT_YEAR,'report data entered by',first_name,last_name)
