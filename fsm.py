# Author: Vinit Patankar
# Date: Wednesday September 25 4:50 pm
# Program to calculate x % 3 using Finite Automata, where x is given by the user as a binary string

def run_fsm(input_string):
    """
    >>> print run_fsm(bin(0)[2:])
    0
    >>> print run_fsm(bin(1)[2:])
    1
    >>> print run_fsm(bin(2)[2:])
    2
    >>> print run_fsm(bin(3)[2:])
    0
    >>> print run_fsm(bin(4)[2:])
    1
    >>> print run_fsm(bin(5)[2:])
    2
    >>> print run_fsm(bin(6)[2:])
    0
    >>> print run_fsm(bin(7)[2:])
    1
    >>> print run_fsm(bin(8)[2:])
    2
    >>> print run_fsm(bin(9)[2:])
    0
    >>> print run_fsm(bin(29)[2:])
    2
    >>> print run_fsm(bin(1801)[2:])
    1
    >>> print run_fsm(bin(454893)[2:])
    0
    >>> print run_fsm(bin(5478950749238075)[2:])
    2
    >>> print run_fsm('1010100041010101')
    Error! Invalid binary string | Input contains number 4
    -1
    >>> print run_fsm('101010011101119010001')
    Error! Invalid binary string | Input contains number 9
    -1
    """
    fsm = {'00': 0,
           '01': 1,
           '10': 2,
           '11': 0,
           '20': 1,
           '21': 2
        }
    current_state = 0
    for c in input_string:
        if c not in '01':
            print('Error! Invalid binary string | Input contains number %s'%c)
            return -1
        new_state = str(current_state)
        current_state = fsm[new_state + c]
    return current_state

def main():

    input_string = raw_input("Please enter a binary string: ")
    if len(input_string) == 0:
        print "Error! Please enter a non-empty string"
        return
    print "User string: ", input_string
    current_state = run_fsm(input_string)
    if(current_state != -1):
        print current_state

if __name__ == "__main__":
    main()

