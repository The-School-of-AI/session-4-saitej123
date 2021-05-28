# epai3session4

## Results :

### **with 'import test_session4' this can be fixed but we are not suppose to change test file**
=======================================short test summary info ==================================
FAILED test_session4.py::test_function_count - NameError: name 'test_session4' is not defined
FAILED test_session4.py::test_function_repeatations - NameError: name 'test_session4' is not defined
================================2 failed, 40 passed, 1 warning in 4.33s===========================
## Numeric Types II

1. Write a Qualean class that is inspired by Boolean+Quantum concepts. We can assign it only 3 possible real states. True, False, and Maybe (1, 0, -1) but it internally picks an imaginary state. The moment you assign it a real number, it immediately finds an imaginary number random.uniform(-1, 1) and multiplies with it and stores that number internally after using Bankers rounding to 10th decimal place. 
   1. It implements these functions (with exactly the same names)
      1. __and__,  __or__, __repr__, __str__, __add__, __eq__, __float__, __ge__, __gt__, __invertsign__, __le__, __lt__, __mul__, __sqrt__, __bool__
2. Your task is to write the above class, and then write all the functions. 
3. Then you need to write a test file, that tests all of the functions mentioned above + the other basic ones you have seen in the tests till now. Your unit test file must contain at least 25 tests, and they must not be repetitive. Some of the tests it must implement are:
   1. q + q + q ... 100 times = 100 * q
   2. q.__sqrt__() = Decimal(q).sqrt
   3. sum of 1 million different qs is very close to zero (use isclose)
   4. q1 and q2 returns False when q2 is not defined as well and q1 is False
   5. q1 or q2 returns True when q2 is not defined as well and q1 is not false
## Assignment Solution 

Here we are given functions __and__,  __or__, __repr__, __str__, __add__, __eq__, __float__, __ge__, __gt__, __invertsign__, __le__, __lt__, __mul__, __sqrt__ and __bool__ to implement inside a class named Qualean which takes in an integer (either 1,0 or -1 ) and randomly selects a number from range -1 to 1 and multiplies to that number. 

### **Functions**

* #### **__init__ function**:
    Here the number selected from the user is passed as the parameter, it is generally of type Decimal. user input and value are passed based on the logic "round(user_input * (random.uniform(-1, 1)), 10)" and validation error for input other than 0, 1, -1
* #### **__and__ function**: 
    The task of this function is to perform and operation, it takes in other_object as parameter. If self.value is not zero, then it proceeds to check for the other  value else via shorthand returns False. While checking the other_other, it checks whether it is an object of class Qualean and is not zero, if any of the condition fails it returns False, else it performs an and operation and returns the result.

* #### **__or__function**:
    The task of this function is to perform or operation, it takes in other_object as parameter. If self.value is zero, then it proceeds to check for the other  value else via shorthand returns True. While checking the other_other, it checks whether it is an object of class Qualean and is not zero, if any of the condition fails it returns False, else it performs an or operation and returns the result.
* #### **__add__ function**:
    This function takes in value as a parameter, This value is added to the original value i.e. self.value and final result is returned back.

* #### **__eq__ function**:
    This function checks whether the numbers are equal or not. It takes in other number as parameter. The other number is compared with self. 
* #### **__float__ function**:
    This function has the task to convert the data type of our value variable i.e. self.value, to float. The result is returned back.

* #### **__ge__ function**:
    This function takes in value as a parameter. The value variable is checked against self. value variable to check which whether self. value is greater than or equal to value. 

* #### **__gt__ function**:
    This function takes in value as a parameter. The value variable is checked against self. value variable to check which whether self. value is greater than value. 

* #### **__le__ function**:
    This function takes in value as a parameter. The value variable is checked against self. value variable to check which whether self. value is lesser than or equal to value. 

* #### **__lt__ function**:
    This function takes in value as a parameter. The value variable is checked against self. value variable to check which whether self. value is lesser than value. 

* #### **__invertsign__ function**:
    This function has the task to convert negative numbers positive and positive numbers negative. Once the conversion is done it returns the value

* #### **__mul__ function**:
    This function is similar as __add__ function, here the value parameter is multiplied with self.value and the result is returned back.

