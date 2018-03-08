import itertools
# TODO having scores equals for one pair, etc
# Clubs = 0, Diamonds = 1, Hearts = 2, Spades = 3
# nums are normal, jack = 11, queen = 12, king = 13, ace = 14

# each of these functions works on one hand by one player

# AS KD 3D JD 8H
# 7C 8C 5C QD 6C

cardVals = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
suitVals = {'C': 0, 'D': 1, 'H': 2, 'S': 3}
faceCards = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}


def detHands():
    with open('p054_poker.txt') as f:
        content = f.readlines()
        # you may also want to remove whitespace characters like `\n` at the end of each line
        content = [x.strip() for x in content]
        # print("test")
    player1Score = 0
    player2Score = 0
    for i in content:
        hand1 = i[:15].strip()
        hand2 = i[14:].strip()
        # print(hand1)
        # print(hand2)
        hand1Vals = getScore(convToNumbers(hand1))
        hand2Vals = getScore(convToNumbers(hand2))
        # print("hand1Vals")
        if hand1Vals[0] > hand2Vals[0]:
            player1Score += 1
        elif hand1Vals[0] == hand2Vals[0] and hand1Vals[1] > hand2Vals[1]:
            player1Score += 1
        elif hand1Vals[0] == hand2Vals[0] == 0 and highestCard(convToNumbers(hand1)) > highestCard(convToNumbers(hand2)):
            player1Score += 1
        elif hand1Vals[0] == hand2Vals[0] and hand1Vals[1] == hand2Vals[1] and highestCard(convToNumbers(hand1)) > highestCard(convToNumbers(hand2)):
            player1Score += 1

        if hand1Vals[0] < hand2Vals[0]:
            player2Score += 1
        elif hand1Vals[0] == hand2Vals[0] and hand1Vals[1] < hand2Vals[1]:
            player2Score += 1
        elif hand1Vals[0] == hand2Vals[0] == 0 and highestCard(convToNumbers(hand1)) < highestCard(convToNumbers(hand2)):
            player2Score += 1
        elif hand1Vals[0] == hand2Vals[0] and hand1Vals[1] == hand2Vals[1] and highestCard(convToNumbers(hand1)) < highestCard(convToNumbers(hand2)):
            player2Score += 1
        #elif hand1Vals[0] == hand2Vals[0] and not hand1Vals[1] < hand2Vals[1]:
            #print(hand1)
            #print(hand2)

        # print(hand1)
        # print(hand2)

        # print(content)
    return (player1Score,player2Score)


def getScore(vals):
    score = 0
    priority = 0
    one = twoOfAKind(vals)
    two = twoPairs(vals)
    three = threeOfAKind(vals)
    four = straight(vals)
    five = fullHouse(vals)
    six = fourOfAKind(vals)
    seven = straightFlush(vals)
    eight = royalFlush(vals)
    if one[0]:
        score = 1
        priority = one[1]
    if two[0]:
        score = 2
        priority = two[1]
    if three[0]:
        score = 3
        priority = three[1]
    if four[0]:
        score = 4
        priority = four[1]
    if five:
        score = 5
        priority = highestCard(vals)
    if six[0]:
        score = 6
        priority = six[1]
    if seven[0]:
        score = 7
        priority = seven[1]
    if eight:
        score = 8
    return (score, priority)


def convToNumbers(hand):
    handNums = []
    for i in hand:
        if i.isdigit():
            handNums.append(int(i))
        elif i in suitVals:
            handNums.append(suitVals[i])
        elif i in faceCards:
            handNums.append(faceCards[i])
    return handNums


def highestCard(vals):
    nums = vals[::2]
    return max(nums)


def twoOfAKind(vals):
    nums = vals[::2]
    combos = itertools.combinations(nums, 2)
    # print(list(combos))
    for i in combos:
        if i[0] == i[1]:
            return (True, i[0])
    return (False, 0)


def twoPairs(vals):
    nums = vals[::2]
    count = []
    combos = itertools.combinations(nums, 2)
    for i in combos:
        if i[0] == i[1]:
            count.append(i[0])
            if len(count) == 2:

                return (True, sorted(count)[-1])
    return (False, 0)


