# I can insert all values through main function by creating object for ENTITY

# Now I retrieve Variables and values


from ENTITY.Claim import *
obj=Claim()
obj.getter()
print(".....................................")
from ENTITY.Payment import *
obj=Payment()
obj.getter()
print("......................................")
from ENTITY.Client import *
obj=Client()
obj.getter()
print("......................................")
from ENTITY.User import *
obj=User()
obj.getter()
print(".......................................")

from ENTITY.InsuranceServiceImpl import InsuranceServiceImpl
obj=InsuranceServiceImpl()
obj.getter()

print('........................................')

from EXCEPTION.custom_exceptions import PolicyNotFoundException

class PolicyManager:
    policies_db = {1:'Policy A',2:'Policy B',3:'Policy C'}

    @staticmethod
    def get_policy(policy_number):
        if policy_number in PolicyManager.policies_db:
            return PolicyManager.policies_db[policy_number]
        else:
            raise PolicyNotFoundException("Policy not found in the database")

def main():
    try:

        user_policy_number=int(input("Enter policy number:"))

        policy_manager=PolicyManager()
        policy=policy_manager.get_policy(user_policy_number)

        print(f"Policy found: {policy}")

    except PolicyNotFoundException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
