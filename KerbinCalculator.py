import math
from scipy import constants as scp


def welcome():
    print("Welcome to the Kerbal Space Program Calculator!")
    print("-----------------------------------------------")
    print("[1]: You're trying to find what velocity is needed at a known altitude relative to Kerbin to maintain a polar orbit")
    print("")
    print("[2]: You're trying to find what height of polar orbit you would get using a known angular velocity")
    print("")
    print("[3]: Given an angular velocity, [and assuming a polar orbit] this finds the period of orbit of a body relative to Kerbin")
    print("")
    print("[4]: (Same as above but using a given height)")
    print("-----------------------------------------------")
    print("")
    

def menuInput():
    menu = int(input("Please enter which menu selection you'd like to pick [1-4]: "))
    return menu
    
def massInput():
    mass = float(input("Please enter the mass [in kg] of your craft [float]: "))
    return mass
    
def angVelocityInput():
    angVelocity = float(input("Please enter your angular velocity [float]: "))
    return angVelocity

def orbitalHeightInput():
    orbHeight = float(input("Please enter your orbital height [float]: "))
    return orbHeight
    
def givenHeightOpt1(height, mass):
    KERB_MASS = (5.929) * (10 ** 22)
    KERB_RADIUS = 600000
    totalHeight = KERB_RADIUS + height
    
    gravForce = ( (scp.G) * (KERB_MASS) * (mass)) / (totalHeight ** 2)
    reqVeloc = math.sqrt( ( (totalHeight) * (gravForce) ) / mass)
    return reqVeloc

def givenVelocityOpt2(velocity, mass):
    KERB_MASS = (5.929) * (10 ** 22)
    KERB_RADIUS = 600000
    
    heightRelativeToSurface = float( ( -(mass * (velocity ** 2) * KERB_RADIUS) + (scp.G * KERB_MASS * mass)) / (mass * (velocity ** 2)) )
    return heightRelativeToSurface
    
def givenAngularVelocityOpt3(velocity, mass):
    KERB_MASS = (5.929) * (10 ** 22)
    KERB_RADIUS = 600000
    orbitalHeight = float(givenVelocityOpt2(velocity, mass))
    
    period = float(math.sqrt( (4 * (scp.pi ** 2) * ( (orbitalHeight + KERB_RADIUS) ** 3) ) / (scp.G * KERB_MASS) ))
    return period
    
def givenHeightOpt4(height, mass):
    KERB_MASS = (5.929) * (10 ** 22)
    KERB_RADIUS = 600000
    
    period = float(math.sqrt( (4 * (scp.pi ** 2) * ( (height + KERB_RADIUS) ** 3) ) / (scp.G * KERB_MASS) ))
    return period
    


welcome()
menuChoice = menuInput()

if menuChoice == 1:
    mass = massInput()
    orbHeight = orbitalHeightInput()
    
    reqVelocity = givenHeightOpt1(orbHeight, mass)
    print("")
    print("Thank you for using the Kerbal Calculator!")
    print("Your angular velocity will be:", reqVelocity, "m/s at an altitude of", orbHeight, "meters.")
    
    
elif menuChoice == 2:
    mass = massInput()
    reqVelocity = angVelocityInput()
    
    orbitHeight = givenVelocityOpt2(reqVelocity, mass)
    print("")
    print("Thank you for using the Kerbal Calculator!")
    print("Your orbit height (relative to surface) will be", orbitHeight, "meters traveling at", reqVelocity, "m/s.")
    
    
    
elif menuChoice == 3:
    mass = massInput()
    velocity = angVelocityInput()
    
    orbPeriod = givenAngularVelocityOpt3(velocity, mass)
    print("")
    print("Thank you for using the Kerbal Calculator!")
    print("Your orbital period will be", orbPeriod, "seconds.")
    
elif menuChoice == 4:
    mass = massInput()
    orbHeight = orbitalHeightInput()
    
    orbPeriod = givenHeightOpt4(orbHeight, mass)
    print("")
    print("Thank you for using the Kerbal Calculator!")
    print("Your orbital period will be", orbPeriod, "seconds.")
    
    
else:
    print("That's not a valid input!")
    menuChoice = menuInput()