def threeOfAKind(vals):
    nums = vals[::2]
    combos = itertools.combinations(nums, 3)
    for i in combos:
        if i[0] == i[1] == i[2]:
            return (True, i[0])
    return (False, 0)


def straight(vals):
    nums = sorted(vals[::2])
    if nums[1] - nums[0] == nums[2] - nums[1] == nums[3] - nums[2] == nums[4] - nums[3] == 1:
        return (True, max(nums))
    elif nums[1] - nums[0] == nums[2] - nums[1] == nums[3] - nums[2] == 1 and nums[4] == 14:
        return (True, nums[-2])
    return (False, 0)


def flush(vals):
    suits = sorted(vals[1::2])
    return suits[::1] == suits[::-1]


def fullHouse(vals):
    nums = vals[::2]
    combos = itertools.combinations(nums, 3)
    for i in combos:
        if i[0] == i[1] == i[2]:
            nums = list(filter(lambda a: a != i[0], nums))
            # print(nums)
    if nums[0] == nums[1]:
        return True
    return False


def fourOfAKind(vals):
    nums = vals[::2]
    combos = itertools.combinations(nums, 4)
    for i in combos:
        if i[0] == i[1] == i[2] == i[3]:
            return (True, i[0])
    return (False, 0)


def straightFlush(vals):
    out = straight(vals)
    return (out[0] and flush(vals),out[1])


def royalFlush(vals):
    if flush(vals):
        vals = sorted(vals[::2])
        # print(cardVals[8:])
        # print(vals)
        return vals == cardVals[8:]


if __name__ == "__main__":
    print("PASS" if twoOfAKind([5, 2, 5, 1, 6, 3, 7, 3, 13, 1])[0] else "FAIL")
    print("PASS" if not twoOfAKind(
        [9, 2, 5, 1, 6, 3, 7, 3, 13, 1])[0] else "FAIL")
    print("PASS" if threeOfAKind(
        [5, 2, 5, 1, 6, 3, 5, 3, 13, 1])[0] else "FAIL")
    print("PASS" if not threeOfAKind(
        [2, 2, 5, 1, 6, 3, 5, 3, 13, 1])[0] else "FAIL")
    print("PASS" if twoPairs([5, 2, 5, 1, 6, 3, 7, 3, 6, 1])[0] else "FAIL")
    print("PASS" if not twoPairs(
        [9, 2, 5, 1, 6, 3, 7, 3, 13, 1])[0] else "FAIL")
    print("PASS" if straight([5, 2, 6, 1, 7, 3, 8, 3, 9, 1])[0] else "FAIL")
    print("PASS" if straight(
        [10, 2, 11, 1, 12, 3, 13, 3, 14, 1])[0] else "FAIL")
    print("PASS" if straight([14, 2, 2, 1, 3, 3, 5, 3, 4, 1])[0] else "FAIL")
    print("PASS" if not straight(
        [9, 2, 5, 1, 6, 3, 7, 3, 13, 1])[0] else "FAIL")
    print("PASS" if flush([14, 2, 2, 2, 3, 2, 5, 2, 4, 2]) else "FAIL")
    print("PASS" if not flush([9, 2, 5, 1, 6, 3, 7, 3, 13, 1]) else "FAIL")
    print("PASS" if fullHouse([5, 2, 5, 1, 6, 3, 5, 3, 6, 1]) else "FAIL")
    print("PASS" if not fullHouse(
        [5, 2, 5, 1, 6, 3, 5, 3, 13, 1]) else "FAIL")
    print("PASS" if fourOfAKind([5, 2, 5, 1, 6, 3, 5, 3, 5, 1])[0] else "FAIL")
    print("PASS" if not fourOfAKind(
        [2, 2, 5, 1, 6, 3, 5, 3, 13, 1])[0] else "FAIL")
    print("PASS" if straightFlush(
        [14, 2, 2, 2, 3, 2, 5, 2, 4, 2])[0] else "FAIL")
    print("PASS" if not straightFlush(
        [9, 2, 5, 1, 6, 3, 7, 3, 13, 1])[0] else "FAIL")
    print("PASS" if royalFlush(
        [10, 2, 11, 2, 12, 2, 13, 2, 14, 2]) else "FAIL")

print(detHands())
