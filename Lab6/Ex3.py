def determine_progress1(hits, spins):
    if spins == 0:
        return "Get going!"
    
    hits_spins_ratio = hits / spins

    if hits_spins_ratio > 0:
        progress = "On your way!"
        if hits_spins_ratio >= 0.25:
            progress = "Almost there!"
            if hits_spins_ratio >= 0.5:
                if hits < spins:
                    progress = "You win!"
    else:
        progress = "Get going!"

    return progress

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



def determine_progress3(hits, spins):
    if spins == 0:
        return "Get going!"

    ratio = hits / spins

    if ratio <= 0:
        return "Get going!"
    elif ratio < 0.25:
        return "On your way!"
    elif ratio < 0.5:
        return "Almost there!"
    else:
        if hits < spins:
            return "You win!"
        return "Almost there!"

test_determine_progress(determine_progress3)

def determine_progress_no_if(hits, spins):
    messages = ["Get going!", "On your way!", "Almost there!", "You win!"]
    
    denom = spins if spins != 0 else 1
    ratio = hits / denom
    spins_nonzero = int(spins != 0)

    level = 0
    level += spins_nonzero * int(ratio > 0)
    level += spins_nonzero * int(ratio >= 0.25)
    level += spins_nonzero * int(ratio >= 0.5)
    level = level - (int(level == 3) * int(not (hits < spins)))

    return messages[level]

test_determine_progress(determine_progress_no_if)
