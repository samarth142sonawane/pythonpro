class kbc:
    def __init__(self):
        self.question = [
            ["\033[1mQue.1 what is the capital of india ?\033[0m" , "1.kolkatta","2.mumbai","3.Delhi","4.Banglor","3","1.Kolkatta  3.Delhi"],
            ["\033[1mQue.2 Who is the PM of India ?\033[0m" , "1.Modi","2.Yogiji","3.Yadav","4.Gndhi","1","1.Modi  2.Yogiji"],
            ["\033[1mQue.3 which is the national animal of India ?\033[0m" , "1.eliphant","2.Tiger","3.pig","4.Cow","2","2.Tiger  4.Delhi"],
            ["\033[1mQue.4 which  country is not a part middle east  ?\033[0m" , "1.Quatar","2.UAE","3.Iran","4.Turkey","4","2.UAE  4.Turkey"],
            ["\033[1mQue.5 what is the financial capital of india ?\033[0m" , "1.kolkatta","2.mumbai","3.Delhi","4.Banglor","2","2.mumbai  3.Delhi"],
            ["\033[1mQue.6 Who is the PM of India ?\033[0m" , "1.Modi","2.Yogiji","3.Yadav","4.Gandhi","1","1.Mdi  2.Yogiji"],
            ["\033[1mQue.7 which is the national bird of India ?\033[0m" , "1.Crow","2.picock","3.sparrow","4.Buffelow","2","2.Picock  3.Sparrow"],
            ["\033[1mQue.8 which  country is not a part of BRICKS  ?\033[0m" , "1.India","2.Brazil","3.China","4.America","4","1.India  4.America"],
            ["\033[1mQue.9 Where is Rahata city located ?\033[0m" , "1.Bihar","2.Assam","3.Rajastan","4.Mharashtra","4","2.Assam  4.Maharashtra"], #8
            ["\033[1mQue.10 Who is the CEO of Goole ?\033[0m" , "1.Sundar ","2.Jethalal","3.Tapu","4.Hathi bhai","1","1.Sundar  3.Tapu"],
            ["\033[1mQue.11 Who is the CEO of Microsoft ?\033[0m" , "1.Satkela ","2.Katela","3.Nadela","4.hatela","3","1.Satkela  3.Nadela"],
            ["\033[1mQue.12 Who is the god of cricket ?\033[0m" , "1.Kohali ","2.Tendulkar","3.Dhoni","4.Rohit","2","1.Kohali  2.Tendulkar"],
            ["\033[1mQue.13 How many overs are there in a one day cricket match  ?\033[0m" , "1. 20 ","2. 50","3. 100.","4. 15","2","1. 20  2. 50"],
            ["\033[1mQue.14 V. Richards comes from which country ?\033[0m" , "1.zimbabwe ","2.S.Africa","3.England","4. W.Indies","4","1.Zimbombay  4. W.Indies"]
        ]
    def play(self):
        level = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000]
        money = 0
        for q in range(0,len(self.question)):
            que=self.question[q]

            print(f"\n\n_____________________This question is for {level[q]} Rs.________________________\n")
            print(que[0])
            print(f"{que[1]}                  {que[2]}")
            print(f"{que[3]}                  {que[4]}")
            ans = input("\n * Choose correct option /or/ Press \"0\" to quit /or/ press \"L\" for lifeline ->  ")
            if ans == 0:
                print(f"Your take home money is {money} Rs /-")
            elif ans == "L":
                print("Warning!!!  : You cannot go forward after correcting it. You can take only Amount of these question.")
                put =input("Want to go forward?(yes/no)")
                if put == "no":
                    continue
                elif put =="yes":
                    give=input(f"so choose correct from {que[6]}")
                    if give == que[5]:
                        print(f"          sahi jawab!! Your take home money is {level[q]}")
                        exit()
                    else:
                        print(f"           your wrong xxxxxxx Your take home money is {money}")   
                else:
                    print("Wrong input")
                    continue
            elif ans == que[5]:
                print("\n\033[1m!!!!!!!! Sahi jawab !!!!!!!!!\n")
                if q == 2 :
                    money = 3000
                elif q == 4:
                    money = 10000
                elif q == 8:
                    money = 160000
                elif q == 11:
                    money = 1250000
                elif q == 12:
                    money = 2500000
                elif q == 14:
                    print("Excelent**************")
                    money = 5000000
            else:
                print("\n\033[1mxxxxx Galat jawab xxxxxx\n")
                print(f"        ||  Your take home money is {money}/-    ||         \n")
                exit()
game = kbc()
game.play()