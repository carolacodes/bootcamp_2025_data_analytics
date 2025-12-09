"""Customers page component."""

import reflex as rx
from tiny_reflex.state import State


def customers_page() -> rx.Component:
    """Page displaying customers data."""
    return rx.fragment(
        rx.vstack(
            rx.heading("Customers", font_size="2em"),
            rx.link("← Back to Home", href="/", style={"text_decoration": "none"}),
            rx.button(
                "Load Customers",
                on_click=State.load_customers,
                is_loading=State.loading_customers,
            ),
            rx.cond(
                State.loading_customers,
                rx.spinner(),
                rx.cond(
                    State.has_customers_data,
                    rx.data_table(
                        data=State.customers_data,
                        columns=[
                            "customer_id",
                            "company_name",
                            "contact_name",
                            "contact_title",
                            "city",
                            "country",
                            "phone",
                        ],
                        pagination=True,
                        search=True,
                        sort=True,
                    ),
                    rx.text("No data loaded. Click 'Load Customers' to fetch data."),
                ),
            ),
            spacing="1",
            padding="2em",
            width="100%",
        ),
    )
