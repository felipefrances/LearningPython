"""CPF Verification.
Develop a program that requests the entry of a CPF number in the format xxx.xxx.xxx-xx
and indicates whether it is a valid or invalid number by validating the check digits and formatting characters."""

# Request the user's CPF in the format xxx.xxx.xxx-xx
cpf = input("Enter your CPF in the format xxx.xxx.xxx-xx: ")

# Remove formatting characters and keep only digits
cpf = ''.join(char for char in cpf if char.isdigit())

# Check if the CPF has 11 digits
if len(cpf) != 11:
    print(f"The CPF {cpf} is invalid.")
else:
    # Calculate the first verification digit
    Sum1 = 0
    for i in range(9):
        Sum1 += int(cpf[i]) * (10 - i)
    Rest1 = Sum1 % 11
    DigitVerifier1 = 11 - Rest1 if Rest1 >= 2 else 0

    # Check the first verification digit
    if DigitVerifier1 != int(cpf[9]):
        print(f"The CPF {cpf} is invalid.")
    else:
        # Calculate the second verification digit
        Sum2 = 0
        for i in range(10):
            Sum2 += int(cpf[i]) * (11 - i)
        Rest2 = Sum2 % 11
        DigitVerifier2 = 11 - Rest2 if Rest2 >= 2 else 0

        # Check the second verification digit
        if DigitVerifier2 != int(cpf[10]):
            print(f"The CPF {cpf} is not valid.")
        else:
            print(f"The CPF {cpf} is valid.")
