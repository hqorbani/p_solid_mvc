def person_type(age):
    if age > 19:
        return "old"
        # print ("old")
    else:
        return "young"
        # print("young")


if person_type(25) == "old":
    print("you are old and neeed to prepare.....")
else:
    print("you are young and neeed to prepare.....")