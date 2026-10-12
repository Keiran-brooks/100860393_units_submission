# Place your answer to Lesson_04 in this file
# Do not rename or remove this file
is_raining = bool(int(input()))
no_hat = bool(int(input()))
takes_umbrella = True

if(is_raining and no_hat):
    takes_umbrella = True
else:
    takes_umbrella = False

print(takes_umbrella)