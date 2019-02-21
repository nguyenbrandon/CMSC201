#Name: Brandon Nguyen     Date: April 5th, 2016
def intToEnglish(number):
    #string = str(number); #converts integer to string
    num1 = number // 100;
    num2 = (number % 100) // 10;
    num3 = (number % 100) % 10;
    
    hundreds = {1:"One ", 2:"Two ", 3:"Three ", 4:"Four ",  
                5:"Five ", 6:"Six ", 7:"Seven ", 8:"Eight ", 9:"Nine ", 0:""}
    
    tenths = {9: "Ninety ", 8: "Eighty ", 7: "Seventy ", 6: "Sixty ", 5: "Fifty ", 
              4: "Fourty ", 3: "Thirty ", 2: "Twenty ", 0:""}
    
    tenths2 = {1:"Eleven", 2:"Twelve", 3:"Thirteen", 4:"Fourteen", 5:"Fifteen", 6:"Sixteen", 
               7:"Seventeen", 8:"Eighteen", 9:"Nineteen", 0:"Ten"}
    
    single = {1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 
              9:"Nine", 0:""}
 
    final = hundreds[num1];
    if num1 > 0:
        final += "Hundred ";
    
    if num2 == 1:
        final += tenths2[num3];
    else:
        final += tenths[num2];
        final += single[num3];
    
    return final;
            
def main():
    number = 1;
    while number != -1:
        number = int(input("Enter in a number (1-999 inclusive) or -1 to quit: "));
        if number != -1:
            result = intToEnglish(number);
            print(result);
            print();
main()