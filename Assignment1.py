# Assignment Part-1
#Q1. Why do we call Python as a general purpose and high-level programming language?

#Answer- Python is a general purpose language because it can be used to create a different kind of variety codes and it is not specialized for any specific problems #and since it is easily understandable/readable for Humans we call it high level language.

#Q2. Why is Python called a dynamically typed language?

#Answer- Python is called as dynamically typrd language because python don't have any prblem if we dont declare the type of variable. Overall in python the type of #variable is determined only during runtime.

#Q3. List some pros and cons of Python programming language?

#Answer- Pros:
#			Beginner-friendly, easy to learn
#			Python enhances productivity
#			Python has vast collection of libraries
#			Free & Open Source, large community
#			Portable
#			Interpreted 
#		Cons:
#			Speed limitation
#			Runtime errors
#			Consumes lot of memory space
#			Not so strong with mobile computing

#Q4. In what all domains can we use Python?

#Answer- Web Development, Data Science, OS Development, Gaming, Scientific Programming.

#Q5. What are variable and how can we declare them?

#Answer- Variables are basically names given to memory location.

#		Below examples to declare variables-
		
		int_var = 45 
		float_var = 99.99
		string_var = 'India is going to win T20 World Cup 2022'

#Q6. How can we take an input from the user in Python?

#Answer- username = input("Enter Name")

#Q7. What is the default datatype of the value that has been taken as an input using input() function?

#Answer- String

#Q8. What is type casting?

#Answer- The conversion of one data type into the other data type is knowns as type casting.
		
		int_var = int_var + 10  
		casted_int_var = float(int_var)

#Q9. Can we take more than one input from the user using single input() function? If yes, how? If no, why?

#Answer- Yes we can take multiple input using single input() function.
#		We can use split method to achieve this.
#		e.g. a,b,c = input("Enter three values: ").split()

#Q10. What are keywords?

#Answer- Python Keywords are special reserved words that have specific meanings and purposes and can't be used for anything but those specific purposes.
#		e.g. if, else, elseif, True, False, and, or, break............. etc.

#Q11. Can we use keywords as a variable? Support your answer with reason.

#Answer- No, Python keywords holds special meaning in Python Programming and it define the syntax of the coding. So, we can't use them as variable.

#Q12. What is indentation? What's the use of indentaion in Python?

#Answer- Indentation refers to the spaces at the beginning of the code line. In Python Indentation play a very important role bacuase it indicate the blocks of #code/statement.

#Q13. How can we throw some output in Python?

#Answer- We can use the print statement to get the required output.

#Q14. What are operators in Python?

#Answer- Operators are special symbols in Python that carry out arithmetic or logical computations.

#		-Numerical Operators
#		-Assignment Operators
#		-Comparison Operators
#		-Logical Operators etc.

#Q15. What is difference between / and // operators?

#Answer- /	- Division - It will do the division and provide a float vale as output.
#		//	- Floor Division - It will do the division operation and rounds the result down to the nearest whole number.

#Q16. Write a code that gives following as an output.
#```
#iNeuroniNeuroniNeuroniNeuron
#```
#Answer-	print("iNeuroniNeuroniNeuroniNeuron")

#Q17. Write a code to take a number as an input from the user and check if the number is odd or even.

#Answer- 
	num = int(input("Enter a number: "))
		if (num % 2) == 0:
			print ("Entered number is even")
		else:
			print("Entered number is odd")
		

#Q18. What are boolean operator?

#Answer- AND, NOT, OR are boolean operators of Python.

#Q19. What will the output of the following?
#```
#1 or 0

#0 and 0

#True and False and True

#1 or 0 or 0
#```

#Answer- 1 or 0 = 1
#		0 and 0 = 0
#		True and False and True = False
#		1 or 0 or 0 = 1

#Q20. What are conditional statements in Python?

#Answer- Python supports the Mathematical logical conditions -
#		Eqauls - a==b
#		Not Equal - a != b
#		Less than - a < b
#		Greater than - a > b
#		Less than or equal to - a <= b
#		Greater than or equal to - a >= b
		
#		All above conditions we can use with Python conditional decision making statements like if, else, else if etc.
		
#Q21. What is use of 'if', 'elif' and 'else' keywords?

#Answer- If, elif, else keywords statements is used in python for decision making. Program will evaluate test expression and will execue the statements based on #conditions for multiple expressions.

#Q22. Write a code to take the age of person as an input and if age >= 18 display "I can vote". If age is < 18 display "I can't vote".

#Answer- 
	age = int(input("Hi!, What's your Age: "))
		if (age >=18 ):
			print ("I can vote")
		if (age < 18 ):
			print ("I can't vote")

#Q23. Write a code that displays the sum of all the even numbers from the given list.
#```
#numbers = [12, 75, 150, 180, 145, 525, 50]
#```

#Answer- 
	numbers = [12, 75, 150, 180, 145, 525, 50]
		sum = 0
		for values in numbers:
			if (values%2)==0:
				sum=sum+values
		print(sum)

#Q24. Write a code to take 3 numbers as an input from the user and display the greatest no as output.

#Answer- 
	num1,num2,num3 = input("Enter three numbers: ").split()
		if (num1 >= num2) and (num1 >= num3):
			larg=num1
		elif (num2 >= num1) and (num2 >= num3):
			larg=num2
		else:
			larg=num3
		print("The Largest Number is",larg)

#Q25. Write a program to display only those numbers from a list that satisfy the following conditions

#- The number must be divisible by five

#- If the number is greater than 150, then skip it and move to the next number

#- If the number is greater than 500, then stop the loop
#```
#numbers = [12, 75, 150, 180, 145, 525, 50]
#```
#Answer- 
number = [12, 75, 150, 180, 145, 525, 50]
for item in number:
    if item>500:
        break
    elif item>150:
        continue
    elif item%5==0:
        print(item)
