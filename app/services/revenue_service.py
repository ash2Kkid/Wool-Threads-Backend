from app.database.revenue_db import get_farmer_revenues
from datetime import datetime
from datetime import datetime



def fetch_farmer_revenue(farmer_id: str):
    revenues = get_farmer_revenues(farmer_id)

    total_paid = 0
    total_pending = 0
    total_profit = 0
    total_loss = 0

    monthly = {}
    yearly = {}

    for r in revenues:
        amount = r["amount"]

        # ✅ Expected benchmark
        expected = r.get("expected_market_price", amount)

        profit_value = amount - expected

        if profit_value >= 0:
            total_profit += profit_value
        else:
            total_loss += abs(profit_value)

        # ✅ Paid vs pending totals
        if r["status"] == "paid":
            total_paid += amount
        else:
            total_pending += amount

        # ✅ Date breakdown
        created_str = r.get("created_at")

        # ✅ If missing, treat it as "today"
        if not created_str:
            created = datetime.utcnow()
        else:
            created = datetime.fromisoformat(created_str)
        month_key = created.strftime("%Y-%m")
        year_key = created.strftime("%Y")

        monthly[month_key] = monthly.get(month_key, 0) + profit_value
        yearly[year_key] = yearly.get(year_key, 0) + profit_value

    return {
        "total_paid": total_paid,
        "total_pending": total_pending,
        "total_profit": total_profit,
        "total_loss": total_loss,
        "monthly_profit": monthly,
        "yearly_profit": yearly,
        "transactions": revenues
    }