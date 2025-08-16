import utils


def main():
    student_name = input("Enter  your name")
    is_like_founder = utils.is_given_name_like_founder_name(student_name)
    if is_like_founder:
        print('Oh, your name like in the founder of our company')
    else:
        print('Nothing special in your name')
    print('By')


main()
