import json

dict={
    "Andhra Pradesh":"Amaravati",
    "Arunachal Pradesh":"Itanagar",
    "Assam":"Dispur",
    "Bihar":"Patna",
    "Chhattisgarh":"Raipur",
    "Goa":"Panaji",
    "Gujarat":"Gandhinagar"
    }

file=open('C:\\Users\\HP\\OneDrive\\Documents\\Edyoda py practice\\python file handling\\Edyoda_assignment_6\\Assignment1_task2\\json_write.json','w')
json.dump(dict,file)