* #### **__sqrt__ function**:
    This function has the task to get the square root of the number. If self.value number is negative, it converts the number to positive, performs the square root and returns the result with an 'i' added in the result. Whereas if the number is positive, it follows the same process where as i is not added here. The result directly is returned back.

* #### **__bool__ function**:
    This function is used to convert the self.value variable to boolean value

### **Testcases**:
 #### **test_readme_proper_description**:
    The task of this function is to check whether the content of the readme is relevant to the code implemented or not. It will do a word check over the README file from a list containing important words which should be present in the documentation. 

 #### **test_function_bool**:
    This function checked the boolean value and return, so if the object is not zero, it will return True, therefore here it is being tested for user choice as either 1 or -1

 #### **test_readme_file_for_formatting**:
    The task of this function is to check whether the formatting has been done properly in the documentation i.e. headings and subheadings. It does so any counting the number of hashed. Here we are checking that the documentation should have minimum of **150** hashed. 

 #### **test_indentations**:
    Python is very prone to indentation errors to do improper use of tabs and spaces. Hence this function is implemented to check indentation is properly maintained, throughout the code. It counts the number of spaces before and statement and checks if that is a multiple of 4, if yes there there shouldn't be any indentation issues thus the test is passed else fail. 

 #### **test_qualean_repr**:
    This test is to check the representation of the qualean class. It should be displaying the old output which was displaying the meory it was stored in. 
 #### **test_function_add**:
    This function is written to check the add functionality of the class. Here the random number is generated and is passed as a parameter to the __add__ function. The add function adds its value with the self.value and returns. We are verifying the value of add function with manually adding those numbers and checking its equality.

 #### **test_function_eq**:
    This test is to check __eq__ function, It will be one in a million or more than that to get the same random number twice, hence we compare self.value with a random number and it should return false to be considered as Pass. 
#### **test_function_float**:
    This test is designed to check the __float__ functionality. The __float__  function converts the decimal type to float, hence here we assert the type of the number to be float.
 #### **test_function_gt**:
    This test is to check __gt__ function. Here r1 is an object of Qualean class initialized with random user choice from either 1 or -1, where as r2 is initialized with user choice as 0. So if r2.value is negative, then r1 should be greater than r2 and vice versa.

 #### **test_function_invertsign**:
    This test function checks __invertsign__ function, Here r1 is initialized randomly with a user choice and inverting function is called. The output should be a positive number should become negative and a negative number should become positive. 

 #### **test_less_than_equal_function test**:
    This test is to check __le__ function. Here r1 is an object of Qualean class initialized with random user choice, where as r2 is initialized with user choice as 0. So if r2.value is positive, then r1 should be less than r2 and vice versa. 

 #### **test_function_le**:
    This test is to check __lt__ function. Here r1 is an object of Qualean class initialized with random user choice from either 1 or -1, where as r2 is initialized with user choice as 0. So if r2.value is negative or zero, then r2 should be less than r1 and vice versa. 

 #### **test_function_mul**:
    This test is very similar to test_add_function, here multiplication is the operation which is getting tested instead of addition.

#### **test_function_sqrt**:
    This test is to check the __sqrt__function. Here qualean class is initialized a random user choice and __sqret function is called. We get the value of quanlean class with get_item function. Thus we take that value convert it to decimal and check its square root. If both are same, then the test is considered pass. 
 #### **test_million_qualeans_sum**:
    In this test, we add random q values 1 million times and check its closeness with zero. As it is an addition operation, small numbers when added a million times will form a number greater than 0, hence this check should return False and that is considered as a pass.

 #### **test_million_qualeans_mul**:
    In this test, we multiply random q values 1 million times and check its closeness with zero. As it is a multiplication operation, small numbers when multiplied a million times will form a very small number close to zero, hence this check should return True and that is considered as a pass.

 #### **test_or_function_both_undefined**:
    This test is to check 'and' functionality. A Qualean class r1 is initialized with random user choice and r2 is some number which is not a Qualean object. The and function should return False on comparison.

 #### **test_and_function_q1_undefined test test**:
    This test is to check 'or' functionality. A Qualean class r2 is initialized with random user choice and r2 is a qualean object with value as 0. Thus and function should return False on comparison.
#### **test_function_lt_non_qualean**: 


#### **test_function_add_non_qualean**: 
  