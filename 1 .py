#create a list of cars as dictionaries
car = [
{'car_id':"C001",'make':"toyota",'model':"innova",'year':2022,'available':True}, 
{'car_id':"C002",'make':"honda",'model':"accord",'year':2022,'available':True}, 
{'car_id':"C003",'make':"maruti",'model':"swift",'year':2022,'available':True}  
]
#create a list of customers as dictionaries
customers = [
{'customer_id':"CU001",'name':"nikita vaidya",'rented_cars':[]},
{'customer_id':"CU002",'name':"harsh dubey",'rented_cars':[]},
{'customer_id':"CU003",'name':"shivam meshram",'rented_cars':[]},
]
#create a list to store rentals as dictionaries
rentals =[]
def rent_car(customer,car):
    if car['available']:
        car['available']=False
        customer['rented_cars'].append(car)
        return True
    return False
#function to return a car
def return_car(customer,car):
    if car in customer['rented_cars']:
        car['available']=True
        customer['rented_cars'].remove(car)
        return True
    return False
#rent cars
rent_car(customers[0],car[0])
rent_car(customers[1],car[1])
rent_car(customers[2],car[2])
#display rented cars for customers
print(f"{customers[0]['name']}'s rented cars:{[car['make']for car in customers[0]['rented_cars']]}")
print(f"{customers[1]['name']}'s rented cars:{[car['make']for car in customers[1]['rented_cars']]}")
print(f"{customers[2]['name']}'s rented cars:{[car['make']for car in customers[2]['rented_cars']]}")
#return cars
return_car(customers[0],car[0])
return_car(customers[2],car[0])
#display updated rented car for customers
print(f"{customers[0]['name']}'s updated rented cars:{[car['make']for car in customers[0]['rented_cars']]}")
print(f"{customers[1]['name']}'s updated rented cars:{[car['make']for car in customers[1]['rented_cars']]}")
print(f"{customers[2]['name']}'s updated rented cars:{[car['make']for car in customers[2]['rented_cars']]}")
#create rentals and add to the list
rentals.append({'rental_id':"R001",'customer':customers[0],'car':car[0],'rental_fee':500.0})
rentals.append({'rental_id':"R002",'customer':customers[1],'car':car[1],'rental_fee':450.0})
rentals.append({'rental_id':"R003",'customer':customers[2],'car':car[2],'rental_fee':350.0})
#display rental information
for rental in rentals:
    print(f"rental ID:{rental['rental_id']},customer:{rental['customer']['name']},car:{rental['car']['make']},rental fee:INR{rental['rental_fee']}")



