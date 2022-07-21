# score_file = open("score.txt", "w", encoding="utf8")
# #(file name, writing, "korean info")

# print("Math : 0", file=score_file)
# print("ENG : 50", file=score_file)

# score_file.close()

# score_file = open("score.txt", "a")
# #"a" = append
# score_file.write("Science = 80")
# score_file.write("\ncoding: 100")
# score_file.close()

score_file = open("score.txt", "r")
print(score_file.read())
score_file.close()

score_file = open("score.txt", "r")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline() )

score_file.close()

score_file = open("score.txt", "r")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line)

score_file.close()