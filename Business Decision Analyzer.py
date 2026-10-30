print('----------------------------')
print('-----Business Decision Analyzer-----')
print('----------------------------')

number_products = int(input('Enter the number of products to analyze: '))
products = []

for i in range(number_products):
    print('----------------------------')
    product = str(input('Enter the product name: '))
    category = str(input('Enter the product category: '))
    country = str(input('Enter the country of origin: '))
    price = float(input('Enter the product price (USD): '))
    cost = float(input('Enter the product cost: '))
    quantity = int(input('Enter the product quantity: '))

    products.append({
        'name': product,
        'category': category,
        'country': country,
        'price': price,
        'cost': cost,
        'quantity': quantity
    })

for product in products:
    
    def calculate_metrics(product):
        price = product['price']
        cost = product['cost']
        quantity = product['quantity']
        
        revenue = price * quantity
        total_cost = cost * quantity
        profit = revenue - total_cost
        profit_margin = (profit/revenue) * 100

        return revenue, total_cost, profit, profit_margin
    
    def business_recommendation(profit_margin):
        if profit_margin < 20:
            return('The product is low profitable. Business Recommendation: Review this product')
        elif profit_margin <= 50:
            return('The product is moderately profitable. Business Recommendation: Keep under observation')
        else:
            return('The product is highly profitable. Business Recommendation: Prioritize')


def main():

    for product in products:

        revenue, total_cost, profit, profit_margin = calculate_metrics(product)

        print('----------------------------')
        print(f"Product Name: {product['name']}")
        print(f"Category: {product['category']}")
        print(f"Country of Origin: {product['country']}")
        print(f"Price: ${product['price']:.2f}")
        print(f"Cost: ${product['cost']:.2f}")
        print(f"Quantity: {product['quantity']}")
        print(f'Revenue: ${revenue:.2f}')
        print(f'Total Cost: ${total_cost:.2f}')
        print(f'Profit: ${profit:.2f}')
        print(f'Profit Margin: {profit_margin:.2f}%')

        recommendation = business_recommendation(profit_margin)
        print(recommendation)

    print('--------------------------------------')
    print('-----Business Portafolio Analysis-----')
    print('--------------------------------------')

    total_products_analyzed = len(products)
    total_revenue = sum(p['price'] * p['quantity'] for p in products)
    total_cost = sum(p['cost'] * p['quantity'] for p in products)
    total_profit = total_revenue - total_cost

    most_profitable_product = max(products, key=lambda x: (x['price'] - x['cost']) * x['quantity'])
    highest_profit_margin = max(products, key=lambda x: ((x['price'] - x['cost']) / x['price']) * 100)

    print(f'Total Products Analyzed: {total_products_analyzed}')
    print(f'Total Revenue: ${total_revenue:.2f}')
    print(f'Total Cost: ${total_cost:.2f}')
    print(f'Total Profit: ${total_profit:.2f}')
    print('                                                           ')
    print(f'Most Profitable Product: {most_profitable_product["name"]}')
    print(f'Highest Profit Margin: {highest_profit_margin["name"]}')
    print('                                                           ')
    print(f'Overall Business Recommendation: ')
    print(f'Focus invesment on the most profitable product: {most_profitable_product["name"]} and the highest profit margin product: {highest_profit_margin["name"]}')

main()

