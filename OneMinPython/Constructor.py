def profile(name, age, main_lang):
    print("Name: {0}\tage: {1}\t main language: {2}".format(name, age, main_lang))

profile("Josh", 20, "Python")
profile("Albert", 22, "Java")

#The same age, same class, same

def profile(name, age=17, main_lang="Python"):
    print("Name: {0}\tage: {1}\t main language: {2}".format(name, age, main_lang))

profile("Josh")
profile("Albert")

def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name="Josh", main_lang="Python", age = 22)
profile(main_lang="Java", name = "Albert", age = 26)

def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("Name: {0}\t Age: {1}\t".format(name, age), end=" ")
    print(lang1, lang2, lang3, lang4, lang5)

profile("Josh", 20, "Python", "Java", "C/C++", "C#", "JavaScript")
profile("Albert", 23, "Kotlin", "Swift", "", "", "")

def profile(name, age, *language):
    print("Name: {0}\t Age: {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end = " ")
    print()

profile("Josh", 20, "Python", "Java", "C/C++", "C#", "JavaScript", "ReactJS")
profile("Albert", 23, "Kotlin", "Swift")