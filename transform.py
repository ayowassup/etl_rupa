import json


def transform_data(input_file, output_file):
    with open(input_file, 'r') as f:
        products = json.load(f)

    transformed_products = []
    for product in products:
        # Clean up rating format
        rating = product['rating'].replace(' |', '') if product['rating'] else None

        transformed_product = {
            'name': product['name'],
            'final_price': product['final_price'].replace('Rp', '').replace('.', '').strip(),
            'initial_price': product['initial_price'].replace('Rp', '').replace('.', '').strip() if product['initial_price'] else None,
            'discounted': product['discounted'],
            'rating': float(rating) if rating else None,
            'product_url': product['product_url'],
            'image_url': product['image_url']
            }
        transformed_products.append(transformed_product)

    with open(output_file, 'w') as f:
        json.dump(transformed_products, f, indent=2)

        print(f'Data successfully transformed and saved to {output_file}')


if __name__ == '__main__':
    transform_data('raw_products.json', 'transformed_products.json')
