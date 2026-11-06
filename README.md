# Warehouse tools

Small Python utilities for warehouse order and shipping workflows.

Run the tests with `python3 -m unittest discover -s tests -v`.

## Shipping

`shipping_quote(weight_kg, zone, service="standard")` returns a delivery quote
in US dollars.

| Parameter   | Values                      | Notes                     |
|-------------|-----------------------------|---------------------------|
| `weight_kg` | positive float              | Parcel weight in kilograms |
| `zone`      | `"local"`, `"regional"`     | Delivery zone             |
| `service`   | `"standard"`, `"express"`   | Default: `"standard"`     |

Express shipping carries a flat **$7.00 surcharge** on top of the standard rate.

### Rates

| Zone       | Base (standard) | Base (express) |
|------------|-----------------|----------------|
| local      | $5.00           | $12.00         |
| regional   | $8.00           | $15.00         |

Plus **$1.50 × weight_kg** for both services.

### CLI

```
python -m warehouse.cli <weight_kg> <zone> [--service {standard,express}]
```

Examples:

```bash
# Standard quote – 3 kg, local zone → $9.50
python -m warehouse.cli 3 local

# Express quote – 3 kg, local zone → $16.50
python -m warehouse.cli 3 local --service express
```
