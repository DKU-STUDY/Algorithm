T = int(input())
for _ in range(T):
    record_voices = input().split()
    fox_voice = set(record_voices)
    while True:
        V = input()
        if V == "what does the fox say?":
            break
        animal, goes, voice = V.split()
        fox_voice.remove(voice)
    for record_voice in record_voices:
        if record_voice in fox_voice:
            print(record_voice, end=' ')
    print()
