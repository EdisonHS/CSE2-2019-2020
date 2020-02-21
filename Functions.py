def say_hi():
    print("Hello!")


say_hi()


def create_divider():
    print()
    print("----------------------")
    print()


create_divider()


def pokemon():
    print("""quu..__
 $$$b  `---.__
  "$$b        `--.                          ___.---uuudP
   `$$b           `.__.------.__     __.---'      $$$$"              .
     "$b          -'            `-.-'            $$$"              .'|
       ".                                       d$"             _.'  |
         `.   /                              ..."             .'     |
           `./                           ..::-'            _.'       |
            /                         .:::-'            .-'         .'
           :                          ::''\          _.'            |
          .' .-.             .-.           `.      .'               |
          : /'$$|           .@"$\           `.   .'              _.-'
         .'|$u$$|          |$$,$$|           |  <            _.-'
         | `:$$:'          :$$$$$:           `.  `.       .-'
         :                  `"--'             |    `-.     \
        :##.       ==             .###.       `.      `.    `\
        |##:                      :###:        |        >     >
        |#'     `..'`..'          `###'        x:      /     /
         \                                   xXX|     /    ./
          \                                xXXX'|    /   ./
          /`-.                                  `.  /   /
         :    `-  ...........,                   | /  .'
         |         ``:::::::'       .            |<    `.
         |             ```          |           x| \ `.:``.
         |                         .'    /'   xXX|  `:`M`M':.
         |    |                    ;    /:' xXXX'|  -'MMMMM:'
         `.  .'                   :    /:'       |-'MMMM.-'
          |  |                   .'   /'        .'MMM.-'
          `'`'                   :  ,'          |MMM<
            |                     `'            |tbap\
             \                                  :MM.-'
              \                 |              .''
               \.               `.            /
                /     .:::::::.. :           /
               |     .:::::::::::`.         /
               |   .:::------------\       /
              /   .''               >::'  /
              `',:                 :    .'

------------------------------------------------
Thank you for visiting https://asciiart.website/
This ASCII pic can be found at
https://asciiart.website/index.php?art=video%20games/pokemon
    """)


pokemon()


def party(cheese, crackers):
    print("We have {} blocks of cheese and "
          "{} crackers".format(cheese, crackers))


party(10, 15)
party(20, 25)
party(15 * 4, 200 - 50)
create_divider()


def add_stuff(num1, num2):
    print("{} + {}".format(num1, num2))
    answer = num1 + num2
    print("The answer is {}".format(answer))


add_stuff(5, 7)
# Answer is a local variable


def subtract(num1, num2):
    print("SUBTRACTING {} and {}".format(num1, num2))
    return num1 - num2


age = subtract(10, 5)


def f(x):
    return x**2 + 3*x + 9


print(f(3))
print(f(9))
print(f(27))


def divisible_by_2(number):
    if number % 2 == 0:
        return True
    return False


# Nothing will be executed as soon as I get to
# a "Return" statement

def divisible_by_7(number):
    return number % 7 == 0


for i in range(1000):
    if divisible_by_2(i) and divisible_by_7(i):
        print(i)


def can_i_sleep_in(weekday, vacation):
    """If it is vacation, I can sleep in.
    If it is not a weekday, I can sleep in"""
    if vacation:
        return True
    elif not weekday:
        return True
    return False