#!/usr/bin/python3
total_gold = 27
friends = 4
each_friend_gets = total_gold // friends
goblin_keeps = total_gold % friends
print("Each friend gets {} pieces. And the goblin keeps {} pieces.".format(each_friend_gets, goblin_keeps))
