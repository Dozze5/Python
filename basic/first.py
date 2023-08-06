print("hello");

print('hello\v');

print(10+200);

print('10'+"67");

#comments are made using # in start

print(6/2);  #output of division is always floating numnber
#output---->  2.0


# forw ( / ) use for classical  divide
#double forw ( // ) use for floor division

print(15//2);
#output----> 7



# modulus( % ) for getting remainder

print(55%2);
#output-----> 1


#( ** ) used for getting power

print(2**7);

#it means 2 to the power of 7
#output----->128

#variable declaration

a = 10;
b = 20;

print(a+b);

# c = _ + a; #work in python shell


# n;//how to not declare

# print(n); 
# as n is not defined it will give----> NameError: name 'n' is not defined

print(14-3.5); #integer to float conversion if float present in eqn

# There is full support for floating point; operators with mixed 
# type operands convert the integer operand to floating point:

# output-----> 10.5

print("C:\some\name")
#output ----> c:\some
            # ame
            
# n character is treated as 'escape' 
#for to treat as char with slash use r in print() in start

print(r"C:\trait\name");
#output----->C:\trait\name

print("""\
    make a string literal
    hello""");

print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""");

# print("""\ some template """)
#will print exact the same output as it is witten

#output----->Usage: thingy [OPTIONS]
                # -h                        Display this usage message
                # -H hostname               Hostname to connect to
                
strg = 3*'anmol';
#concatenate 'anmol' 3 times
print(strg)
#output-----> anmolanmolanmol

strg = 'anmol'+3*'genius'
print(strg);
#output----->anmolgeniusgeniusgenius

# prefix = 'Py'
# prefix 'thon'  # can't concatenate a variable and a string literal
#   File "<stdin>", line 1
#     prefix 'thon'
#            ^^^^^^
# SyntaxError: invalid syntax


# ('un' * 3) 'ium'
#   File "<stdin>", line 1
#     ('un' * 3) 'ium'
                # ^^^
# SyntaxError: invalid syntax


s = "helloEveryoneNyan";

Wi = "python";

print(Wi[0]);
#output-----> p

print(Wi[-1]);#last index
# output----> n

print(Wi[-6])

#indexing structure
#  +---+---+---+---+---+---+
#  | P | y | t | h | o | n |
#  +---+---+---+---+---+---+
#    0   1   2   3   4   5   
#   -6  -5  -4  -3  -2  -1


#strings in python are immutable

#word = "Python"
# word[0] = 'J'
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'str' object does not support item assignment
# word[2:] = 'py'
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'str' object does not support item assignment

print(s[4:6])

print(s[0:len(s)])

#len() method return lengt of string

print('J'+s[1:])

print(s[:6]+'kya'+s[6:])
#output----> helloEkyaveryoneNyan
#                  ^^^  
#              added string



#Lists in pyhton

array = [1,2,4,2,6,3];

print(array)

 #structure and indexing
#    +---+---+---+---+---+---+
#    | 1 | 2 | 4 | 2 | 6 | 3 |
#    +---+---+---+---+---+---+
#      0   1   2   3   4   5
#     -6  -5  -4  -3  -2  -1

#list are mutable

array[-6] = 6**2;

print(array[:])

# output----> [36,2,4,2,6,3]
#              ^^
#             mutated from 1 to 36

#You can also add new items at the end of the list, 
# by using the append() method
array.append(4**5);
print(array)
# output----> [1,2,4,2,6,3,1024]