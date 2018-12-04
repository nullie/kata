REGULAR = [
    (1000 ** 3, 'Billion'),
    (1000 ** 2, 'Million'),
    (1000, 'Thousand'),
    (100, 'Hundred'),
    (1, None),
]
IRREGULAR = dict(enumerate('''
        Zero One Two Three Four Five Six Seven Eight Nine
        Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen
    '''.split()))
IRREGULAR.update(zip(
    [20, 30, 40, 50, 60, 70, 80, 90],
    'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split(),
))
# One Billion Billion does not make sense, so limit to less than that
MAX = REGULAR[0][0]**2 - 1


def number_to_words(num, factor_word=None):
    assert 0 <= num <= MAX
    if num < 100:
        yield from less_than_hundred(num)
    else:
        remainder = num
        for value, word in REGULAR:
            factor, remainder = divmod(remainder, value)
            if factor:
                yield from number_to_words(factor, word)
    if num and factor_word:
        yield factor_word


def less_than_hundred(num):
    assert 0 <= num < 100

    if num in IRREGULAR:
        yield IRREGULAR[num]
    else:
        units = num % 10
        yield IRREGULAR[num - units]
        yield IRREGULAR[units]


class Solution:
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        return ' '.join(number_to_words(num))