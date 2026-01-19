# Calc_Adf
Advanced calculator that contains very interesting things - will update soon

# this is a concept of the folder structure will add changes as new updates are added #

```
smart_calculator/
│
├── app.py                     # Main Python entry point (Flask backend)
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
│
├── config/
│   ├── __init__.py
│   ├── settings.py            # App settings, API keys, constants
│   └── database.py            # Database connection setup
│
├── database/
│   ├── calculator.db          # SQLite database (history, logs)
│   └── schema.sql             # Table definitions
│
├── api/
│   ├── __init__.py
│   ├── currency_api.py        # Currency conversion (external API)
│   └── graph_api.py           # Graph plotting endpoints
│
├── core/
│   ├── __init__.py
│   │
│   ├── calculator/
│   │   ├── __init__.py
│   │   ├── basic_ops.py       # +, -, *, /, modulus
│   │   ├── bodmas.py          # Expression evaluation
│   │   ├── trig.py            # sin, cos, tan, inverse
│   │   ├── logarithmic.py     # log, ln
│   │   ├── exponential.py    # e^x operations
│   │   ├── fractions.py       # Fraction calculations
│   │   ├── symbolic.py        # Symbolic math (sympy)
│   │   ├── matrix.py          # Matrix operations
│   │   └── history.py         # Calculator history logic
│   │
│   └── converters/
│       ├── __init__.py
│       ├── currency.py        # Currency converter
│       ├── length.py          # Length conversions
│       ├── mass.py            # Mass conversions
│       ├── area.py            # Area conversions
│       ├── time.py            # Time conversions
│       ├── volume.py          # Volume conversions
│       ├── speed.py           # Speed conversions
│       ├── temperature.py     # Temperature conversions
│       ├── discount.py        # Discount calculator
│       ├── bmi.py             # BMI calculator
│       ├── gst.py             # GST calculator
│       └── emi.py             # EMI calculator
│
├── static/
│   ├── css/
│   │   └── style.css          # Global styles
│   │
│   ├── js/
│   │   ├── calculator.js      # Calculator frontend logic
│   │   ├── converters.js      # Converter frontend logic
│   │   ├── graph.js           # Graph plotting (Chart.js / Plotly)
│   │   └── history.js         # History handling
│   │
│   └── assets/
│       └── images/            # Icons, images
│
├── templates/
│   ├── base.html              # Base layout
│   ├── index.html             # Removed
│   ├── calculator.html        # Calculator UI
│   ├── converters.html        # Converter UI
│   └── graph.html             # Graph visualization page
│
└── tests/
    ├── test_calculator.py     # Calculator unit tests
    ├── test_converters.py     # Converter unit tests
    └── test_api.py            # API testing
```
