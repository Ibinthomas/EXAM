import num
from add import add
from sub import sub
from div import div
from mult import mult
from mode import mode
while True:
    print("""
            1.Add
            2.Sub
            3.Div
            4.Mode
            5.Mul
""")
    choice=int(input("enter the choice :"))

    if choice==1:
        a,b=num.num()
        add(a,b)
    elif choice==2:
        a,b=num.num()
        sub(a,b)
    elif choice==3:
        a,b=num.num()
        div(a,b)
    elif choice==4:
        a,b=num.num()
        mode(a,b)
    elif choice==5:
        a,b=num.num()
        mult(a,b)
    elif choice==6:
        break
    else:
        print("invalid choice")

    


