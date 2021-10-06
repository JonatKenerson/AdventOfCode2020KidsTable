

input = open("/content/Day2Input.txt") 

#Doing stuff to the input because I cannot wrap my mind around how to do anything with these inputs without doing stuff like this



#Function to split each line into its own dictionary
def make_dict(line):
  pw_and_policy_dict = {}
  pw_and_policy_list = line.split()

  min_max = pw_and_policy_list[0].split("-")
  pw_and_policy_dict["min"] = int(min_max[0])
  pw_and_policy_dict["max"] = int(min_max[1])

  pw_and_policy_dict["char"] = pw_and_policy_list[1][0]
  pw_and_policy_dict["pw"] = pw_and_policy_list[2]                               
  return pw_and_policy_dict

#List comprehension to turn this into a list of dictionaries
pw_and_policies_master = [make_dict(pw_and_policy) for pw_and_policy in input]




#Part 1

#Function to count how often "char" appears in a line and see if it's between "min" and "max"
def meets_policy(pw_and_policy):
  char_count_in_pw = pw_and_policy["pw"].count(pw_and_policy["char"])
  return pw_and_policy["min"] <= char_count_in_pw <= pw_and_policy["max"]

#Checking to see if this works. Counted the top 3 manually and made sure the results matched
print("Test runs: If results are false, false, true -> function works")
print(meets_policy(pw_and_policies_master[0]))
print(meets_policy(pw_and_policies_master[1]))
print(meets_policy(pw_and_policies_master[2]))
#It works!

#Google said this is how you do countif in python
how_many_meet_policy = sum(meets_policy(x) for x in pw_and_policies_master)
print("How many passwords meet the password policy?")
print(how_many_meet_policy)




#Part 2

def meets_actual_policy(pw_and_policy):
  position_one = pw_and_policy["min"]
  char_in_position_one = pw_and_policy["pw"][position_one - 1] == pw_and_policy["char"]

  position_two = pw_and_policy["max"]
  char_in_position_two = pw_and_policy["pw"][position_two - 1] == pw_and_policy["char"]

  return char_in_position_one ^ char_in_position_two

how_many_meet_actual_policy = sum(meets_actual_policy(x) for x in pw_and_policies_master)
print("How many passwords meet the actual password policy?")
print(how_many_meet_actual_policy)
