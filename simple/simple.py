def oddoreven():
    while(True):    
        try: 
            num=int(input("Enter a number: "))
            if num%2==0:
                print("Even" )
            else:
                print("Odd" )
        except:
            print("Invalid input!")

def listandtuple():
    List=[1,2,3,4,5]
    Tuple=(1,2,3,4,5)
    print(List)
    print(Tuple)
def sets():
    #Set is collection of 
    #sets=set(1,2,3,4)
    SET={1,2,3,4}
    for read in SET :
        print(read, )
oddoreven()