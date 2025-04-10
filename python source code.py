import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector as sqltor
mycon = sqltor.connect(host="localhost", user="root", passwd="Anurag1031",
                       database="indira_gandhi_international_airport_flight_records")
print("                     INDIRA GANDHI INTERNATIONAL AIRPORT FLIGHT RECORDS")
q=input('Type Y/y if u wish to access the flight records and if not type N/n:')
while(q in ['Y','y']):
    if q=='Y' or q=='y':
        x = input('''To display details of domestic economy class,type T1 or t1
           To display details of domestic business class,type T2 or t2
           To display details of international economy class,type T3 or t3
           To display details of international business class class,type T4 or t4:''')
        if x == "T1" or x == "t1":
            x1 = input('''To display details of departure,type a1 or A1
                To display details of arrival,type a2 or A2
                To display the statistics of different airlines/flights with respect to number of passengers,type s1:''')
            if x1 == "a1" or x1 == "A1":
                y1 = input('''To display the names of passengers,type n1
                    To display the destinations,type p1
                    To display the diffrent flights/airlines,type r1
                    To display the details of passengers including name,destination,flight,time of departure,time of landing,type q1
                    To insert a new record,type f1:
                    To update an existing record, type k1:''')
                if y1 == "n1":
                    d1 = pd.read_sql("select PASSENGER_NAME from domestic_economyclass_departing;", mycon)
                    print(d1)
                if y1 == "p1":
                    d2 = pd.read_sql("select DESTINATION from domestic_economyclass_departing;", mycon)
                    print(d2)
                if y1 == "r1":
                    d3 = pd.read_sql("select distinct FLIGHT from domestic_economyclass_departing;", mycon)
                    print(d3)
                if y1 == "q1":
                    d4 = pd.read_sql("select PASSENGER_NAME,DESTINATION,FLIGHT,TIME_OF_DEPARTURE,TIME_OF_LANDING from domestic_economyclass_departing;",mycon)
                    print(d4)
                if y1 == "f1":
                    cursor = mycon.cursor()
                    slno = int(input('Enter slno:'))
                    name = input('Enter passenger name:')
                    destination = input('Enter destination:')
                    Flight = input('Enter flight:')
                    Time_of_departure = input('Enter time of departure:')
                    Time_of_landing = input('Enter time of landing:')
                    price = float(input('Enter price:'))
                    query = "insert into domestic_economyclass_departing values({},'{}','{}','{}','{}','{}',{})".format(slno,
                                                                                                                name,
                                                                                                                destination,
                                                                                                                Flight,
                                                                                                                Time_of_departure,
                                                                                                                Time_of_landing,
                                                                                                                price)
                    cursor.execute(query)
                    mycon.commit()
                    print("RECORD ENTERED SUCCESSFULLY")
                if y1 == "k1":
                    cursor = mycon.cursor()
                    SL_NO = int(input("Enter sl no:"))
                    price = int(input("Enter new price:"))
                    query = "update domestic_economyclass_departing set price={} where SL_NO={}".format(price,
                                                                                                SL_NO)
                    cursor.execute(query)
                    mycon.commit()
                    print("DATA UPDATED SUCCESSFULLY")
            if x1 == "a2" or x1 == "A2":
                y1 = input('''To display the names of passengers,type n2
                    To display the places that the passengers are arriving from,type p2
                    To display the diffrent flights/airlines,type r2
                    To display the details of passengers including name,place arriving from,flight,time of departure,time of landing,type q2
                    To insert a new record,type f2:
                    To update an existing record, type k2:''')
                if y1 == "n2":
                    d6 = pd.read_sql("select PASSENGER_NAME from domestic_economyclass_arriving;", mycon)
                    print(d6)
                if y1 == "p2":
                    d7 = pd.read_sql("select ARRIVING_FROM from domestic_economyclass_arriving;", mycon)
                    print(d7)
                if y1 == "r2":
                    d8 = pd.read_sql("select distinct FLIGHT from domestic_economyclass_arriving;", mycon)
                    print(d8)
                if y1 == "q2":
                    d9 = pd.read_sql("select PASSENGER_NAME,ARRIVING_FROM,FLIGHT,TIME_OF_DEPARTURE,TIME_OF_LANDING from domestic_economyclass_arriving;",mycon)
                    print(d9)
                if y1 == "f2":
                    cursor = mycon.cursor()
                    slno = int(input('Enter slno:'))
                    name = input('Enter passenger name:')
                    arriving_from = input('Enter destination:')
                    Flight = input('Enter flight:')
                    Time_of_departure = input('Enter time of departure:')
                    Time_of_landing = input('Enter time of landing:')
                    price = float(input('Enter price:'))
                    query = "insert into domestic_economyclass_arriving values({},'{}','{}','{}','{}','{}',{})".format(slno,
                                                                                                               name,
                                                                                                               arriving_from,
                                                                                                               Flight,
                                                                                                               Time_of_departure,
                                                                                                               Time_of_landing,
                                                                                                               price)
                    cursor.execute(query)
                    mycon.commit()
                    print("RECORD ENTERED SUCCESSFULLY")
                if y1 == "k2":
                    cursor = mycon.cursor()
                    SL_NO = int(input("Enter sl_no:"))
                    price = int(input("Enter new price:"))
                    query = "update domestic_economyclass_arriving set price={} where SL_NO={}".format(price,
                                                                                               SL_NO)
                    cursor.execute(query)
                    mycon.commit()
                    print("DATA UPDATED SUCCESSFULLY")
            if x1 == "s1":
                df = pd.read_sql("select distinct FLIGHT as flt,count(*) as cnt from domestic_economyclass_arriving group by FLIGHT;", mycon)
                df1 = pd.read_sql("select distinct FLIGHT as flt,count(*)as cnt from domestic_economyclass_departing group by FLIGHT;", mycon)
                plt.bar(df.flt, df.cnt, label="Arriving")
                plt.bar(df1.flt, df1.cnt, label="Departing")
                plt.title("Domestic Economy Class")
                plt.xlabel("Names of flights")
                plt.ylabel("Number of passengers")
                plt.legend(loc="upper right")
                plt.show()
        if x == "T2" or x == "t2":
            x2 = input('''To display details of departure,type b1 or B1
                To display details of arrival,type b2 or B2:
                To display the statistics of different airlines/flights with respect to number of passengers,type s2:''')
            if x2 == "b1" or x2 == "B1":
                y2 = input('''To display the names of passengers,type n1
                    To display the destinations,type p1
                    To display the diffrent flights/airlines,type r1
                    To display the details of passengers including name,destination,flight,time of departure,time of arrival,type q1
                    To insert a new record,type f1:
                    To update an existing record, type k1:''')
                if y2 == "n1":
                    d11 = pd.read_sql("select Passenger_name  from domestic_businessclass_departing;", mycon)
                    print(d11)
                if y2 == "p1":
                    d12 = pd.read_sql("select Destination from domestic_businessclass_departing;", mycon)
                    print(d12)
                if y2 == "r1":
                    d13 = pd.read_sql("select distinct Flight from domestic_businessclass_departing;", mycon)
                    print(d13)
                if y2 == "q1":
                    d14 = pd.read_sql("select Passenger_name,Destination,Flight,Time_of_departure,Time_of_landing from domestic_businessclass_departing;",mycon)
                    print(d14)
                if y2 == "f1":
                    cursor = mycon.cursor()
                    slno = int(input('Enter slno:'))
                    name = input('Enter passenger name:')
                    destination = input('Enter destination:')
                    Flight = input('Enter flight:')
                    Time_of_departure = input('Enter time of departure:')
                    Time_of_landing = input('Enter time of landing:')
                    price = float(input('Enter price:'))
                    query = "insert into domestic_businessclass_departing values({},'{}','{}','{}','{}','{}',{})".format(slno,
                                                                                                                 name,
                                                                                                                 destination,
                                                                                                                 Flight,
                                                                                                                 Time_of_departure,
                                                                                                                 Time_of_landing,
                                                                                                                 price)
                    cursor.execute(query)
                    mycon.commit()
                    print("RECORD ENTERED SUCCESSFULLY")
                if y2 == "k1":
                    cursor = mycon.cursor()
                    SL_NO = int(input("Enter sl no:"))
                    price = int(input("Enter new price:"))
                    query = "update domestic_businessclass_departing set price={} where SL_NO={}".format(price,
                                                                                                 SL_NO)
                    cursor.execute(query)
                    mycon.commit()
                    print("DATA UPDATED SUCCESSFULLY")

            if x2 == "a2" or x2 == "A2":
                y2 = input('''To display the names of passengers,type n2
                    To display the places that the passengers are arriving from,type p2
                    To display the diffrent flights/airlines,type r2
                    To display the details of passengers including name,place arriving from,flight,time of departure,time of landing,type q2
                    To insert a new record,type f2:
                    To update an existing record, type k2:''')
                if y2 == "n2":
                    d16 = pd.read_sql("select Passenger_name from domestic_businessclass_arriving;", mycon)
                    print(d16)
                if y2 == "p2":
                    d17 = pd.read_sql("select Arriving_from from domestic_businessclass_arriving;", mycon)
                    print(d17)
                if y2 == "r2":
                    d18 = pd.read_sql("select distinct Flight from domestic_businessclass_arriving;", mycon)
                    print(d18)
                if y2 == "q2":
                    d19 = pd.read_sql("select Passenger_name,Arriving_from,Flight,Time_of_departure,Time_of_landing from domestic_businessclass_arriving;",mycon)
                    print(d19)
                if y2 == "f1":
                    cursor = mycon.cursor()
                    slno = int(input('Enter slno:'))
                    name = input('Enter passenger name:')
                    arriving_from = input('Enter destination:')
                    Flight = input('Enter flight:')
                    Time_of_departure = input('Enter time of departure:')
                    Time_of_landing = input('Enter time of landing:')
                    price = float(input('Enter price:'))
                    query = "insert into domestic_businessclass_arriving values({},'{}','{}','{}','{}','{}',{})".format(slno,
                                                                                                                name,
                                                                                                                arriving_from,
                                                                                                                Flight,
                                                                                                                Time_of_departure,
                                                                                                                Time_of_landing,
                                                                                                                price)
                    cursor.execute(query)
                    mycon.commit()
                    print("RECORD ENTERED SUCCESSFULLY")
                if y2 == "k2":
                    cursor = mycon.cursor()
                    SL_NO = int(input("Enter sl no:"))
                    price = int(input("Enter new price:"))
                    query = "update domestic_businessclass_arriving set price={} where SL_NO={}".format(price,
                                                                                                SL_NO)
                    cursor.execute(query)
                    mycon.commit()
                    print("DATA UPDATED SUCCESSFULLY")
            if x2 == "s2":
                df = pd.read_sql("select distinct Flight as flt,count(*) as cnt from domestic_businessclass_arriving group by Flight;",mycon)
                df1 = pd.read_sql("select distinct Flight as flt,count(*)as cnt from domestic_businessclass_departing group by Flight;",mycon)
                plt.bar(df.flt, df.cnt, label="Arriving")
                plt.bar(df1.flt, df1.cnt, label="Departing")
                plt.title("Domestic Business Class")
                plt.xlabel("Names of flights")
                plt.ylabel("Number of passengers")
                plt.legend(loc="upper right")
                plt.show()
        if x == "T3" or x == "t3":
            x3 = input('''To display details of departure,type c1 or C1
                To display details of arrival,type c2 or C2
                To display the statistics of different airlines/flights with respect to number of passengers,type s3:''')
            if x3 == "c1" or x3 == "C1":
                y3 = input('''To display the names of passengers,type n1
                    To display the destinations,type p1
                    To display the different flights/airlines,type r1
                    To display the details of passengers including name,destination,flight,time of departure,time of landing,type q1
                    To insert a new record,type f1
                    To update an existing record, type k1:''')
                if y3 == "n1":
                    d21 = pd.read_sql("select PASSENGER_NAME from international_economyclass_departing;", mycon)
                    print(d21)
                if y3 == "p1":
                    d22 = pd.read_sql("select DESTINATION from international_economyclass_departing;", mycon)
                    print(d22)
                if y3 == "r1":
                    d23 = pd.read_sql("select distinct FLIGHT from international_economyclass_departing;", mycon)
                    print(d23)
                if y3 == "q1":
                    d24 = pd.read_sql("select PASSENGER_NAME,DESTINATION,FLIGHT,TIME_OF_DEPARTURE,TIME_OF_LANDING from international_economyclass_departing;",mycon)
                    print(d24)
                if y3 == "f1":
                    cursor = mycon.cursor()
                    slno = int(input('Enter slno:'))
                    name = input('Enter passenger name:')
                    destination = input('Enter destination:')
                    Flight = input('Enter flight:')
                    Time_of_departure = input('Enter time of departure:')
                    Time_of_landing = input('Enter time of landing:')
                    price = float(input('Enter price:'))
                    query = "insert into international_economyclass_departing values({},'{}','{}','{}','{}','{}',{})".format(slno,
                                                                                                                             name,
                                                                                                                             destination,
                                                                                                                             Flight,
                                                                                                                             Time_of_departure,
                                                                                                                             Time_of_landing,
                                                                                                                             price)
                    cursor.execute(query)
                    mycon.commit()
                    print("RECORD ENTERED SUCCESSFULLY")
                if y3 == "k1":
                    cursor = mycon.cursor()
                    SL_NO = int(input("Enter sl no:"))
                    price = int(input("Enter new price:"))
                    query = "update international_economyclass_departing set price={} where SL_NO={}".format(price,
                                                                                                     SL_NO)
                    cursor.execute(query)
                    mycon.commit()
                    print("DATA UPDATED SUCCESSFULLY")

            if x3 == "c2" or x3 == "C2":
                y3 = input('''To display the names of passengers,type n2
                    To display the places that the passengers are arriving from,type p2
                    To display the diffrent flights/airlines,type r2
                    To display the details of passengers including name,place arriving from,flight,time of departure,time of landing,type q2
                    To insert a new record,type f2:
                    To update an existing record, type k2:''')
                if y3 == "n2":
                    d26 = pd.read_sql("select PASSENGER_NAME from international_economyclass_arriving;", mycon)
                    print(d26)
                if y3 == "p2":
                    d27 = pd.read_sql("select ARRIVING_FROM from international_economyclass_arriving;", mycon)
                    print(d27)
                if y3 == "r2":
                    d28 = pd.read_sql("select distinct FLIGHT from international_economyclass_arriving;", mycon)
                    print(d28)
                if y3 == "q2":
                    d29 = pd.read_sql("select PASSENGER_NAME,ARRIVING_FROM,FLIGHT,TIME_OF_DEPARTURE,TIME_OF_LANDING from international_economyclass_arriving;",mycon)
                    print(d29)
                if y3 == "f2":
                    cursor = mycon.cursor()
                    slno = int(input('Enter slno:'))
                    name = input('Enter passenger name:')
                    arriving_from = input('Enter destination:')
                    Flight = input('Enter flight:')
                    Time_of_departure = input('Enter time of departure:')
                    Time_of_landing = input('Enter time of landing:')
                    price = float(input('Enter price:'))
                    query = "insert into international_economyclass_arriving values({},'{}','{}','{}','{}','{}',{})".format(slno,
                                                                                                                            name,
                                                                                                                            arriving_from,
                                                                                                                            Flight,
                                                                                                                            Time_of_departure,
                                                                                                                            Time_of_landing,
                                                                                                                            price)
                    cursor.execute(query)
                    mycon.commit()
                    print("RECORD ENTERED SUCCESSFULLY")
                if y3 == "k2":
                    cursor = mycon.cursor()
                    SL_NO = int(input("Enter sl no:"))
                    price = int(input("Enter new price:"))
                    query = "update international_economyclass_departing set price={} where SL_NO={}".format(price,
                                                                                                     SL_NO)
                    cursor.execute(query)
                    mycon.commit()
                    print("DATA UPDATED SUCCESSFULLY")
            if x3 == "s3":
                df = pd.read_sql("select distinct FLIGHT as flt,count(*) as cnt from international_economyclass_arriving group by FLIGHT;",mycon)
                df1 = pd.read_sql("select distinct FLIGHT as flt,count(*)as cnt from international_economyclass_departing group by FLIGHT;",mycon)
                plt.bar(df.flt, df.cnt, label="Arriving")
                plt.bar(df1.flt, df1.cnt, label="Departing")
                plt.title("International Economy Class")
                plt.xlabel("Names of flights")
                plt.ylabel("Number of passengers")
                plt.legend(loc="upper right")
                plt.show()
        if x == "T4" or x == "t4":
            x4 = input('''To display details of departure,type d1 or D1
                To display details of arrival,type d2 or D2:
                To display the statistics of different airlines/flights with respect to number of passengers,type s4:''')
            if x4 == "d1" or x4 == "D1":
                y4 = input('''To display the names of passengers,type n1
                    To display the destinations,type p1
                    To display the diffrent flights/airlines,type r1
                    To display the details of passengers including name,destination,flight,time of departure,time of landing,type q1
                    To insert a new record,type f1:
                    To update an existing record, type k1:''')
                if y4 == "n1":
                    d31 = pd.read_sql("select Passenger_name from international_businessclass_departing;", mycon)
                    print(d31)
                if y4 == "p1":
                    d32 = pd.read_sql("select Destination from international_businessclass_departing;", mycon)
                    print(d32)
                if y4 == "r1":
                    d33 = pd.read_sql("select distinct Flight from international_businessclass_departing;", mycon)
                    print(d33)
                if y4 == "q1":
                    d34 = pd.read_sql("select Passenger,Destination,Flight,Time_of_departure,Time_of_landing from international_businessclass_departing;",mycon)
                    print(d34)
                if y4 == "f1":
                    cursor = mycon.cursor()
                    slno = int(input('Enter slno:'))
                    name = input('Enter passenger name:')
                    destination = input('Enter destination:')
                    Flight = input('Enter flight:')
                    Time_of_departure = input('Enter time of departure:')
                    Time_of_landing = input('Enter time of landing:')
                    price = float(input('Enter price:'))
                    query = "insert into international_businessclass_departing values({},'{}','{}','{}','{}','{}',{})".format(slno,
                                                                                                                              name,
                                                                                                                              destination,
                                                                                                                              Flight,
                                                                                                                              Time_of_departure,
                                                                                                                              Time_of_landing,
                                                                                                                              price)
                    cursor.execute(query)
                    mycon.commit()
                    print("RECORD ENTERED SUCCESSFULLY")
                if y4 == "k1":
                    cursor = mycon.cursor()
                    SL_NO = int(input("Enter sl no:"))
                    price = int(input("Enter new price:"))
                    query = "update international_businessclass_departing set price={} where SL_NO={}".format(price,
                                                                                                      SL_NO)
                    cursor.execute(query)
                    mycon.commit()
                    print("DATA UPDATED SUCCESSFULLY")
            if x4 == "d2" or x4 == "D2":
                y4 = input('''To display the names of passengers,type n2
                    To display the places that the passengers are arriving from,type p2
                    To display the diffrent flights/airlines,type r2
                    To display the details of passengers including name,place arriving from,flight,time of departure,time of landing,type q2
                    To insert a new record,type f2:
                    To update an existing record, type k2:''')
                if y4 == "n2":
                    d36 = pd.read_sql("select Passenger_name from international_businessclass_arriving;", mycon)
                    print(d36)
                if y4 == "p2":
                    d37 = pd.read_sql("select Arriving_from from international_businessclass_arriving;", mycon)
                    print(d37)
                if y4 == "r2":
                    d38 = pd.read_sql("select distinct Flight from international_businessclass_arriving;", mycon)
                    print(d38)
                if y4 == "q2":
                    d39 = pd.read_sql("select Passenger_name,Arriving_from,Flight,Time_of_departure,Time_of_landing from international_businessclass_arriving;",mycon)
                    print(d39)
                if y4 == "f2":
                    cursor = mycon.cursor()
                    slno = int(input('Enter slno:'))
                    name = input('Enter passenger name:')
                    destination = input('Enter destination:')
                    Flight = input('Enter flight:')
                    Time_of_departure = input('Enter time of departure:')
                    Time_of_landing = input('Enter time of landing:')
                    price = float(input('Enter price:'))
                    query = "insert into international_businessclass_arriving values({},'{}','{}','{}','{}','{}',{})".format(slno,name,destination,Flight,
                                                                                                                             Time_of_departure,Time_of_landing,price)
                    cursor.execute(query)
                    mycon.commit()
                    print("RECORD ENTERED SUCCESSFULLY")
                if y4 == "k1":
                    cursor = mycon.cursor()
                    SL_NO = int(input("Enter sl no:"))
                    price = int(input("Enter new price:"))
                    query = "update international_businessclass_arriving set price={} where SL_NO={}".format(price,
                                                                                                     SL_NO)
                    cursor.execute(query)
                    mycon.commit()
                    print("DATA UPDATED SUCCESSFULLY")
            if x4 == "s4":
                df = pd.read_sql("select distinct Flight as flt,count(*) as cnt from international_businessclass_arriving group by Flight;",mycon)
                df1 = pd.read_sql("select distinct Flight as flt,count(*)as cnt from international_businessclass_departing group by Flight;",mycon)
                plt.bar(df.flt, df.cnt, label="Arriving")
                plt.bar(df1.flt, df1.cnt, label="Departing")
                plt.title("International Business Class")
                plt.xlabel("Names of flights")
                plt.ylabel("Number of passengers")
                plt.legend(loc="upper right")
                plt.show()
        q=input('would you like to continue,Y/y or N/n:')
    else:
        break
    print("Thank you for your time")
