import pickle
import profile
# profile_file = open("profile.pickle", "wb")
# profile = {"Name":"John", "Age":30, "Hobby":["Basketball", "swimming", "Coding"]}
# print(profile)
# pickle.dump(profile, profile_file)
# profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file)
print(profile)
profile_file.close()

