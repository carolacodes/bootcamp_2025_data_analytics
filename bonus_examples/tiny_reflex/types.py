"""Type definitions for data structures used in the application."""

from typing import TypedDict


class CustomerData(TypedDict):
    """Type definition for customer data from database."""

    customer_id: str
    company_name: str
    contact_name: str | None
    contact_title: str | None
    address: str | None
    city: str | None
    region: str | None
    postal_code: str | None
    country: str | None
    phone: str | None
    fax: str | None


class OrderCustomerData(TypedDict):
    """Type definition for orders and customers join data from database."""

    order_id: int
    order_date: str | None
    ship_name: str | None
    ship_city: str | None
    ship_country: str | None
    freight: float | None
    customer_id: str
    company_name: str
    contact_name: str | None
    customer_country: str | None


class StatisticsData(TypedDict):
    """Type definition for statistics data."""

    total_customers: int
    total_orders: int
    avg_freight: float | None
    orders_by_country: dict[str, int]
    customers_by_country: dict[str, int]
