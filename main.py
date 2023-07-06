import sys

"""CLASSES"""

class Solution:
    roman_numerals = ["M", "D", "C", "L", "X", "V", "I"]
    arabic_numbers = [1000, 500, 100, 50, 10, 5, 1]
    ordered_values = list()

    """Method to convert roman numerals to integer"""
    def get_ordered_values(self, s: str):
        s_length = len(s)
        s_iter = enumerate(iter(s))

        for i, letter in s_iter:
            current_index = self.roman_numerals.index(letter)
            next_index = self.roman_numerals.index(s[i + 1]) if i < s_length - 1 else None

            if(
                (self.roman_numerals[current_index] == "I" and self.roman_numerals[next_index] == "V") or
                (self.roman_numerals[current_index] == "I" and self.roman_numerals[next_index] == "X") or
                (self.roman_numerals[current_index] == "X" and self.roman_numerals[next_index] == "L") or
                (self.roman_numerals[current_index] == "X" and self.roman_numerals[next_index] == "C") or
                (self.roman_numerals[current_index] == "C" and self.roman_numerals[next_index] == "D") or
                (self.roman_numerals[current_index] == "C" and self.roman_numerals[next_index] == "M")
            ):
                self.ordered_values.append(self.arabic_numbers[next_index])
                self.ordered_values.append(self.arabic_numbers[current_index])
                try:
                    next(s_iter)
                except StopIteration:
                    break
            else:
                self.ordered_values.append(self.arabic_numbers[current_index])

    """Method to validate or check if the roman numeral entered is valid"""
    def validate_string(self, s: str) -> bool:
        # CONSTRAINT 1: 's' string length is between 1 - 15 inclusive
        if len(s) < 1 or len(s) > 15:
            print("The length of the roman numerals entered must be from 1 to 15.")
            return False
        
        # CONSTRAINT 2: Throw error if the roman numeral entered contains an invalid character
        for i in range(len(s)):
            try:
                self.roman_numerals.index(s[i])
            except:
                print("Roman numerals can only contain the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').")
                return False
            
        # If 's' passes all constraints, run get_ordered_values
        self.get_ordered_values(s)

        # RULE 1: Order of roman numerals must be descending

            
        return True

    """Method to convert roman numerals to integer"""
    def roman_to_int(self, s: str) -> int:
        # Check if validateString method returns false, then exit system
        if not self.validate_string(s):
            sys.exit()

        # Variable declarations
        total = 0


        # Loop through all characters of 's' string
        for i in range(len(self.ordered_values)):
            total += self.ordered_values[i]

        return total

"""MAIN CODE"""

s = "MCMXIV"
sol = Solution()

print("ROMAN NUMERAL TO INTEGER")
print(f"Roman Numeral: {s}")
print(f"Integer: {sol.roman_to_int(s.upper())}")
print(sol.ordered_values)