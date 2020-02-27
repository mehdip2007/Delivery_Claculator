#### based on the below inqiers are rate per KM
min_fee = 2
mid_fee = 3
max_fee = 5
fragile_fee = 10
additional_fee = 5

###### check whether your item is fragile to add on the your deposit 
def bool_validator(isFragile):
    if isFragile == 'y':
        isFragile = True
    if isFragile == 'n':
        isFragile = False
    return isFragile

bool_valRes = bool_validator(input("is your Item Fragile? [y/N]: " ))


#### function to calculate the fee rate
def radius_meter(Shipment_weight,Delivery_radius): 
    if Delivery_radius <= 10 and bool_valRes != True:
        return(Shipment_weight * 2)
    if Delivery_radius <= 10 and bool_valRes == True:
        return(Shipment_weight * 2 +  fragile_fee)
    if 10 < Delivery_radius <= 15 and bool_valRes != True:
        return(Shipment_weight * 3 + additional_fee)
    if 10 < Delivery_radius <= 15 and bool_valRes == True:
        return(Shipment_weight * 3 + additional_fee + fragile_fee)
    if Delivery_radius > 15 and bool_valRes != True:
        return(Shipment_weight * 5 + additional_fee)
    if Delivery_radius > 15 and bool_valRes == True:
        return(Shipment_weight * 5 + additional_fee + fragile_fee)

Delivery_radius = int(input("Enter your Delivery radius: "))
Shipment_weight = int(input("Enter your Shipment weight: "))
Total_Fee = radius_meter(Shipment_weight,Delivery_radius)


### write your output to the file
myFile = open('res.csv','a')
myFile.write('{},{},{},{}'.format(Delivery_radius,Shipment_weight,bool_valRes,Total_Fee) + '\n')
myFile.close()
