"""
converter.py
------------

Command‑line utility to convert distances between miles and kilometres.
Illustrates:
  • constants
  • simple functions
  • CLI I/O
  • basic error handling
  • sanity assertions

Run directly for interactive use,
or import the two conversion functions elsewhere.
"""


KM_PER_MILE = 1.60934

# ---- Reusable functions ------------

def miles_to_km(miles: float) -> float:   # Defines the variable for converting miles to km
    """Return kilometers equivalent of *miles*."""
    return miles * KM_PER_MILE

def km_to_miles(km: float) -> float:    # Defines the variable for converting km to miles
    """Return miles equivalent of *km*."""
    return km / KM_PER_MILE

#---- CLI wrapper ----------------

def main() -> None:
    """Interactive command-line interface."""
    choice = input("Convert (1) miles→km or (2) km→miles? ") # First choice

    try:
        value = float(input("Enter the distance: ")) # Input validation step. Needs numeric for distance
    except ValueError:
        print("Distance must be numeric.")
        return

    if choice == "1":
        result = miles_to_km(value)
        unit_in, unit_out = "mi", "km"
    elif choice == "2":
        result = km_to_miles(value)
        unit_in, unit_out = "km", "mi"
    else:
        print("Invalid choice.")
        return

    print(f"{value:.2f} {unit_in} = {result:.2f} {unit_out}")
    # end of main()

# ---- sanity assertions ----------------------------------
assert abs(miles_to_km(1) - 1.60934) < 1e-6
assert abs(km_to_miles(1.60934) - 1) < 1e-6

# ---- script‑vs‑module guard -----------------------------
if __name__ == "__main__":
    main()