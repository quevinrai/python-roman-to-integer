# Roman to Integer

Convert Roman numerals to its equivalent integer which is **guaranteed** to be in the range of 1 through 3999.

## About the Project

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

| Symbol | Value |
| :------: | :------: |
| I | 1 |
| V | 5 |
| X | 10 |
| L | 50 |
| C | 100 |
| D | 500 |
| M | 1000 |

For example, 2 is written as **II** in Roman numeral, just two ones added together. 12 is written as **XII**, which is simply **X** + **II**. The number 27 is written as **XXVII**, which is **XX** + **V** + **II**.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not **IIII**. Instead, the number four is written as **IV**. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as **IX**. There are six instances where subtraction is used:

+ **I** can be placed before **V** (5) and **X** (10) to make 4 and 9. 
+ **X** can be placed before **L** (50) and **C** (100) to make 40 and 90. 
+ **C** can be placed before **D** (500) and **M** (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

## Installation

1. Clone the repo
    ```sh
    git clone https://github.com/quevinrai/python-roman-to-integer.git
    ```
2. In your IDE, open a terminal and run the project
    ```sh
    python main.py
    ```

## Usage

### Example 1:

    "------------------------------"
    "+  ROMAN NUMERAL TO INTEGER + "
    "------------------------------"

    Input: III
    Output: 3

    "------------------------------"
    " +         BREAKDOWN        + "
    "------------------------------"

    III     =     3
    

### Example 2:

    "------------------------------"
    "+  ROMAN NUMERAL TO INTEGER + "
    "------------------------------"
    
    Input: LVIII
    Output: 58
    
    "------------------------------"
    " +         BREAKDOWN        + "
    "------------------------------"

    L       =     50
    V       =     5
    III     =     3

### Example 3:

    "------------------------------"
    "+  ROMAN NUMERAL TO INTEGER + "
    "------------------------------"
    
    Input: MCMXCIV
    Output: 1994
    
    "------------------------------"
    " +         BREAKDOWN        + "
    "------------------------------"

    M      =     1000
    CM     =     900
    XC     =     90
    IV     =     4

## Rules

1. `1 <= s.length <= 15`
2. `'s'` contains only the characters `(I, V, X, L, C, D, M)`.
3. **D**, **L**, and **V** can only appear once.
4. M, C, X, or I may appear no more that three times consecutively in the string.
5. Only **I**, **X**, and **C** can be used for subtraction (V, L, and D cannot). Therefore, the following pairs of letter are invalid: **VX**, **VL**, **VC**, **VD**, **VM**, **LC**, **LD**, **LM**, **DM**.
6. When subtracting, the value of the letter being subtracted from cannot be more than 10 times the value of letter being used for subtraction. Therefore, the following pairs of letters are invalid: **IL**, **IC**, **ID**, **IM**, **XD**, **XM**.
7. Once a letter has been used as a subtraction modifier, that letter cannot appear again in the string, unless that letter itself is subtracted from. For example, **CDC** is not valid (you would be subtracting 100 from 500, then adding it right back) – but **CDXC** (for 490) is valid. Similarly, **XCX** is not valid, but **XCIX** is.
    - To summarize:
        - **C** cannot follow **CM** or **CD** except in case of **XC**.
        - **X** cannot follow **XC** or **XL** except in the case of **IX**.
8. Once a letter has been subtracted from, neither it nor the next lowest multiple of 5 may appear again in the string - so neither **X** nor **V** can follow **IX**, neither **C** nor **L** may follow **XC**, and neither **M** nor **D** may follow **CM**.
9. A letter cannot be used as a subtraction modifier if that letter, or the next highest multiple of 5, appears previously in the string - so **IV** or **IX** cannot follow **I** or **V**, **XL** or **XC** cannot follow **X** or **L**, and **CD** or **CM** cannot follow **C** or **D**.
10. The values of a roman numeral must be in descending order.
11. When going from big number to small number, add.
12. When going from small number to big number, subtract.

## Resources

- LeetCode Challenege 13: Roman to Integer ([link](https://leetcode.com/problems/roman-to-integer/?envType=featured-list&envId=challenges-for-new-users))
- TheVBProgrammer Programming Exercies: Roman Numerals ([link](https://www.thevbprogrammer.com/Ch08/08-10-RomanNumerals.htm#:~:text=Similarly%2C%20XCX%20is%20not%20valid,in%20the%20case%20of%20IX.))
- CalculatorSoup: Roman Numeral Converter ([link](https://www.calculatorsoup.com/calculators/conversions/roman-numeral-converter.php))