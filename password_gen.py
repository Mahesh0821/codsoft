import random
def generate_password(len):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"
    password=""
    for i in range(len):
      password += random.choice(chars)
    return password

len = int(input("Enter the length of the password: "))
generated_password = generate_password(len)
print(generated_password)
