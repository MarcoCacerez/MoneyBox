class MoneyBox:
    def __init__(self):
        self.coins = [];
        self.bills = [];
        self.total = 0;
        
    def addCoin(self,coin):
        self.coins.append(coin)
        
    def addBill(self,bill):
        self.bills.append(bill)
        
    def getCoins(self):
        coinsAmount = [0,0,0,0]
        for coin in self.coins:
            if coin == 1:
                coinsAmount[0] += 1
            if(coin == 2):
                coinsAmount[1] += 1
            if(coin == 5):
                coinsAmount[2] += 1
            if(coin == 10):
                coinsAmount[3] += 1
        return 'Monedas de 1: {}, Monedas de 2: {},Monedas de 5: {}, Monedas de 10: {}'.format(
            coinsAmount[0],coinsAmount[1],coinsAmount[2],coinsAmount[3]);

    def getBills(self):
        bill20,bill50,bill100,bill200,bill500,bill1000 = 0;
        
        for bill in self.bills:
            if bill == 20:
                bill20 += 1;
            if bill == 50:
                bill50 += 1;
            if bill == 100:
                bill100 += 1;
            if bill == 200:
                bill200 += 1;
            if bill == 500:
                bill500 += 1;
            if bill == 1000:
                bill1000 += 1;
        
        return f'Billetes de 20: {bill20}, 50: {bill50}, 100: {bill100}, 200: {bill200}, 500: {bill500}, 1000: {bill1000}';
    
    def getTotal(self):
        self.total = 0
        for coin in self.coins:
            self.total += coin
        for bill in self.bills:
            self.total += bill
        return self.total    
        
    def breakMb(self):
        del self.coins[:];
        del self.bills[:];
        del self.total;

mb = MoneyBox()
exit = True;
coins = [1,2,5,10]
bills = [20,50,100,200,500,1000]

while (exit):
    print('Opciones')
    print('(1) Agregar Moneda')
    print('(2) Cantidad de Monedas')
    print('(3) Agregar Billete')
    print('(4) Cantidad de Billetes')
    print('(5) Obtener total')
    print('(6) Romper Alcancia')
    print('(7) Salir')
    option = input('Seleccione opcion: ')
    
    if(option == '1'):
        coin = 0;
        while True:
            coin = int(input('ingresa la moneda(1,2,5,10): '))
            if coin in coins:
                break;
        mb.addCoin(coin)
    if(option == '2'):
        print(mb.getCoins());
    if(option == '3'):
        bill = 0;
        while True:
            bill = int(input('ingresa el billete(20,50,100,200,500,1000): '))
            if bill in bills:
                break;
        mb.addBill(bill)
    if(option == '4'):
        print(mb.getBills());
    if(option == '5'):
        print(f'Cantidad total {mb.getTotal()}')
    if(option == '6'):
        mb.breakMb();
        print('Alcancía Vacía')
    if(option == '7'):
        exit = False;