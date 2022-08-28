cli = input().split()

cod, quant = cli

cod = int(cod)
quant = int(quant)

if cod == 1 :
    print('Total: R$ {:.2f}' .format(4.00 * quant))
elif cod == 2 :
    print ('Total: R$ {:.2f}' .format(4.50 * quant))
elif cod == 3 :
    print('Total: R$ {:.2f}' .format(5.00 * quant))
elif cod == 4 :
    print('Total: R$ {:.2f}' .format(2.00 * quant))
elif cod == 5:
    print('Total: R$ {:.2f}' .format(1.50 * quant))