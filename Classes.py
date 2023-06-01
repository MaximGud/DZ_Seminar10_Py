class Coffee:
  def __init__(self, mark: str, price: int, milk: str):
    self.mark = mark
    self.price = price
    self.milk = milk
    
  def __str__(self):
    return f'Кофе марки {self.mark}, цена: {self.price}, {self.milk}'

def coffee_buy(choice: int):
    match choice:
      case 1:
        print(f'Вы выбрали {capuchino}. К оплате {capuchino.price}. Спасибо за покупку!')  
      case 2:
        print(f'Вы выбрали {americano}. К оплате {americano.price}. Спасибо за покупку!') 
      case 3:
        print(f'Вы выбрали {latte}. К оплате {latte.price}. Спасибо за покупку!') 


capuchino = Coffee('Капучино', 120, 'с молоком')
americano = Coffee('Американо', 100, 'без молоком')
latte = Coffee('Латте', 150, 'с молоком')


choice = int(input('''К Вашим услугам кофейный аппарат!
Выберите кофе:
1. Капучино
2. Американо
3. Латте\n'''))

coffee_buy(choice)