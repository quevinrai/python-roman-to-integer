import sys
import re

class Solution:
    roman_numerals = ["M", "D", "C", "L", "X", "V", "I"]
    arabic_numbers = [1000, 500, 100, 50, 10, 5, 1]
    total_values = list()
    current_highest_length = 0

    def convert_roman_to_integer(self, s: str):
        s_length = len(s)
        s_iter = enumerate(iter(s))
        current_roman_numeral = ""
        current_integer_total = 0
        previous_value = 0

        for i, letter in s_iter:
            current_index = self.roman_numerals.index(letter)
            next_index = self.roman_numerals.index(s[i + 1]) if i < s_length - 1 else 0

            if(
                (self.roman_numerals[current_index] == "I" and self.roman_numerals[next_index] == "V") or
                (self.roman_numerals[current_index] == "I" and self.roman_numerals[next_index] == "X") or
                (self.roman_numerals[current_index] == "X" and self.roman_numerals[next_index] == "L") or
                (self.roman_numerals[current_index] == "X" and self.roman_numerals[next_index] == "C") or
                (self.roman_numerals[current_index] == "C" and self.roman_numerals[next_index] == "D") or
                (self.roman_numerals[current_index] == "C" and self.roman_numerals[next_index] == "M")
            ):
                current_roman_numeral = self.roman_numerals[current_index] + self.roman_numerals[next_index]
                current_integer_total = self.arabic_numbers[next_index] - self.arabic_numbers[current_index]
                self.total_values.append((current_roman_numeral, current_integer_total))

                if self.current_highest_length < len(current_roman_numeral):
                    self.current_highest_length = len(current_roman_numeral)

                current_roman_numeral = ""
                current_integer_total = 0
                
                try:
                    next(s_iter)
                except StopIteration:
                    break
            else:
                current_roman_numeral += letter
                current_integer_total += self.arabic_numbers[current_index]

                if self.current_highest_length < len(current_roman_numeral):
                    self.current_highest_length = len(current_roman_numeral)

                if current_index != next_index:
                    self.total_values.append((current_roman_numeral, current_integer_total))
                    current_roman_numeral = ""
                    current_integer_total = 0

        # Check if values are in descending order
        for total_values_tuple in self.total_values:
            if previous_value < total_values_tuple[1] and previous_value != 0:
                sys.exit("Invalid roman numerator. Values are not in descending order.")
            else:
                previous_value = total_values_tuple[1]

    def validate_string(self, s: str):
        """RULE #1: 's' string length is between 1 - 15 inclusive"""

        if len(s) < 1 or len(s) > 15:
            sys.exit("The length of the roman numerals entered must be from 1 to 15.")
        
        """RULE #2: Throw error if the roman numeral entered contains an invalid character"""

        for i in range(len(s)):
            try:
                self.roman_numerals.index(s[i])
            except:
                sys.exit("Roman numerals can only contain the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').")
            
        """RULE #3: 'D', 'L', and 'V' can only appear once"""

        if s.count("D") > 1 or s.count("L") > 1 or s.count("V") > 1:
            sys.exit("Invalid roman numeral. The letters 'D', 'L', and 'V' can only appear once.")
        
        """RULE #4: 'M', 'C', 'X', or 'I' may appear no more that three times consecutively in the string"""

        letter_count = 0
        is_letter_count_exceeded = False

        for i in range(len(s)):
            if ((s[i] == "M") or (s[i] == "C") or
                (s[i] == "X") or (s[i] == "I")
            ):
                letter_count += 1

            if letter_count == 4:
                is_letter_count_exceeded = True
                break
            
            try:
                if (s[i] != s[i + 1]):
                    letter_count = 0
            except:
                break

        if ((s.count("M") > 3 and is_letter_count_exceeded) or
            (s.count("C") > 3 and is_letter_count_exceeded) or
            (s.count("X") > 3 and is_letter_count_exceeded) or
            (s.count("I") > 3 and is_letter_count_exceeded)
        ):
            sys.exit("Invalid roman numeral. The letters 'M', 'C', 'X', and 'I' cannot appear more than three times consecutively.")
        
        """RULE #5: Only I, X, and C can be used for subtraction (V, L, and D cannot)"""

        constraint_5_regex = re.search("[V][XLCDM]|[L][CDM]|[D][M]", s)

        if constraint_5_regex is not None:
            sys.exit("Invalid roman numeral. Only 'I', 'X', and 'C' can be used for subtraction ('V', 'L', and 'D' cannot).")
        
        """RULE #6: When subtracting, the value of the letter being subtracted from cannot be more than 10 times the value of letter being used for subtraction"""

        constraint_6_regex = re.search("[I][LCDM]|[X][DM]", s)

        if constraint_6_regex is not None:
            sys.exit("Invalid roman numeral. When subtracting, the value of the letter being subtracted from cannot be more than 10 times the value of letter being used for subtraction.")
        
        """RULE #7: Once a letter has been used as a subtraction modifier, that letter cannot appear again in the string, unless that letter itself is subtracted from"""

        constraint_7_1_regex = re.search("(CM|CD)[C]", s)
        constraint_7_2_regex = re.search("(XC|XL)[X]", s)

        if constraint_7_1_regex is not None or constraint_7_2_regex is not None:
            sys.exit("Invalid roman numeral. Once a letter has been used as a subtraction modifier, that letter cannot appear again in the string, unless that letter itself is subtracted from")
        
        """RULE #8: Once a letter has been subtracted from, neither it nor the next lowest multiple of 5 may appear again in the string"""

        constraint_8_1_regex = re.search("IX[XV]", s)
        constraint_8_2_regex = re.search("XC[CL]", s)
        constraint_8_3_regex = re.search("CM[MD]", s)

        if (constraint_8_1_regex is not None or
            constraint_8_2_regex is not None or
            constraint_8_3_regex is not None
        ):
            sys.exit("Invalid roman numeral. Once a letter has been subtracted from, neither it nor the next lowest multiple of 5 may appear again in the string.")
        
        """RULE #9: A letter cannot be used as a subtraction modifier if that letter, or the next highest multiple of 5, appears previously in the string"""

        constraint_9_1_regex = re.search("[IV](IV|IX)",s)
        constraint_9_2_regex = re.search("[XL](XL|XC)",s)
        constraint_9_3_regex = re.search("[CD](CD|CM)",s)

        if (constraint_9_1_regex is not None or
            constraint_9_2_regex is not None or
            constraint_9_3_regex is not None
        ):
            sys.exit("Invalid roman numeral. A letter cannot be used as a subtraction modifier if that letter, or the next highest multiple of 5, appears previously in the string.")

    def display_values(self):
        white_space_count1 = 0
        white_space_count2 = 5

        for letter, key in self.total_values:
            white_space_count1 = (self.current_highest_length - len(letter)) + 5

            print(f"{letter}{' ' * white_space_count1}={' ' * white_space_count2}{key}")

    def roman_to_int(self, s: str) -> int:
        total = 0

        # Check if 's' passes all rules
        self.validate_string(s)

        # If 's' has no errors, run method to convert the entered roman numeral into an integer
        self.convert_roman_to_integer(s)

        # Loop through list of total values
        for total_values_tuple in self.total_values:
            total += total_values_tuple[1]

        return total

s = "III"
sol = Solution()

print("----------------------------")
print("+ ROMAN NUMERAL TO INTEGER +")
print("----------------------------\n")

print(f"Roman Numeral: {s}")
print(f"Integer: {sol.roman_to_int(s.upper())}\n")

print("----------------------------")
print("+         BREAKDOWN        +")
print("----------------------------\n")

sol.display_values()