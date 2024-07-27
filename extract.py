import json
from curl_cffi import requests
from bs4 import BeautifulSoup


def fetch_page(page_num):
    url = f'https://www.ruparupa.com/jual/meja?query=meja&page={page_num}'
    response = requests.get(url, impersonate="chrome123")
    return response.content


def parse_page(content):
    soup = BeautifulSoup(content, 'html.parser')
    products = []

    for item in soup.select('.content__product'):
        # Name
        name_element = item.select_one('.product__name')
        name = name_element.text.strip() if name_element and name_element.text.strip() else None

        # Prices
        price_init_element = item.select_one('.price__initial')
        price_real_element = item.select_one('.price__real')

        price_initial = price_init_element.text.strip() if price_init_element and price_init_element.text.strip() else None
        price_real = price_real_element.text.strip() if price_real_element and price_real_element.text.strip() else None

        # Determine final price and discount status
        if price_real:
            final_price = price_real
            initial_price = price_initial if price_initial else None
            discounted = 'yes' if initial_price and price_real != price_initial else 'no'
        else:
            final_price = price_real
            initial_price = None
            discounted = 'no'

        # Rating
        rating_element = item.select_one('.ui-text-4.text__grey50')
        rating = rating_element.text.strip() if rating_element and rating_element.text.strip() else None

        # Product url
        product_url = item.select_one('#productsProductCard')['href'] if item.select_one(
            '#productsProductCard') else None

        # Image url
        image_element = item.select_one('.image.col-xs-12 img')
        image_url = image_element['src'] if image_element else None

        products.append({
            'name': name,
            'final_price': final_price,
            'initial_price': initial_price,
            'discounted': discounted,
            'rating': rating,
            'product_url': product_url,
            'image_url': image_url
        })

    return products


def scrape(pages):
    all_products = []
    for page in range(1, pages + 1):
        content = fetch_page(page)
        products = parse_page(content)
        all_products.extend(products)
        print(f'Page {page} scraped successfully.')

    # Filter out invalid entries
    valid_products = [product for product in all_products
                      if product['name'] != '\u200c' and product['final_price'] != '\u200c']

    return valid_products


if __name__ == '__main__':
    pages_to_scrape = 10
    products = scrape(pages_to_scrape)

    with open('raw_products.json', 'w') as f:
        json.dump(products, f, indent=2)

    print('Data successfully scraped and saved to raw_products.json')
