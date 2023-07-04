import sys

# --------------------------------------------- CLASSES --------------------------------------------- #

class Solution:
    rNumerals = ["M", "D", "C", "L", "X", "V", "I"]
    arabicNumbers = [1000, 500, 100, 50, 10, 5, 1]

    # Validation method to check if the roman numeral entered is valid
    def validateString(self, s: str) -> bool:
        # CONSTRAINT 1: 's' string length is between 1 - 15 inclusive
        if len(s) < 1 or len(s) > 15:
            print("The length of the roman numerals entered must be from 1 to 15.")
            return False
        
        # CONSTRAINT 2: Throw error if the roman numeral entered contains an invalid character
        for i in range(len(s)):
            try:
                self.rNumerals.index(s[i])
            except:
                print("Roman numerals can only contain the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').")
                return False
            
        # RULE 1: Order of roman numerals must be descending
        for i in range(len(s)):
            currentIndex = self.rNumerals.index(s[i])
            nextIndex = self.rNumerals.index(s[i + 1])

            if self.rNumerals[currentIndex] == "I" and self.rNumerals[nextIndex] == "V":
                pass
            
        return True

    # Main method to convert roman numerals to integer
    def romanToInt(self, s: str) -> int:
        # Check if validateString method returns false, then exit system
        if not self.validateString(s):
            sys.exit()

        # Variable declarations
        total = 0


        # Loop through all characters of 's' string
        for i in range(len(s)):
            currentIndex = self.rNumerals.index(s[i])
            total += self.arabicNumbers[currentIndex]

        return total

# --------------------------------------------- MAIN CODE --------------------------------------------- #

s = "MCMXIV"
sol = Solution()

print("ROMAN NUMERAL TO INTEGER")
print(f"Roman Numeral: {s}")
print(f"Integer: {sol.romanToInt(s)}")