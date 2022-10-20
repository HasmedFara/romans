class Solution:
    symbols = {
        1: "I", 4: "IV", 5: "V", 9: "IX",
        10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C",
        400: "CD", 500: "D", 900: "CM", 1000: "M"
    }

    def _get_roman_number(self, num: int, ac: str) -> str:
        # exit condition
        if num in self.symbols:
            return ac + self.symbols[num]

        number_idx = 0
        values = list(self.symbols.keys())

        while number_idx < len(values):
            current_val = values[number_idx]

            # choose preview value
            if current_val > num:
                prev_val = values[number_idx - 1]
                rest = num - prev_val
                ac += self.symbols[prev_val]
                return self._get_roman_number(rest, ac)

            # latest index
            elif number_idx == len(values) - 1:
                rest = num - current_val
                ac += self.symbols[current_val]
                return self._get_roman_number(rest, ac)

            number_idx += 1

    def int_to_roman(self, num: int) -> str:
        """
        Converts an integer to a Roman number
        :param num: integer
        """

        return self._get_roman_number(num, "")


if __name__ == '__main__':
    print(Solution().int_to_roman(1984))
