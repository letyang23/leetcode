from typing import List


def cardPackets(cardTypes: List[int]) -> int:
    maxCard = max(cardTypes)
    additionalCards = float("inf")
    for target in range(2, maxCard):
        res = 0
        for i in range(len(cardTypes)):
            if cardTypes[i] % target != 0:
                res += target - (cardTypes[i] % target)
        additionalCards = min(additionalCards, res)
    return additionalCards


print(cardPackets([4, 7, 5, 11, 15]))
