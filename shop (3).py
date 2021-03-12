#kadari faulkner 3/12/2021


def check_money(total_cost, customer_money):
    #Your code here
    if total_cost>customer_money:
        return False
    else:
        return True


#This should print False
can_pay = check_money(107, 49)
print(can_pay)

#This should print True
can_pay = check_money(6, 88)
print(can_pay)
