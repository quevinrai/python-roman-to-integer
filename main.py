import sys
import re

class Solution:
    roman_numerals = ["M", "D", "C", "L", "X", "V", "I"]
    arabic_numbers = [1000, 500, 100, 50, 10, 5, 1]
    ordered_values = list()
    ordered_operations = list()

    def get_ordered_values(self, s: str):
        s_length = len(s)
        s_iter = enumerate(iter(s))

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
                self.ordered_values.append(self.arabic_numbers[next_index])
                self.ordered_operations.append("+")
                self.ordered_values.append(self.arabic_numbers[current_index])
                self.ordered_operations.append("-")
                try:
                    next(s_iter)
                except StopIteration:
                    break
            else:
                self.ordered_values.append(self.arabic_numbers[current_index])
                self.ordered_operations.append("+")

    def validate_string(self, s: str) -> bool:
        """CONSTRAINT #1:
        
        's' string length is between 1 - 15 inclusive
        """

        if len(s) < 1 or len(s) > 15:
            print("The length of the roman numerals entered must be from 1 to 15.")
            return False
        
        """CONSTRAINT #2:
        
        Throw error if the roman numeral entered contains an invalid character.
        """

        for i in range(len(s)):
            try:
                self.roman_numerals.index(s[i])
            except:
                print("Roman numerals can only contain the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').")
                return False
            
        """CONSTRAINT #3:
        
        'D', 'L', and 'V' can only appear once
        """

        if (s.count("D") > 1 or
            s.count("L") > 1 or
            s.count("V") > 1
        ):
            print("Invalid roman numeral. The letters 'D', 'L', and 'V' can only appear once.")
            return False
        
        """CONSTRAINT #4:
        
        'M', 'C', 'X', or 'I' may appear no more that three times consecutively in the string
        """

        constraint_four_regex = re.search("[MCXI]{4,}", s)

        if (s.count("M") > 3 or
            s.count("C") > 3 or
            s.count("X") > 3 or
            s.count("I") > 3
        ):
            print("Invalid roman numeral. The letters 'M', 'C', 'X', and 'I' cannot appear more than three times consecutively.")
            return False
        
        """CONSTRAINT #5:
        
        Only I, X, and C can be used for subtraction (V, L, and D cannot).
        Therefore, the following pairs of letter are invalid: VX, VL, VC, VD, VM, LC, LD, LM, DM.
        """

        constraint_5_regex = re.search("[V][XLCDM]|[L][CDM]|[D][M]", s)

        if constraint_5_regex is not None:
            print("Invalid roman numeral. Only 'I', 'X', and 'C' can be used for subtraction ('V', 'L', and 'D' cannot).")
            print("Therefore, the following pairs of letter are invalid: 'VX', 'VL', 'VC', 'VD', 'VM', 'LC', 'LD', 'LM', 'DM'.")
            return False
        
        """CONSTRAINT #6:
        
        When subtracting, the value of the letter being subtracted from cannot be more than 10 times the
        value of letter being used for subtraction.
        Therefore, the following pairs of letters are invalid: IL, IC, ID, IM, XD, XM.
        """

        constraint_6_regex = re.search("[I][LCDM]|[X][DM]", s)

        if constraint_6_regex is not None:
            print("Invalid roman numeral. When subtracting, the value of the letter being subtracted from cannot be more than 10 times the value of letter being used for subtraction.")
            print("Therefore, the following pairs of letters are invalid: 'IL', 'IC', 'ID', 'IM', 'XD', 'XM'.")
            return False
        
        """CONSTRAINT #7:
        
        Once a letter has been used as a subtraction modifier, that letter cannot appear again in
        the string, unless that letter itself is subtracted from.
        """

        constraint_7_1_regex = re.search("(CM|CD)[C]", s)
        constraint_7_2_regex = re.search("(XC|XL)[X]", s)

        if constraint_7_1_regex is not None or constraint_7_2_regex is not None:
            print("Invalid roman numeral. Once a letter has been used as a subtraction modifier, that letter cannot appear again in the string, unless that letter itself is subtracted from.")
            return False
        
        """CONSTRAINT #8:
        
        Once a letter has been subtracted from, neither it nor the next lowest multiple of 5 may
        appear again in the string - so neither X nor V can follow IX, neither C nor L may follow XC, and
        neither M nor D may follow CM.
        """

        constraint_8_1_regex = re.search("IX[XV]", s)
        constraint_8_2_regex = re.search("XC[CL]", s)
        constraint_8_3_regex = re.search("CM[MD]", s)

        if (constraint_8_1_regex is not None or
            constraint_8_2_regex is not None or
            constraint_8_3_regex is not None
        ):
            print("Invalid roman numeral. Once a letter has been subtracted from, neither it nor the next lowest multiple of 5 may appear again in the string.")
            print("Neither X nor V can follow IX, neither C nor L may follow XC, and neither M nor D may follow CM.")
            return False
        
        """CONSTRAINT #9:
        
        A letter cannot be used as a subtraction modifier if that letter, or the next highest
        multiple of 5, appears previously in the string - so IV or IX cannot follow I or V, XL or
        XC cannot follow X or L, and CD or CM cannot follow C or D.
        """

        constraint_9_1_regex = re.search("[IV](IV|IX)",s)
        constraint_9_2_regex = re.search("[XL](XL|XC)",s)
        constraint_9_3_regex = re.search("[CD](CD|CM)",s)

        if (constraint_9_1_regex is not None or
            constraint_9_2_regex is not None or
            constraint_9_3_regex is not None
        ):
            print("Invalid roman numeral. A letter cannot be used as a subtraction modifier if that letter, or the next highest multiple of 5, appears previously in the string.")
            print("'IV' or 'IX' cannot follow 'I' or 'V', 'XL' or 'XC' cannot follow 'X' or 'L', and 'CD' or 'CM' cannot follow 'C' or 'D'.")
            return False

        """If 's' passes all constraints, run get_ordered_values"""
        self.get_ordered_values(s)

        """RULE 1:
        
        Order of roman numerals must be descending
        """

        for i in range(len(self.ordered_values)):
            if i >= len(self.ordered_values) - 1:
                break

            if self.ordered_values[i] < self.ordered_values[i + 1]:
                print("Invalid roman numerator. Values are not in descending order.")
                return False
        
        return True

    def roman_to_int(self, s: str) -> int:
        # Check if validateString method returns false, then exit system
        if not self.validate_string(s):
            sys.exit()

        # Variable declarations
        total = 0


        # Loop through all characters of 's' string
        for i in range(len(self.ordered_values)):
            if self.ordered_operations[i] == "+":
                total += self.ordered_values[i]
            elif self.ordered_operations[i] == "-":
                total -= self.ordered_values[i]

        return total

s = "MCMXIV"
sol = Solution()

print("ROMAN NUMERAL TO INTEGER")
print("------------------------\n")
print(f"Roman Numeral: {s}")
print(f"Integer: {sol.roman_to_int(s.upper())}")
print(sol.ordered_values)