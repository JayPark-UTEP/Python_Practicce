gun = 10

def checkpoint(soldiers):
    global gun #전역 변수 gun
    gun = gun - soldiers
    print("[Method] Remain guns: {0}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[Method] Remain guns: {0}".format(gun))
    return gun

print("Total Guns: {0}".format(gun))
checkpoint(2)
print("Remain Guns: {0}".format(gun))

print("Total Guns: {0}".format(gun))
checkpoint_ret(gun, 2)
print("Remain Guns: {0}".format(gun))