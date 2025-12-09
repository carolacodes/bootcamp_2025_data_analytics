"""Main application file for Reflex app."""

import reflex as rx
from tiny_reflex.pages.index import index
from tiny_reflex.pages.customers import customers_page
from tiny_reflex.pages.orders_customers import orders_customers_page
from tiny_reflex.pages.statistics import statistics_page

# Create and configure the app
app = rx.App()

# Register all pages
app.add_page(index, route="/")
app.add_page(customers_page, route="/customers")
app.add_page(orders_customers_page, route="/orders-customers")
app.add_page(statistics_page, route="/statistics")
