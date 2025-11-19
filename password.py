def checkIfGood(email,password):
    if not isinstance(email,str): return "Error email is not a string. "
    if not "@" in email: return "Error email does not include '@'. "
    if len(password) < 8: return "Password is less then 8 characters. "
    found = False
    for i in range(10): 
        if str(i) in password: found = True
    if not found: return "Password must incude a number"
    if password.islower(): return "Password must have a capital letter. "
    return {"email":email, "password":password}
print(checkIfGood("ChrisIsAbum@gmail.com","ayaanIsABUM1234"))