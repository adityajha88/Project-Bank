import pymysql
#global variables
db=None
cur=None
def connectDB():
    global db
    global cur
    db = pymysql.connect(host="localhost",
			user="root",
			password="",
			database="Bank")
    cur = db.cursor()

def disconnectDB():
    cur.close()
    db.close()

def openAcc():
    n=input("Enter Your Name : ")
    ac=input("Enter Account No : ")
    dob=input("Enter Your D.O.B : ")
    ph=input("Enter Your Phone No : ")
    ad=input("Enter Your Address : ")
    ob=int(input("Enter Your Opening balance : "))
    connectDB()
    data1=(n,ac,dob,ph,ad,ob)
    data2=(n,ac,ob)
    sql1="insert into account values('{}','{}','{}','{}','{}','{}')".format(n,ac,dob,ph,ad,ob)
    sql2="insert into amount values('{}','{}','{}')".format(n,ac,ob)
    cur.execute(sql1)
    cur.execute(sql2)
    print('Details Entered Successfully')
    db.commit()
    disconnectDB()
    menu()
def deposite():
    am=int(input("Enter Amount : "))
    ac=input("Enter Account No : ")
    a='select balance from amount where acno=%s'
    data=(ac,)
    connectDB()
    cur.execute(a,data)
    result=cur.fetchone()
    tam=result[0] +am
    sql='update amount set balance =%s where acno=%s'
    d=(tam,ac)
    cur.execute(sql,d)
    db.commit()
    disconnectDB()
    menu()
class MinimumBalanceError(Exception):
    def __init__(self):
        print('Sorry ! You Cannot Withdraw the amount due to Minimum Balance Policey\nThe minimum balance to be maintained is 5000')

def withdraw():
        am=int(input("Enter Amount : "))
        ac=input("Enter Account No : ")
        a='select balance from amount where acno=%s'
        data=(ac,)
        connectDB()
        cur.execute(a,data)
        result=cur.fetchone()
        if result[0]<= am:
             MinimumBalanceError()
        else:
            tam=result[0] -am
            sql='update amount set balance =%s where acno=%s'
            d=(tam,ac)
            cur.execute(sql,d)
            db.commit()
            disconnectDB()
            print('Withdrawal Excepted !!!' )
            menu()
def balance():
    ac=input("Enter Account No : ")
    a='select balance from amount where acno=%s'
    data=(ac,)
    connectDB()
    cur.execute(a,data)
    result=cur.fetchone()
    print("Balance for Account: ",ac,"is" ,result[0])
    disconnectDB()
    menu()
def chOwner():
    ac=input("Enter Account No : ")
    n=input("Enter New Name : ")
    a= "update account set name='{}' where acno={}".format(n,ac)
    b= "update amount set name='{}' where acno={}".format(n,ac)
    connectDB()
    cur.execute(a)
    cur.execute(b)
    db.commit()
    disconnectDB()
    menu()
def closeac():
     ac=input("Enter Account No : ")
     sql1='delete from account where acno=%s'
     sql2='delete from amount where acno=%s'
     data=(ac,)
     connectDB()
     cur.execute(sql1,data)
     cur.execute(sql2,data)
     db.commit()
     disconnectDB()
     menu()

def menu():
   print("""
      1.Open a Bank Account
      2.Perform Transcation For an Account
      3.Exit the Application""")
   choice=int(input("Enter Your Choice: "))
   while True:
      if choice==3:
           break
      elif choice==1:
          openAcc()
      elif choice==2:
          print('''Select any One
                1.Deposite Money
                2.Withdraw Money
                3.Change Owner Name
                4.Remaining Balance
                5.Close an Account
                6.Exit''') 
          sub=int(input("Enter Your Task: "))
          if (sub==6):
              break
          elif (sub==1):
             deposite()
          elif (sub==2):
             withdraw()
          elif (sub==3):
             chOwner()
          elif (sub==4):
             balance()
          elif (sub==5):
             closeac()
          else:
            print('Please Enter the correct Choice')
            menu()
      else:
          print('Please Enter the correct Choice')
          menu()
menu()            
     
     
    

    
