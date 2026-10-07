#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""초등 5, 6학년 영단어 복습 게임 - 단어 몬스터를 물리쳐라!"""

import random
import time

WORDS = {
    "apple": "사과",
    "beautiful": "아름다운",
    "library": "도서관",
    "friend": "친구",
    "family": "가족",
    "school": "학교",
    "teacher": "선생님",
    "weather": "날씨",
    "holiday": "휴일",
    "birthday": "생일",
    "mountain": "산",
    "river": "강",
    "season": "계절",
    "kitchen": "부엌",
    "doctor": "의사",
    "animal": "동물",
    "museum": "박물관",
    "dangerous": "위험한",
    "favorite": "가장 좋아하는",
    "vegetable": "채소",
}

TOTAL_QUESTIONS = 5

TITLE_ART = r"""
 __        _____  ____  ____     ____    _    __  __ _____
 \ \      / / _ \|  _ \|  _ \   / ___|  / \  |  \/  | ____|
  \ \ /\ / / | | | |_) | | | | | |  _  / _ \ | |\/| |  _|
   \ V  V /| |_| |  _ <| |_| | | |_| |/ ___ \| |  | | |___
    \_/\_/  \___/|_| \_\____/   \____/_/   \_\_|  |_|_____|
"""

MONSTER_ART = r"""
      /\_/\
     ( o.o )   "단어 몬스터가 나타났다!
      > ^ <     영어로 맞혀서 물리쳐라!"
"""

HAPPY_ART = r"""
     \(^o^)/   정답! 몬스터가 쓰러졌다!
"""

SAD_ART = r"""
     (T_T)     앗, 몬스터가 웃고 있어...
"""

CORRECT_MSGS = ["대박! 천재 아니야?", "짝짝짝! 완벽해요!", "영어 박사 등장!", "와우! 멋져요!"]
WRONG_MSGS = ["괜찮아, 다음엔 꼭 맞힐 수 있어!", "아깝다! 거의 다 왔어!", "실수는 성장의 친구야!"]

RANKS = [
    (5, "🏆 영어 대마왕", "모든 몬스터를 물리쳤어요! 최고!"),
    (4, "🥇 영어 영웅", "거의 완벽해요! 조금만 더!"),
    (3, "🥈 영어 용사", "잘했어요! 복습하면 만점!"),
    (2, "🥉 영어 견습생", "좋은 시작이에요! 또 도전!"),
    (0, "🌱 영어 새싹", "괜찮아요, 연습하면 쑥쑥 자라요!"),
]


def play():
    print(TITLE_ART)
    name = input("용사님의 이름은? > ").strip() or "용사"
    print(f"\n환영해요, {name}! 한글 뜻을 보고 영어 단어를 써보세요.")
    print(MONSTER_ART)
    input("준비되면 Enter 를 누르세요! ")

    questions = random.sample(list(WORDS.items()), TOTAL_QUESTIONS)
    score = 0
    wrong_list = []

    for i, (eng, kor) in enumerate(questions, 1):
        print(f"\n========== 문제 {i}/{TOTAL_QUESTIONS} | 현재 점수: {score}점 ==========")
        print(f"👉 '{kor}' 은(는) 영어로?  ({len(eng)}글자)")
        answer = input("정답 > ").strip().lower()

        if answer == eng:
            score += 1
            print(HAPPY_ART)
            print(random.choice(CORRECT_MSGS))
        else:
            wrong_list.append((eng, kor))
            print(SAD_ART)
            print(random.choice(WRONG_MSGS))
            print(f"💡 힌트: 첫 글자는 '{eng[0].upper()}' 였어요!")
            print(f"✅ 정답: {eng}")
        time.sleep(0.5)

    show_scoreboard(name, score, wrong_list)


def show_scoreboard(name, score, wrong_list):
    rank, comment = next((r[1], r[2]) for r in RANKS if score >= r[0])
    print("\n" + "=" * 40)
    print("          🎉  점 수 판  🎉")
    print("=" * 40)
    print(f"  이름 : {name}")
    print(f"  점수 : {'★' * score}{'☆' * (TOTAL_QUESTIONS - score)}  ({score}/{TOTAL_QUESTIONS})")
    print(f"  등급 : {rank}")
    print(f"  한마디: {comment}")
    if wrong_list:
        print("\n  📝 다시 복습할 단어")
        for eng, kor in wrong_list:
            print(f"    - {eng} : {kor}")
    print("=" * 40)


def main():
    while True:
        play()
        again = input("\n다시 도전할까요? (y/n) > ").strip().lower()
        if again != "y":
            print("\n오늘도 수고했어요! 내일 또 만나요! 👋")
            break


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\n게임을 종료합니다. 안녕! 👋")
