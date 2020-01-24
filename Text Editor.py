import os
def create():
    f2=open("Titles.txt","a")
    newtitle=input("\nEnter the title of the new list : ")
    f2.write(newtitle), f2.write("\n")
    f2.close()
    main()
def edit():
    fname=input("\nEnter the name of the file to be opened : ")
    fname=fname+".txt"
    refresh(fname)
def refresh(fname):
    try:
        f2=open(fname,"r")
    except IOError:
        print("\nRe-Enter")
        edit()
    print("\nContents of ",fname,"\n")
    count=0
    text=f2.readlines()
    for x in text:
        count+=1
        print("Line ",count,": ",x)
    f2.close()
    ch2=int(input("\nWhat would you want to do?\nEnter 1 to add to the list\nEnter 2 to delete a line\nEnter 3 to return to menu\nEnter 4 to exit\nYour choice : "))
    if ch2==1: addline(fname)
    elif ch2==2:
        lino=int(input("\nEnter the line number to be deleted : "))
        delline(fname,lino)
        refresh(fname)
    elif ch2==3: main()
    else : exit()
def addline(fname3):
    f3=open(fname3,"a")
    no=int(input("\nEnter no of lines : "))
    print("\nEnter text to be inputted\n")
    while (no>=1):
        f3.write(input())
        f3.write("\n")
        no-=1
    f3.close()
    refresh(fname3)
def delline(fname3,lno):
    f3=open(fname3,"r")
    f4=open("temp.txt","w")
    count=0
    line=f3.readlines()
    for x in line:
        count+=1
        if count==lno:
            if os.path.exists(x.strip('\n')+".txt"): os.remove(x.strip('\n')+".txt")
            continue
        f4.write(x)
    f3.close()
    f4.close()
    os.remove(fname3)
    os.rename("temp.txt",fname3)
def main():
    fname="Titles.txt"
    f1=open(fname,"a")
    f1=open(fname,"r")
    titles=f1.readlines()
    count=0
    print("\nContents of your Master List: \n")
    for x in titles:
        count+=1
        print(count,") ",x)
        f2=open((x.strip('\n')+".txt"),"a")
        f2.close()
    f1.close()
    ch1=int(input("\nWhat would you want to do?\nEnter 1 to create a new list\nEnter 2 to open a list\nEnter 3 to remove a list\nEnter 4 to exit\nYour choice : "))
    if ch1==1: create()
    elif ch1==2 : edit()
    elif ch1==3 :
        lino=int(input("\nEnter the line no of the list to be deleted : "))
        delline(fname,lino)
        main()
    else : exit()
    return
main()

