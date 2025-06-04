def patient_inset_data(name: str,age: int ) :
    if type(name)== str and type(age)== int :
        if age < 0:
            raise ValueError("Age cant be negative")
        else:
            print(name)
            print (age)
            print("Insert into the data base ")
    else:
        raise TypeError('Incorrect data type')
    
    
    def patient_update_data(name : str , age :int ):
        if type(name)==str and type(age)== int :
            print(name)
            print(age)
            print("update into the data base")
        else:
            raise TypeError("Incorrect datatype")


# this is called type intinfg (name: str,age: int ) 
#type inting for giving only information not to raise error 
    
# in dfault pyhton doesnt have type validation so to achieve this we use pydantic for type validation
    
# patient_inset_data('bhushan ' ,21)
patient_inset_data('nitish','30')


