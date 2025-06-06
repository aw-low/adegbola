password = str(input("Input password."))
character = ["!","@","#","$","%","^","&","*","(",")","_","+","-","=","{","}","[","]","|",":","<",">","?","/",".",",","'","\"","`","~"," "]
digit = ["0","1","2","3","4","5","6","7","8","9"]


has_letter = any(char.isalpha() for char in password)
has_number = any(char.isdigit() for char in password)
has_special = any(char in character for char in password)

if len(password) < 8:
    print("❌ Password must contain at least 8 characters.")
elif not has_letter:
    print("❌ Password must contain at least one letter.")
elif not has_number:
    print("❌ Password must contain at least one number.")
elif not has_special:
    print("❌ Password must contain at least one special character.")

# Final status
else:
    print("✅ Strong password!")
