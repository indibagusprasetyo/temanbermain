#operasi binary (biner) / bitwise
# or dalam bitwise "|"

a =  9
b =  5

#bitwise OR (|)
c = a | b
print('\n==========OR==========')
print('nilai : ',a,' binary :',format(a,'08b'))
print('nilai : ',b,' binary :',format(b,'08b'))
print("----------------------(|)")
print('nilai : ',c,' binary :',format(c,'08b'))

print("\n")

#bitwise OR (&)
c = a & b
print('\n==========AND==========')
print('nilai : ',a,' binary :',format(a,'08b'))
print('nilai : ',b,' binary :',format(b,'08b'))
print("----------------------(&)")
print('nilai : ',c,' binary :',format(c,'08b'))

print("\n")

#bitwise XOR (^)
c = a ^ b
print('\n==========XOR==========')
print('nilai : ',a,' binary :',format(a,'08b'))
print('nilai : ',b,' binary :',format(b,'08b'))
print("----------------------(^)")
print('nilai : ',c,' binary :',format(c,'08b'))

print("\n")

#bitwise NOT (~)
c = ~a
print('\n==========NOT==========')
print('nilai : ',a,' binary :',format(a,'08b'))
print("----------------------(~)")
print('nilai : ',c,' binary :',format(c,'08b'))
print("----------------------(^)")
d = 0b0000001001
e = 0b1111111111
print('nilai : ',e^d, ' binary :',format(e^d,'08b'))


#shift right (>>)
c = a >> 0 #ubah literal
print('\n==========>>==========')
print('nilai : ',a,' binary :',format(a,'08b'))
print("----------------------(>>)")
print('nilai : ',c,' binary :',format(c,'08b'))

#shift left (<<)
c = a << 5 #ubah literal
print('\n==========>>==========')
print('nilai : ',a,' binary :',format(a,'08b'))
print("----------------------(<<)")
print('nilai : ',c,' binary :',format(c,'08b'))