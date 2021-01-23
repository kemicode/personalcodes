#Name: Oluwakemi LaBadie
#Student ID Number: 00002489343
#Write a program that solves ' Acme auto pays sales persons 3.5% commission on thier sales
#assign the value to properly named constant. Sasha sold three cars. Write a program that
#prompts for the selling prices of the three cars and calculates her total sales and commission

#
#Pseudocode
#start Program
#
#prompt user for cost of 3 cars, assign to variable 'car_sales'
#prompt user for commission rate, assign to variable 'comm_rate'
#calculate pay = sales * comm_rate 
#output the total sales
#end of program

#start program

def main():
    #Prompt user for cost of three cars
    car_sale = float(input('Enter cost of three cars'))
    #prompt user for commission rate
    comm_rate = float(input('commission rate'))
    #calculate pay
    pay = car_sale * comm_rate
    #output the total sales for three cars
    print('The total sales for three cars is', pay)

    main()
    
    
