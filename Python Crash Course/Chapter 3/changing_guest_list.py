# 3-5. Changing Guest List. You just head that one of your guests can't make the
# dinner, so you need to send out a new set of invitations. You'll have to think of
# someone else to invite.
#
#   * Start with your program from Exercise 3-4. Add a print() call at the end of
#     your program, stating the name of the guest who cant make it.
#   
#   * Modify your list, replacing the name of the guest who cant make it with the
#     name of the new person you are inviting.
#
#   * Print a second set of invitation messages, one for each person who is still in
#     your list.

guestList = ['Ricardo', 'ricky', 'bro']

print(f"Would you please come to dinner with me {guestList[0].title()} ?")

print(f"How about one last meal {guestList[1].title()} ?")

print(f"Hey {guestList[2].title()} lets go to dinner everyday")

print(f"{guestList[1].title()} cant make it to dinner.")

guestList = ['Ricardo', 'amy', 'bro']

print(f"Would you please come to dinner with me {guestList[0].title()} ?")

print(f"How about one last meal {guestList[1].title()} ?")

print(f"Hey {guestList[2].title()} lets go to dinner everyday")

