while True:
    print('Enter your new password (Letters and Numbers only)')
    newPassword = input()
    if newPassword.isalnum():
        break
    print('Password can only have letters and numbers')