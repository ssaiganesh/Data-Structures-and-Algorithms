"""

Stack Data Structures

D
C
B
A

to access A , take D out first then C and so on. 
this is called popping 
A B C D

to push on stack:

D
C
B
A

Take note of push and pop
"""

class Stack():
    def __init__(self):
        self.items = [] 
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        return self.items == [] #Stack.is_empty() returns true if items is empty list as == is boolean operator
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    def get_stack(self):
        return self.items

s = Stack()
s.push("A")
s.push("B")

print(s.get_stack())


s.push("C")
print(s.get_stack())

s.pop()

print(s.get_stack())
s.pop()
s.pop()
print(s.is_empty()) #True because list is empty
s.push("A")
print(s.is_empty())
s.push('B')
s.push('C')
s.push('D')
print(s.peek()
s.pop()
s.pop()
s.pop()
s.pop()

#____________________________________________________________________________________________________________________________________________________
"""
Use a stack to check whether or not a string
has balanced usage of parenthesis.

Example:

    (), ()(), (({[]}))  <- Balanced.

    ((), {{{)}], [][]]] <- Not Balanced.

Balanced Example: {[]}
Non-Balanced Example: (()
Non-Balanced Example: ))
"""
#_____________________________________________________________________________________________________________________________________________
#MY CODE w/o stack class:
user_input = input('Enter the parantheses: ') #inputs parantheses
length_input = len(user_input) #length -1 as index starts from 0

#This function checks for the opposite parantheses
def opp_paran(p):
    if p == '(':
        return ')'
    elif p == '{':
        return '}'
    elif p == '[':
        return ']'
    
#Checks balance of user input
def check_balance(user_input, length_input):
    if length_input % 2 == 0:
        for i in range(length_input):
            if i<length_input//2:
                if user_input[length_input - i - 1] != opp_paran(user_input[i]):
                    return False
            else:
                return True
    else:
        return True


if check_balance(user_input, length_input):
    print('Balanced.')
else:
    print('Not Balanced.')
#____________________________________________________________________________________________________________________________________
#Given Answer by making use of stack classs:

def is_match(p1,p2):
    return True if p1+p2 in ['()','[]','{}'] else False

def is_paren_balanced(user_input):
    t = Stack()
    is_balanced = True
    index = 0
    
    while index < len(user_input) and is_balanced:
        paren = user_input[index]
        if paren in '{([':
            t.push(paren)
        else:
            if t.is_empty():
                is_balanced = False
            else:
                top = t.pop()
                if not is_match(top, paren):
                    is_balanced = False
        index += 1
    if t.is_empty() and is_balanced:
        return True
    else:
        return False


print(is_paren_balanced(user_input))
"""
Use a stack data structure to convert integer values to binary.

Example: 242 
"""
# My Code using stack:

user_int = int(input('Enter your integer: '))
def bin_(int_input):
    r = Stack()
    while int_input > 0:
        remainder = int_input % 2
        r.push(remainder)
        int_input = int_input // 2
    return r.get_stack()
final_list = bin_(user_int)
final_ans = ''.join(map(str,final_list[::-1])) #take note of this 1 line code to convert list to str. 
print(final_ans)

#What i can take note for my code is that i did not make use of pop which can include in my code to further make use of the stack algo 

#Given code:

dec_num  = int(input("Enter your integer: "))
def div_by_2(dec_num):
    p =  Stack()

    while dec_num > 0:
        remainder = dec_num % 2
        p.push(remainder)
        dec_num = dec_num // 2
    bin_num = ''
    while not p.is_empty():
        bin_num += str(p.pop())
    
    return bin_num 

print(div_by_2(dec_num))

"""
input_str = "Hello"
output = "olleH" using stack 

usually use without stack:
#print(input_str[::-1])

but with stack
"""
# My Answer with stack:
user_input = input('Enter the string: ')
def rev_string(user_input):
    t = Stack()
    for s in user_input:
        t.push(s)
    final_ans = ""
    while not t.is_empty():   
        final_ans += t.pop()
    return final_ans

print(reverse_string(user_input))


#Given Answer with stack:

def reverse_string(stack, input_str):
    for i in range(len(input_str)):
        stack.push(input_str[i])
    rev_str = ''
    while not stack.is_empty():
        rev_str += stack.pop()
    return rev_str
stack = Stack()
input_str = input('String:')

print(reverse_string(stack, input_str))

#For me to take note: 
#From list to string:
# stringname = ''.join(map(str, listname))