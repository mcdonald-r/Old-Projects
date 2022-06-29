import random 

def main():
    print('*** Welcome to The Password Generator ***\n')
    letters = int(input('How many letters do you want your password to contain? '))
    numbers = int(input('How many numbers do you want you password to contain? '))
    ask_special = input('Does it need to contain special characters? (Y) for yes, (N) for no) ')
    if ask_special == 'Y' or ask_special == 'y':
        special = int(input('How may special characters do you want your password to contain? '))
    else:
        special = 0
    upper = input('Does it need to contain uppercase and lowercase characters? (Y) for yes, (N) for no) ')

    print('')
    print(f'Your random generated password is:')
    pass_generator(letters, numbers, ask_special, special, upper)

def pass_generator(lets, nums, inc_spec, spec, up):
    if inc_spec == 'Y' or inc_spec == 'y':
        generated_pass = get_lets(lets, up) + get_nums(nums) + special_vals(spec)
        random.shuffle(generated_pass)
        for i in range(len(generated_pass)):
            print(generated_pass[i], end='')
    else:
        generated_pass = get_lets(lets, up) + get_nums(nums)
        random.shuffle(generated_pass)
        for i in range(len(generated_pass)):
            print(generated_pass[i], end='')
# 
def get_lets(lets, ups):
    string_lets = [0 for i in range(lets)]
    if ups == 'N' or ups == 'n':
        for i in range(lets):
            string_lets[i] = chr(random.randint(97, 122))
        return string_lets
    else:
        for i in range(lets):
            rand_val = random.randint(0, 1)
            if rand_val == 0:
                string_lets[i] = chr(random.randint(97, 122))
            else:
                string_lets[i] = chr(random.randint(65, 90))
        return string_lets

def get_nums(nums):
    string_nums = [0 for i in range(nums)]
    for i in range(nums):
        string_nums[i] = random.randint(0, 9)
    return string_nums

def special_vals(spec):
    string_spec = [0 for i in range(spec)]
    for i in range(spec):
        string_spec[i] = random.choice(['!', '#', '$', '%', '&', '*' ,'?', '/'])
    return string_spec

main()