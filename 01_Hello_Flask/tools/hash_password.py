from werkzeug.security import generate_password_hash, check_password_hash

pw_hash = generate_password_hash('mypassword')
print(pw_hash)
ck1 = check_password_hash(pw_hash, 'mypassword')
ck2 = check_password_hash(pw_hash, 'anotherpassword')
print(ck1, ck2)