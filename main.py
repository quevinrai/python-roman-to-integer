import sys

class Solution:
    roman_numerals = ["M", "D", "C", "L", "X", "V", "I"]
    arabic_numbers = [1000, 500, 100, 50, 10, 5, 1]
    total_values = list()
    current_highest_length = 0
    is_validation_invalid = False
    validation_error_message = ""

    def convert_roman_to_integer(self, s: str):
        s_length = len(s)
        s_iter = enumerate(iter(s))
        current_index = 0
        next_index = 0
        current_roman_numeral = ""
        current_integer_total = 0

        for i, letter in s_iter:
            current_index = self.roman_numerals.index(letter)
            if i < s_length - 1:
                next_index = self.roman_numerals.index(s[i + 1])

            if(
                (self.roman_numerals[current_index] == "I" and self.roman_numerals[next_index] == "V") or
                (self.roman_numerals[current_index] == "I" and self.roman_numerals[next_index] == "X") or
                (self.roman_numerals[current_index] == "X" and self.roman_numerals[next_index] == "L") or
                (self.roman_numerals[current_index] == "X" and self.roman_numerals[next_index] == "C") or
                (self.roman_numerals[current_index] == "C" and self.roman_numerals[next_index] == "D") or
                (self.roman_numerals[current_index] == "C" and self.roman_numerals[next_index] == "M" and i != s_length - 1)
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

                if current_index != next_index or i == s_length - 1:
                    self.total_values.append((current_roman_numeral, current_integer_total))
                    current_roman_numeral = ""
                    current_integer_total = 0

    def validate_string(self, s: str):
        """RULE #1: 's' string length is between 1 - 15 inclusive"""

        if len(s) < 1 or len(s) > 15:
            self.validation_error_message = "The length of the roman numerals entered must be from 1 to 15."
        
        """RULE #2: Throw error if the roman numeral entered contains an invalid character"""

        for i in range(len(s)):
            try:
                self.roman_numerals.index(s[i])
            except:
                self.validation_error_message = "Roman numerals can only contain the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M')."
            
        """RULE #3: 'D', 'L', and 'V' can only appear once"""

        if s.count("D") > 1 or s.count("L") > 1 or s.count("V") > 1:
            self.validation_error_message = "Invalid roman numeral. The letters 'D', 'L', and 'V' can only appear once."
        
        """RULE #4: 'M', 'C', 'X', or 'I' may appear no more that three times consecutively in the string"""

        letter_count = 0

        for i in range(len(s)):
            if s[i] == "M" or s[i] == "C" or s[i] == "X" or s[i] == "I":
                letter_count += 1

            if letter_count == 4:
                if s.count("M") > 3 or s.count("C") > 3 or s.count("X") > 3 or s.count("I") > 3:
                    self.validation_error_message = "Invalid roman numeral. The letters 'M', 'C', 'X', and 'I' cannot appear more than three times consecutively."
            
            try:
                if s[i] != s[i + 1]:
                    letter_count = 0
            except:
                break
        
        """RULE #5: Only I, X, and C can be used for subtraction (V, L, and D cannot)"""

        for i in range(len(s)):
            try:
                if (s[i] == "V" and s[i + 1] == "X" or
                    s[i] == "V" and s[i + 1] == "L" or
                    s[i] == "V" and s[i + 1] == "C" or
                    s[i] == "V" and s[i + 1] == "D" or
                    s[i] == "V" and s[i + 1] == "M" or
                    s[i] == "L" and s[i + 1] == "C" or
                    s[i] == "L" and s[i + 1] == "D" or
                    s[i] == "L" and s[i + 1] == "M" or
                    s[i] == "D" and s[i + 1] == "M"
                ):
                    self.validation_error_message = "Invalid roman numeral. Only 'I', 'X', and 'C' can be used for subtraction ('V', 'L', and 'D' cannot)."
            except:
                break
        
        """RULE #6: When subtracting, the value of the letter being subtracted from cannot be more than 10 times the value of letter being used for subtraction"""
        
        for i in range(len(s)):
            try:
                if (s[i] == "I" and s[i + 1] == "L" or
                    s[i] == "I" and s[i + 1] == "C" or
                    s[i] == "I" and s[i + 1] == "D" or
                    s[i] == "I" and s[i + 1] == "M" or
                    s[i] == "X" and s[i + 1] == "D" or
                    s[i] == "X" and s[i + 1] == "M"
                ):
                    self.validation_error_message = "Invalid roman numeral. When subtracting, the value of the letter being subtracted from cannot be more than 10 times the value of letter being used for subtraction."
            except:
                break
        
        """RULE #7: Once a letter has been used as a subtraction modifier, that letter cannot appear again in the string, unless that letter itself is subtracted from"""

        for i in range(len(s)):
            try:
                if (s[i] == "C" and s[i + 1] == "M" and s[i + 2] == "C" or
                    s[i] == "C" and s[i + 1] == "D" and s[i + 2] == "C" or
                    s[i] == "X" and s[i + 1] == "X" and s[i + 2] == "X" or
                    s[i] == "C" and s[i + 1] == "L" and s[i + 2] == "X"
                ):
                    self.validation_error_message = "Invalid roman numeral. Once a letter has been used as a subtraction modifier, that letter cannot appear again in the string, unless that letter itself is subtracted from."
            except:
                break
        
        """RULE #8: Once a letter has been subtracted from, neither it nor the next lowest multiple of 5 may appear again in the string"""

        for i in range(len(s)):
            try:
                if (s[i] == "I" and s[i + 1] == "X" and s[i + 2] == "X" or
                    s[i] == "I" and s[i + 1] == "X" and s[i + 2] == "V" or
                    s[i] == "X" and s[i + 1] == "C" and s[i + 2] == "C" or
                    s[i] == "X" and s[i + 1] == "C" and s[i + 2] == "L" or
                    s[i] == "C" and s[i + 1] == "M" and s[i + 2] == "M" or
                    s[i] == "C" and s[i + 1] == "M" and s[i + 2] == "D"
                ):
                    self.validation_error_message = "Invalid roman numeral. Once a letter has been subtracted from, neither it nor the next lowest multiple of 5 may appear again in the string."
            except:
                break
        
        """RULE #9: A letter cannot be used as a subtraction modifier if that letter, or the next highest multiple of 5, appears previously in the string"""

        for i in range(len(s)):
            try:
                if (s[i] == "I" and s[i + 1] == "I" and s[i + 2] == "V" or
                    s[i] == "I" and s[i + 1] == "I" and s[i + 2] == "X" or
                    s[i] == "V" and s[i + 1] == "I" and s[i + 2] == "V" or
                    s[i] == "V" and s[i + 1] == "I" and s[i + 2] == "X" or
                    s[i] == "X" and s[i + 1] == "X" and s[i + 2] == "L" or
                    s[i] == "X" and s[i + 1] == "X" and s[i + 2] == "C" or
                    s[i] == "L" and s[i + 1] == "X" and s[i + 2] == "L" or
                    s[i] == "L" and s[i + 1] == "X" and s[i + 2] == "C" or
                    s[i] == "C" and s[i + 1] == "C" and s[i + 2] == "D" or
                    s[i] == "C" and s[i + 1] == "C" and s[i + 2] == "M" or
                    s[i] == "D" and s[i + 1] == "C" and s[i + 2] == "D" or
                    s[i] == "D" and s[i + 1] == "C" and s[i + 2] == "M" 
                ):
                    self.validation_error_message = "Invalid roman numeral. A letter cannot be used as a subtraction modifier if that letter, or the next highest multiple of 5, appears previously in the string."
            except:
                break

        """RULE #10: Values must be in descending order"""
        previous_value = 0

        for total_values_tuple in self.total_values:
            if previous_value < total_values_tuple[1] and previous_value != 0:
                self.validation_error_message = "Invalid roman numerator. Values are not in descending order."
                break
            else:
                previous_value = total_values_tuple[1]

        """Check if there was a validation error message captured"""
        if self.validation_error_message != "":
            sys.exit(self.validation_error_message)

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

sol = Solution()

print("------------------------------")
print(" + ROMAN NUMERAL TO INTEGER + ")
print("------------------------------\n")

s = input("Input: ")
print(f"Input: {s.upper()}")
print(f"Output: {sol.roman_to_int(s.upper())}\n")

print("------------------------------")
print(" +          BREAKDOWN       + ")
print("------------------------------\n")

sol.display_values()