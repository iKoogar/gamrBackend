"""
testing.py
small testing suite for gamr
"""

import Services.data_service as svc


def testAddAndDeleteUser(eml: str) -> bool:
    # create the user and add to database
    svc.addUser("testName", eml, "testPWD")

    # check if user was added to database
    user, found = svc.findUserByEmail(eml)
    if not (found and user.email == eml):
        print("ERROR: user not found")
        return False

    # delete the user from the database
    svc.deleteUserByEmail(eml)

    # check if user was removed from database
    user, found = svc.findUserByEmail(eml)
    if found:
        print("ERROR: user not removed")
        return False

    return True


def runTests():
    return testAddAndDeleteUser("test")


