def main():
    """
    ##################################################
    # Comlete your code here
    Use the same variables: celsius fahrenheit 



    ##################################################
    """
    celsius = int(input("Enter the tempature in celsius:"))   
    fahrenheit = celsius /5 *9 +32
    print (fahrenheit)

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return celsius, fahrenheit


if __name__ == '__main__':
    main()
