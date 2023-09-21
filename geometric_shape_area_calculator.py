#geometric_shape_area_calculator

import math # DO NOT MODIFY

def main():
    circle_pi = math.pi # DO NOT MODIFY, this line of code is assigning the variable 'circle_pi' equal to Pi ~3.14

    # TODO: In terminal, print Welcome to the geometric shape area calculator!
    print('Welcome to the geometric shape area calculator!')
    # User Options
    # Circle = 1
    # Rectangle = 2
    # Triangle = 3
    
    # TODO: Using one print statement, use string concatenation to print the options only 
    # as a single string (make sure to add a space between each option)
    print('Circle = 1', 'Rectangle = 2', 'Triangle = 3')
    # TODO: In terminal, ask the user "Select a shape by entering 1, 2, or 3' and assign the input to a new variable named 'choice'.
    choice = input("Select a shape by entering 1, 2, or 3 ")
    
    # TODO: Convert the variable 'choice' to an integer data type.
    choice = int(choice)
    
    # TODO: With one line of code, verify the variable 'choice' is indeed the data type integer, use conditional logic and print the output.  If converted correctly, the output in Terminal should read 'True'.
    if choice is int:
        print(True)
    
    # Calculate the area of a circle
    # TODO: Assign a new variable named 'radius' and ask for the user's input for the radius of the circle.       
    # TODO: Convert 'radius' to float.
    # TODO: Assign a new variable named 'area' and implement the logic to calculate the area of a circle. 
    # HINT 1 : The formula to find area of a circle: 'circle_pi' times radius squared     
    # 
    if choice == 1:  #DO NOT REMOVE THE 'IF
        radius = input('Enter the radius ')
        radius = float(radius)
        area = circle_pi * radius ** 2

    #  Hint 2 : circle_pi is a variable that has been assigned on Line 9 and equals Pi in math.     

    # Calculate the area of a rectangle
    # TODO: Assign new variables 'length' and 'width' and ask for the user's input for the length and width of the rectangle.
    # TODO: Convert both 'length' and 'width' to float.
    # TODO: Assign a new variable 'area' and implement the logic to calculate the area of a rectangle.
    # HINT: The formula to find the area of a rectangle: length times width   

    elif choice == 2: # DO NOT REMOVE THE 'ELIF'
        length = input("Enter the length of the rectangle ")
        width = input('Enter the width of the rectangle ')
        length = float(length)
        width = float(width)
        area = length * width
        
    # Calculate the area of a triangle
    # TODO: Assign new variables 'base' and 'height' and ask for the user's input for the base length and height of the triangle.
    # TODO: Convert both 'base' and 'height' to float.
    # TODO: Assign a new variable 'area' and implement the logic to calculate the area of a triangle.
    # HINT: The formula to find the area of a Triangle: half times base times height 
    elif choice == 3: #DO NOT REMOVE THE 'ELIF'
        base = input('Enter the base length of the triangle ')
        height = input('Enter the height of the triangle ')
        base = float(base)
        height = float(height)
        area = .5 * base * height 
    
    # TODO: If the user enters anything other than 1, 2 or 3, print statement "Invalid choice .       
    else:
        print("Invalid choice .")
            
    if choice in [1, 2, 3]: # DO NOT MODIFY
        print(f"The area is: {area:.2f} square units.") # DO NOT MODIFY"    
            
        
    # TODO: Print a statement explaining each step required to find and complete your technical assignments.  Be specific. 
    # print(f'To find our technical assignments you\n 1. Go to your module tab')
    print("To find our technical assignments\n 1. Go to your module tab and click it\n2. Find the Week and Day for the assignment your looking for. n3.You can go to either the Live Classes link, or below that the Assignment link\n4.Click on the link to that assignment\n5.When on the Live Classes option go to the last section called After Class. In  that section you will find the assignment.(example: Complete 🧑‍💻W4D2 After Class Exercise: Data Structures-Dictionary🧑‍💻). The Assignments page will have the matching name and date.\n6. Click on the link directly after the Click Here: statment. (example: Click here: W4D2: After Class Exercise)\n7. Accept the assignment.\n8. Go into your Repo on your github for Jusice through code.\n9. Once in the repo for your assignment, copy the link under the Green button <>Code and clone it into the folder you choose by cd <folder> and putting git clone <link> into the terminal.\n10. Once you've completed the assignment run python3 -m unittest, if it fails you will need to fix something in your code.\nIf it passes go to your terminal and enter git add ., git commit -m (whatever message here), git push.\n11. If it passes youll see a green check mark, if it doesnt youll see a red X and you will have to find the issue and fix it'\n12. Copy the link to your repo and in the actual assignment link on Canvas, click on the link saying Start Assignment and paste the link in Website URL")
  
        
if __name__ == "__main__": # DO NOT MODIFY
    main() # DO NOT MODIFY

