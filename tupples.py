point = [5,6]
print(point[1]) #6
print(type(point)) #list
point = (5,6)
print(type(point)) #tuple
# point[1]=7  ----> error // 'tuple' object does not support item assignment
point_3d = (5,8,10)
print(point_3d)


def find_pe_and_pb(price, eps, book_value):
    pe = price/eps
    pb = price/book_value
    return (pe, pb)
# val =find_pe_and_pb(100,2,4)
# print(val[0]) #50.0
# print(val[1]) #25.0

pe_ratio, pb_ratio =find_pe_and_pb(100,2,4)

print(pe_ratio) #50.0
print(pb_ratio) #25.0

contacts = [('rachel',889787342),('monica',539787342),('joey',333387342)]
for contact in contacts:
    if contact[0]=="monica":
        print(contact[1])

