from ITM352_S26.Lab6.Ex2 import determine_progress1


def test_determine_progress(progress_function):
    """Test all possible return values of the determine_progress function.
   
    This test function validates all distinct code paths and return values:
    - "Get going!" when spins = 0 or hits = 0
    - "On your way!" when 0 < hits/spins < 0.25
    - "Almost there!" when 0.25 <= hits/spins < 0.5
    - "You win!" when hits/spins >= 0.5 AND hits < spins
    - "Almost there!" when hits/spins >= 0.5 AND hits >= spins (edge case)
    - "Almost there!" = when ratio >= 0.5 but hits >= spins 
    """
   
    # Test case 1: spins = 0 returns "Get going!"
    assert progress_function(10, 0) == "Get going!", "Test case 1 failed: spins=0"
    # Test case 2: hits = 0 returns "Get going!"
    assert progress_function(0, 10) == "Get going!", "Test case 2 failed: hits=0"
   
    # Test case 3: 0 < ratio < 0.25 returns "On your way!"
    # hits=1, spins=5 gives ratio=0.2
    assert progress_function(1, 5) == "On your way!", "Test case 3 failed: ratio < 0.25"
   
    # Test case 4: 0.25 <= ratio < 0.5 returns "Almost there!"
    # hits=1, spins=3 gives ratio≈0.333
    assert progress_function(1, 3) == "Almost there!", "Test case 4 failed: 0.25 <= ratio < 0.5"
   
    # Test case 5: ratio >= 0.5 AND hits < spins returns "You win!"
    # hits=6, spins=10 gives ratio=0.6
    assert progress_function(6, 10) == "You win!", "Test case 5 failed: ratio >= 0.5 and hits < spins"
   
    # Test case 6: ratio >= 0.5 AND hits >= spins returns "Almost there!"
    # hits=10, spins=10 gives ratio=1.0, but hits is not < spins
    assert progress_function(10, 10) == "Almost there!", "Test case 6 failed: ratio >= 0.5 but hits >= spins"
   
    print("All tests passed!")




# Test the function
if __name__ == "__main__":
    test_determine_progress(determine_progress1) 
