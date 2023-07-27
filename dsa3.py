# #Q1. Write a program to find all pairs of an integer array whose sum is equal to a given number?------------------------

def sum_pairs(array , number , sum):
    for i in range(number):
        for j in range(i+1 , number):
            if array[i] + array[j] == sum:
                print("(",array[i],",",array[j],")",sep = "")
                
                
                
# example:
array = [1,3,5,4,6,7,8,6,5,4]
number = len(array)
sum = 10
sum_pairs(array, number, sum)


# #Q2. Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.


def ReverseArray(Array, first, last):
    while first < last:
        Array[first],Array[last] = Array[last],Array[first]
        
        first += 1
        last -= 1
        
# example:      
Array = [10,20,30,40,50,60,70]
print("Given array:",Array)
ReverseArray(Array, 0, 6)
print("Reversed array is:")
print(Array)


# #Q3. Write a program to check if two strings are a rotation of each other?----------------------------------------


def is_rotation(str1,str2):
    if len(str1) != len(str2):
        return False
    s = str1 + str1
    return  s

# example:
str1 = "ABCDEFG"
str2 = "DEFGABC"
if is_rotation(str1,str2):
    print("string is rotating of each other")
else:
    print("string is not rotating of each other")


# #Q4. Write a program to print the first non-repeated character from a string?  ---------------------------------------  



string = input("Enter the string: " )
l = len(string)
found = None

for i in string:
    if (string.count(i) == 1):
        print("the first founded string variable is: ",i)
        found = True
        break

if (found == False):
    print("there is non repeating char in string") 



# #Q5. Read about the Tower of Hanoi algorithm. Write a program to implement it.--------------------------------------



def TowerOfHanoi(n , from_rod, to_rod, aux_rod):
    if n == 1:
        print("Move disk 1 from rod",from_rod,"to rod",to_rod)
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk",n,"from rod",from_rod,"to rod",to_rod)
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)
    
n = int(input("enter the value of n:"))
TowerOfHanoi(n, 'A', 'C', 'B')


# #Q6. Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression.------------


def isOperator(x):

    if x == "+":
        return True

    if x == "-":
        return True

    if x == "/":
        return True

    if x == "*":
        return True

    return False

def postToPre(post_exp):

    s = []

    length = len(post_exp)

    for i in range(length):

        if (isOperator(post_exp[i])):

            op1 = s[-1]
            s.pop()
            op2 = s[-1]
            s.pop()
            temp = post_exp[i] + op2 + op1

            s.append(temp)

        else:

            s.append(post_exp[i])

    ans = ""
    for i in s:
        ans += i
    return ans

if __name__ == "__main__":

    post_exp = "AB+CD-"

    print("Prefix : ", postToPre(post_exp))


# #Q7. Write a program to convert prefix expression to infix expression.--------------------------------------


def prefixToInfix(prefix):
    stack = []

    i = len(prefix) - 1
    while i >= 0:
        if not isOperator(prefix[i]):

            stack.append(prefix[i])
            i -= 1
        else:

            string = "(" + stack.pop() + prefix[i] + stack.pop() + ")"
            stack.append(string)
            i -= 1

    return stack.pop()

def isOperator(c):
    if c == "*" or c == "+" or c == "-" or c == "/" or c == "^" or c == "(" or c == ")":
        return True
    else:
        return False

if __name__=="__main__":
    string = "*-A/BC-/AKL"
    print(prefixToInfix(string))


# #Q8. Write a program to check if all the brackets are closed in a given code snippet.----------------------------------


def areBracketsBalanced(expr):
    stack = []

    for char in expr:
        if char in ["(", "{", "["]:

            stack.append(char)
        else:

            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '[':
                if char != "]":
                    return False

    if stack:
        return False
    return True

if __name__ == "__main__":
    expr = "{()}[]"

    if areBracketsBalanced(expr):
        print("Balanced")
    else:
        print("Not Balanced")   


# #Q9. Write a program to reverse a stack.-------------------------------------------------------------


class Stack:

    def __init__(self):
        self.Elements = []

    def push(self, value):
        self.Elements.append(value)
        
    def pop(self):
        return self.Elements.pop()
    
    def empty(self):
        return self.Elements == []

    def show(self):
        for value in reversed(self.Elements):
            print(value)

def BottomInsert(s, value):

    if s.empty():

        s.push(value)

    else:
        popped = s.pop()
        BottomInsert(s, value)
        s.push(popped)

def Reverse(s):
    if s.empty():
        pass
    else:
        popped = s.pop()
        Reverse(s)
        BottomInsert(s, popped)

stk = Stack()

stk.push(1)
stk.push(2)
stk.push(3)
stk.push(4)
stk.push(5)

print("Original Stack")
stk.show()

print("\nStack after Reversing")
Reverse(stk)
stk.show()

# #Q10. Write a program to find the smallest number using a stack.-----------------------------------------------------


First = []
num = int(input('How many numbers: '))

for n in range(num):
    numbers = int(input('Enter number: '))
    First.append(numbers)
    
print("Smallest number in the list is :  ", min(First))



# ----------------------------------------------------------------------------------------------------------------------------------

