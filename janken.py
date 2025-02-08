import random

def janken():
    choices = ["グー", "チョキ", "パー"]
    user = input("グー・チョキ・パーのどれを出しますか？: ")
    ai = random.choice(choices)
    print(f"プレイヤー: {user}, AI: {ai}")
    if user == ai:
        print("あいこ")
    elif (user == "グー" and ai == "チョキ") or (user == "チョキ" and ai == "パー") or (user == "パー" and ai == "グー"):
        print("あなたの勝ち！")
    else:
        print("あなたの負け…")

if __name__ == "__main__":
    janken()