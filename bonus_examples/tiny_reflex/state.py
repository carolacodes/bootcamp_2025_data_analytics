"""Application state management."""

import reflex as rx
from tiny_reflex.types import CustomerData, OrderCustomerData, StatisticsData
from tiny_reflex.queries import (
    load_customers,
    load_orders_customers,
    load_statistics,
)


class State(rx.State):
    """The app state."""

    customers_data: list[CustomerData] = []
    orders_customers_data: list[OrderCustomerData] = []
    statistics_data: StatisticsData | None = None
    loading_customers: bool = False
    loading_orders: bool = False
    loading_statistics: bool = False

    @rx.var
    def has_customers_data(self) -> bool:
        """Check if customers data is loaded."""
        return len(self.customers_data) > 0

    @rx.var
    def has_orders_data(self) -> bool:
        """Check if orders data is loaded."""
        return len(self.orders_customers_data) > 0

    @rx.var
    def has_statistics_data(self) -> bool:
        """Check if statistics data is loaded."""
        return self.statistics_data is not None

    @rx.var
    def total_customers(self) -> int:
        """Get total customers count."""
        return self.statistics_data["total_customers"] if self.statistics_data else 0

    @rx.var
    def total_orders(self) -> int:
        """Get total orders count."""

        return self.statistics_data["total_orders"] if self.statistics_data else 0

    @rx.var
    def avg_freight_value(self) -> str:
        """Get average freight as formatted string."""
        if self.statistics_data and self.statistics_data["avg_freight"] is not None:
            return f"${self.statistics_data['avg_freight']:.2f}"
        return "N/A"

    @rx.var
    def orders_by_country_list(self) -> list[dict[str, int | str]]:
        """Get orders by country as list of dicts for charts."""
        if not self.statistics_data:
            return []
        return [
            {"country": country, "orders": count}
            for country, count in self.statistics_data["orders_by_country"].items()
        ]

    @rx.var
    def customers_by_country_list(self) -> list[dict[str, int | str]]:
        """Get customers by country as list of dicts for charts."""
        if not self.statistics_data:
            return []
        return [
            {"country": country, "customers": count}
            for country, count in self.statistics_data["customers_by_country"].items()
        ]

    @rx.event
    def load_customers(self):
        """Load customers data from database."""
        self.loading_customers = True
        self.customers_data = load_customers()
        self.loading_customers = False

    @rx.event
    def load_orders_customers(self):
        """Load orders and customers join data from database."""
        self.loading_orders = True
        self.orders_customers_data = load_orders_customers()
        self.loading_orders = False

    @rx.event
    def load_statistics(self):
        """Load statistics data from database."""
        self.loading_statistics = True
        self.statistics_data = load_statistics()
        self.loading_statistics = False
