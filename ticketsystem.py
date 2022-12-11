TICKET_PRICE = 10
SERVICE_CHARGE = 2

tickets_remaining = 100

# Create a function to calculate the price
def calculate_price(ticket_amount):
    return (ticket_amount * TICKET_PRICE) + SERVICE_CHARGE


while tickets_remaining >= 1:
    print('There are {} tickets remaining'.format(tickets_remaining))

    # Capture the user's name and assign it to a new variable
    name = input('What is your name?: ')

    # Ask how many tickets they would like and calculate the price
    ticket_amount = input(
        '{}, How many tickets would you like?: '.format(name))
    # Expect a ValueError to happen and handle it appropriately
    try:
        ticket_amount = int(ticket_amount)
        # Raise a ValueError if the request is more tickets than there are available
        if ticket_amount > tickets_remaining:
            raise ValueError(
                'Sorry, there are only {} tickets remaining.'.format(tickets_remaining))
    except ValueError as err:
        print('Sorry, invalid input {}'.format(err))
    else:
        price = calculate_price(ticket_amount)
        print('Your total is ${} for {} tickets'.format(price, ticket_amount))

        # Prompt the user if they want to proceed Y/N
        proceed = input(
            'Would you like to proceed with your purchase? yes/no: ')
        if proceed.lower() == 'yes':

            # TODO: Gather credit card information and process it

            print('Sold!')
            tickets_remaining -= ticket_amount
        else:
            print('Thank you {}, hope to see you again soon.'.format(name))

# Notify the user when the tickets are sold out
print('Sorry, the tickets are sold out.')
