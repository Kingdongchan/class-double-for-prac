class cafeMenu:
    def order (self, name, price):
        cafe_food = name
        cafe_food_price = price

        def order_output(self):
         print(f"주문하신 {cafe_food} 나왔습니다.")

americano = cafeMenu("아메리카노", 5000)
cafelatte = cafeMenu("카페라떼", 5500)
bananalatte = cafeMenu("바닐라라뗴", 6000)

americano.order_output()
cafelatte.order_output()