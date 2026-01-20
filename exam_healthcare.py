def sort(width, height, length, mass):
    """
    Sort packages into STANDARD, SPECIAL, or REJECTED stacks based on dimensions and mass.
    
    Args:
        width (float): Package width in centimeters
        height (float): Package height in centimeters
        length (float): Package length in centimeters
        mass (float): Package mass in kilograms
    
    Returns:
        str: Stack name - "STANDARD", "SPECIAL", or "REJECTED"
    """
    # Calculate volume
    volume = width * height * length
    
    # Check if package is bulky (using ternary operator as required)
    is_bulky = True if (volume >= 1_000_000 or max(width, height, length) >= 150) else False
    
    # Check if package is heavy (using ternary operator)
    is_heavy = True if mass >= 20 else False
    
    # Determine the appropriate stack using ternary operators
    return "REJECTED" if (is_bulky and is_heavy) else ("SPECIAL" if (is_bulky or is_heavy) else "STANDARD")


# Test cases
def test_sort():
    """Comprehensive test suite for the sort function."""
    
    # Test STANDARD packages
    assert sort(10, 10, 10, 5) == "STANDARD", "Small, light package should be STANDARD"
    assert sort(50, 50, 50, 10) == "STANDARD", "Medium package under thresholds should be STANDARD"
    assert sort(149, 10, 10, 19.9) == "STANDARD", "Just under bulky/heavy thresholds should be STANDARD"
    
    # Test SPECIAL packages - bulky only
    assert sort(150, 10, 10, 5) == "SPECIAL", "Package with one dimension >= 150 should be SPECIAL"
    assert sort(10, 150, 10, 5) == "SPECIAL", "Package with height >= 150 should be SPECIAL"
    assert sort(10, 10, 150, 5) == "SPECIAL", "Package with length >= 150 should be SPECIAL"
    assert sort(100, 100, 100, 5) == "SPECIAL", "Package with volume >= 1,000,000 should be SPECIAL"
    assert sort(101, 99, 100, 10) == "STANDARD", "Package with volume 999,900 (under threshold) should be STANDARD"
    
    # Test SPECIAL packages - heavy only
    assert sort(10, 10, 10, 20) == "SPECIAL", "Heavy package (mass >= 20) should be SPECIAL"
    assert sort(50, 50, 50, 25) == "SPECIAL", "Heavy package under bulky thresholds should be SPECIAL"
    
    # Test REJECTED packages - both bulky and heavy
    assert sort(150, 10, 10, 20) == "REJECTED", "Bulky and heavy package should be REJECTED"
    assert sort(100, 100, 100, 20) == "REJECTED", "High volume and heavy should be REJECTED"
    assert sort(200, 200, 200, 50) == "REJECTED", "Very large and heavy should be REJECTED"
    
    # Edge cases
    assert sort(0, 0, 0, 0) == "STANDARD", "Zero dimensions should be STANDARD"
    assert sort(149, 10, 10, 19.9) == "STANDARD", "Just below all thresholds should be STANDARD"
    assert sort(150, 150, 150, 20) == "REJECTED", "Exactly at both thresholds should be REJECTED"
    
    # Boundary testing for volume calculation
    assert sort(100, 100, 99.99, 10) == "STANDARD", "Volume just under 1,000,000 should be STANDARD"
    assert sort(100, 100, 100.01, 10) == "SPECIAL", "Volume just over 1,000,000 should be SPECIAL"
    
    print("All tests passed! ✅")


if __name__ == "__main__":
    # Run tests
    test_sort()
    
    # Example usage
    print("\nExample outputs:")
    print(f"sort(50, 50, 50, 10) = {sort(50, 50, 50, 10)}")  # STANDARD
    print(f"sort(150, 50, 50, 10) = {sort(150, 50, 50, 10)}")  # SPECIAL (bulky)
    print(f"sort(50, 50, 50, 20) = {sort(50, 50, 50, 20)}")  # SPECIAL (heavy)
    print(f"sort(150, 50, 50, 20) = {sort(150, 50, 50, 20)}")  # REJECTED (both)