candidate_vote_count={
    'party1':0,
    'party2':0,
    'party3':0
}
voter_set=set()

def vote():
    votername=input("enter our name").strip()
    if votername in voter_set:
        print("can not vote again")
        return
    candidate_name=input("enter the candidate name you ant t vote:").strip()

    if candidate_name in candidate_vote_count:
        candidate_vote_count[candidate_name] += 1
        print("vote recorded")
    else:
        print("nvalid candidate name")

def display_result():
    print("\nNo of count of this person:")
    for candidate,count in candidate_vote_count.items():
        print(f"{candidate}:{count}")

    winner = max(candidate_vote_count,key=candidate_vote_count.get)
    print(f"\nwinner:{winner}")

while True:
    print("\n1.vote")
    print("2.result")
    print("3.exit")
    choice = int(input("enter our choice:"))

    if choice == 1:
         vote()
    elif choice == 2:
         display_result()
    elif choice == 3:
        break
    else:
        print("invalid choice")


