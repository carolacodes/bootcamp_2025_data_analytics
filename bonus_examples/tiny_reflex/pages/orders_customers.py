"""Orders and Customers page component."""

import reflex as rx
from tiny_reflex.state import State


def orders_customers_page() -> rx.Component:
    """Page displaying orders and customers join data."""
    return rx.fragment(
        rx.vstack(
            rx.heading("Orders & Customers", font_size="2em"),
            rx.link("← Back to Home", href="/", style={"text_decoration": "none"}),
            rx.button(
                "Load Orders & Customers",
                on_click=State.load_orders_customers,
                is_loading=State.loading_orders,
            ),
            rx.cond(
                State.loading_orders,
                rx.spinner(),
                rx.cond(
                    State.has_orders_data,
                    rx.data_table(
                        data=State.orders_customers_data,
                        columns=[
                            "order_id",
                            "order_date",
                            "company_name",
                            "contact_name",
                            "ship_name",
                            "ship_city",
                            "ship_country",
                            "freight",
                        ],
                        pagination=True,
                        search=True,
                        sort=True,
                    ),
                    rx.text(
                        "No data loaded. Click 'Load Orders & Customers' to fetch data."
                    ),
                ),
            ),
            spacing="1",
            padding="2em",
            width="100%",
        ),
    )
