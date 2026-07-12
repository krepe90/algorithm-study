# https://school.programmers.co.kr/learn/courses/30/lessons/250137
# 2026-07-12 / PCCP 기출문제 > [PCCP 기출문제] 1번 / 붕대 감기 / Lv. 1

# 역시나 그냥 구현 문제


def solution(bandage: list[int], health: int, attacks: list[list[int]]):
    attack_idx = 0
    t = 0
    heal_streak = 0
    current_health = health
    while attack_idx < len(attacks):
        next_attack_time, next_attack_dmg = attacks[attack_idx]
        # 1. 공격을 받은 경우
        if next_attack_time == t:
            current_health -= next_attack_dmg
            attack_idx += 1
            heal_streak = 0
            if current_health <= 0:
                break
        # 2. 공격을 받지 않아 붕대가 감기는 중인 경우
        else:
            current_health += bandage[1]
            heal_streak += 1
            if heal_streak == bandage[0]:
                current_health += bandage[2]
                heal_streak = 0
            if current_health > health:
                current_health = health
        t += 1
    return current_health if current_health > 0 else -1


if __name__ == "__main__":
    print(solution([5, 1, 5], 30, [[2, 10], [9, 15], [10, 5], [11, 5]]))
    print(solution([3, 2, 7], 20, [[1, 15], [5, 16], [8, 6]]))
    print(solution([4, 2, 7], 20, [[1, 15], [5, 16], [8, 6]]))
    print(solution([1, 1, 1], 5, [[1, 2], [3, 2]]))
