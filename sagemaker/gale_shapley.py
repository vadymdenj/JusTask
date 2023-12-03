# Number of users entered into AWS RDS (min is 2)
uid_count = 4
 
# Function for determining whether uid1 has uid2 higher on pref list than uid3
# Returns True if yes, False if no
def uid1_Prefers_uid2_Over_uid3(prefer, uid_1, uid2, uid3):
    for i in range(uid_count): 
        if (prefer[uid_1][i] == uid3):
            return True
        if (prefer[uid_1][i] == uid2):
            return False
 
# Prints stable matching between N by N user matrix
# uid group 1 are numbered as 0 to N-1. 
# uid group 2 are numbered as N to 2N-1.
def stable_match(pref):
     
    uid1 = [-1 for i in range(uid_count)]
    free_match = [False for i in range(uid_count)]
    count = uid_count

    while (count > 0):
        u = 0
        while (u < uid_count):
            if (free_match[u] == False):
                break
            u += 1
 
        i = 0
        while i < uid_count and free_match[u] == False:
            u2 = pref[u][i]
            if (uid1[u2 - uid_count] == -1):
                uid1[u2 - uid_count] = u
                free_match[u] = True
                count -= 1
 
            else: 
                u1 = uid1[u2 - uid_count]
                if (uid1_Prefers_uid2_Over_uid3(pref, u2, u, u1) == False):
                    uid_count[u2 - uid_count] = u
                    free_match[u] = True
                    free_match[u1] = False
            i += 1
 
    # Matrix print
    print("UID 1 ", " UID2")
    for i in range(uid_count):
        print(i + uid_count, "\t", uid1[i])
 
# Incompatibility score (1 to 10, based on time compatibility, interest, etc) decides matchings 
# Then, users are matched based on their preferences
pref = [[0, 2, 1, 3], [1, 6, 2, 3],
          [0, 1, 7, 3], [0, 1, 2, 3],
          [3, 5, 6, 4], [5, 3, 6, 7],
          [4, 1, 8, 7], [4, 5, 2, 7]]
stable_match(pref)
 