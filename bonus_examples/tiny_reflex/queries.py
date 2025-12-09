"""Database query functions."""

import pandas as pd
from typing import cast
from tiny_reflex.db_connection import get_engine
from tiny_reflex.types import CustomerData, OrderCustomerData, StatisticsData


def load_customers() -> list[CustomerData]:
    """Load customers data from database."""
    try:
        engine = get_engine()
        query = "SELECT * FROM customers ORDER BY customer_id LIMIT 100"
        df = pd.read_sql(query, engine)
        records = df.to_dict("records")
        return cast(list[CustomerData], records)
    except Exception as e:
        print(f"Error loading customers: {e}")
        return []


def load_orders_customers() -> list[OrderCustomerData]:
    """Load orders and customers join data from database."""
    try:
        engine = get_engine()
        query = """
            SELECT 
                o.order_id,
                o.order_date,
                o.ship_name,
                o.ship_city,
                o.ship_country,
                o.freight,
                c.customer_id,
                c.company_name,
                c.contact_name,
                c.country as customer_country
            FROM orders o
            INNER JOIN customers c ON o.customer_id = c.customer_id
            ORDER BY o.order_date DESC
            LIMIT 100
        """
        df = pd.read_sql(query, engine)
        records = df.to_dict("records")
        return cast(list[OrderCustomerData], records)
    except Exception as e:
        print(f"Error loading orders and customers: {e}")
        return []


def load_statistics() -> StatisticsData:
    """Load statistics data from database."""
    try:
        engine = get_engine()
        
        # Total customers
        customers_query = "SELECT COUNT(*) as count FROM customers"
        customers_df = pd.read_sql(customers_query, engine)
        total_customers = int(customers_df.iloc[0]["count"])
        
        # Total orders
        orders_query = "SELECT COUNT(*) as count FROM orders"
        orders_df = pd.read_sql(orders_query, engine)
        total_orders = int(orders_df.iloc[0]["count"])
        
        # Average freight
        freight_query = "SELECT AVG(freight) as avg_freight FROM orders WHERE freight IS NOT NULL"
        freight_df = pd.read_sql(freight_query, engine)
        avg_freight = float(freight_df.iloc[0]["avg_freight"]) if freight_df.iloc[0]["avg_freight"] is not None else None
        
        # Orders by country
        orders_by_country_query = """
            SELECT ship_country, COUNT(*) as count 
            FROM orders 
            WHERE ship_country IS NOT NULL
            GROUP BY ship_country 
            ORDER BY count DESC
            LIMIT 10
        """
        orders_by_country_df = pd.read_sql(orders_by_country_query, engine)
        orders_by_country = dict(zip(orders_by_country_df["ship_country"], orders_by_country_df["count"]))
        
        # Customers by country
        customers_by_country_query = """
            SELECT country, COUNT(*) as count 
            FROM customers 
            WHERE country IS NOT NULL
            GROUP BY country 
            ORDER BY count DESC
            LIMIT 10
        """
        customers_by_country_df = pd.read_sql(customers_by_country_query, engine)
        customers_by_country = dict(zip(customers_by_country_df["country"], customers_by_country_df["count"]))
        
        return StatisticsData(
            total_customers=total_customers,
            total_orders=total_orders,
            avg_freight=avg_freight,
            orders_by_country=orders_by_country,
            customers_by_country=customers_by_country,
        )
    except Exception as e:
        print(f"Error loading statistics: {e}")
        return StatisticsData(
            total_customers=0,
            total_orders=0,
            avg_freight=None,
            orders_by_country={},
            customers_by_country={},
        )
