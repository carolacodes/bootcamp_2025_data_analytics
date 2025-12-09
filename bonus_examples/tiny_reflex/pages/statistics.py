"""Statistics page component with charts and visualizations."""

import reflex as rx
from tiny_reflex.state import State


def statistics_page() -> rx.Component:
    """Page displaying statistics with charts and visualizations."""
    return rx.fragment(
        rx.vstack(
            rx.heading("Statistics", font_size="2em"),
            rx.link("← Back to Home", href="/", style={"text_decoration": "none"}),
            rx.button(
                "Load Statistics",
                on_click=State.load_statistics,
                is_loading=State.loading_statistics,
            ),
            rx.cond(
                State.loading_statistics,
                rx.spinner(),
                rx.cond(
                    State.has_statistics_data,
                    rx.vstack(
                        # Summary statistics cards
                        rx.hstack(
                            rx.box(
                                rx.vstack(
                                    rx.text(
                                        "Total Customers",
                                        font_size="0.9em",
                                        color="gray",
                                    ),
                                    rx.heading(
                                        State.total_customers,
                                        font_size="2em",
                                        color="blue",
                                    ),
                                    rx.text(
                                        "Registered customers",
                                        font_size="0.8em",
                                        color="gray",
                                    ),
                                    spacing="1",
                                    align="center",
                                ),
                                border="1px solid #e0e0e0",
                                border_radius="8px",
                                padding="1.5em",
                                bg="white",
                                box_shadow="0 2px 4px rgba(0,0,0,0.1)",
                                min_width="200px",
                            ),
                            rx.box(
                                rx.vstack(
                                    rx.text(
                                        "Total Orders", font_size="0.9em", color="gray"
                                    ),
                                    rx.heading(
                                        State.total_orders,
                                        font_size="2em",
                                        color="green",
                                    ),
                                    rx.text(
                                        "All orders", font_size="0.8em", color="gray"
                                    ),
                                    spacing="1",
                                    align="center",
                                ),
                                border="1px solid #e0e0e0",
                                border_radius="8px",
                                padding="1.5em",
                                bg="white",
                                box_shadow="0 2px 4px rgba(0,0,0,0.1)",
                                min_width="200px",
                            ),
                            rx.box(
                                rx.vstack(
                                    rx.text(
                                        "Average Freight",
                                        font_size="0.9em",
                                        color="gray",
                                    ),
                                    rx.heading(
                                        State.avg_freight_value,
                                        font_size="2em",
                                        color="purple",
                                    ),
                                    rx.text(
                                        "Average shipping cost",
                                        font_size="0.8em",
                                        color="gray",
                                    ),
                                    spacing="1",
                                    align="center",
                                ),
                                border="1px solid #e0e0e0",
                                border_radius="8px",
                                padding="1.5em",
                                bg="white",
                                box_shadow="0 2px 4px rgba(0,0,0,0.1)",
                                min_width="200px",
                            ),
                            spacing="4",
                            width="100%",
                            justify="center",
                            wrap="wrap",
                        ),
                        # Orders by country chart
                        rx.box(
                            rx.heading("Orders by Country (Top 10)", font_size="1.5em"),
                            rx.recharts.bar_chart(
                                rx.recharts.bar(
                                    data_key="orders",
                                    stroke="#8884d8",
                                    fill="#8884d8",
                                ),
                                rx.recharts.x_axis(data_key="country"),
                                rx.recharts.y_axis(),
                                rx.recharts.graphing_tooltip(),
                                rx.recharts.legend(),
                                data=State.orders_by_country_list,
                                width="100%",
                                height=350,
                            ),
                            width="100%",
                            padding="1em",
                        ),
                        # Customers by country chart
                        rx.box(
                            rx.heading(
                                "Customers by Country (Top 10)", font_size="1.5em"
                            ),
                            rx.recharts.bar_chart(
                                rx.recharts.bar(
                                    data_key="customers",
                                    stroke="#82ca9d",
                                    fill="#82ca9d",
                                ),
                                rx.recharts.x_axis(data_key="country"),
                                rx.recharts.y_axis(),
                                rx.recharts.graphing_tooltip(),
                                rx.recharts.legend(),
                                data=State.customers_by_country_list,
                                width="100%",
                                height=350,
                            ),
                            width="100%",
                            padding="1em",
                        ),
                        spacing="4",
                        width="100%",
                    ),
                    rx.text(
                        "No data loaded. Click 'Load Statistics' to fetch statistics."
                    ),
                ),
            ),
            spacing="1",
            padding="2em",
            width="100%",
        ),
    )
