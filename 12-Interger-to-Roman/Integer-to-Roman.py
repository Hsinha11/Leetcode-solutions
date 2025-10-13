class Solution:
    def intToRoman(self, num: int) -> str:
        # Map of decimal values to Roman numerals in descending order
        val_to_roman = [
            (1000, "M"),
            (900,  "CM"),
            (500,  "D"),
            (400,  "CD"),
            (100,  "C"),
            (90,   "XC"),
            (50,   "L"),
            (40,   "XL"),
            (10,   "X"),
            (9,    "IX"),
            (5,    "V"),
            (4,    "IV"),
            (1,    "I")
        ]
        
        roman = []
        
        for value, symbol in val_to_roman:
            # Count how many times the symbol fits into num
            count = num // value
            if count:
                roman.append(symbol * count)
                num -= value * count
        
        return ''.join(roman)
