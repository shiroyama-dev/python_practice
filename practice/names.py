names = ["Elon", "Sam", "Dario"]
print(names[0])
print(names[1])
print(names[2])

print(f"{names[0]}さん、こんにちは")
print(f"{names[1]}さん、こんにちは")
print(f"{names[2]}さん、こんにちは")

motorcycle = ["Honda", "Suzuki", "Kawasaki", "Claude"]
print(f"私は{motorcycle[0]}のバイクがほしい。")
print(f"私は{motorcycle[1]}のバイクがほしい。")
print(f"私は{motorcycle[2]}のバイクがほしい。")
print(f"私は{motorcycle[3]}のバイクがほしい。")

guests = ["Elon", "Sam", "Dario"]
print(f"{guests[0]}さん、夕食にお越しください")
print(f"{guests[1]}さん、夕食にお越しください")
print(f"{guests[2]}さん、夕食にお越しください")

print(f"{guests[0]}さんは夕食にこれなくなりました")
guests[0] = "Grok"
print(f"{guests[0]}さん、夕食にお越しください")
print(f"{guests[1]}さん、夕食にお越しください")
print(f"{guests[2]}さん、夕食にお越しください")

print("大きなテーブルを見つけました")
guests.insert(0, "Jensen")
guests.insert(3, "ChatGPT")
guests.append("Gemini")
print(f"こんにちは{guests[0]}さん、夕食にお越しください")
print(f"こんにちは{guests[1]}さん、夕食にお越しください")
print(f"こんにちは{guests[2]}さん、夕食にお越しください")
print(f"こんにちは{guests[3]}さん、夕食にお越しください")
print(f"こんにちは{guests[4]}さん、夕食にお越しください")
print(f"こんにちは{guests[5]}さん、夕食にお越しください")

print("夕食には2人しか招待できなくなりました")
remove = guests.pop()
print(f"{remove}さん、招待できなくなりました")
remove = guests.pop()
print(f"{remove}さん、招待できなくなりました")
remove = guests.pop()
print(f"{remove}さん、招待できなくなりました")
remove = guests.pop()
print(f"{remove}さん、招待できなくなりました")
print(f"{guests[0]}さん、夕食にお越しください")
print(f"{guests[1]}さん、夕食にお越しください")
del guests[0]
del guests[0]
print(guests)

country = ["USA", "Japan", "China", "Korea", "Russia"]
print(country)
print(sorted(country))
print(country)
print(sorted(country, reverse=True))
print(country)
country.reverse()
print(country)
country.reverse()
print(country)
country.sort()
print(country)
country.sort(reverse=True)
print(country)

print(f"夕食には{len(guests)}人招待できます")

