def check_prefix_suffix(string, prefix=None, suffix=None):
    starts_with_prefix = False
    ends_with_suffix = False
    
    if prefix is not None:
        starts_with_prefix = string.startswith(prefix)
        
    if suffix is not None:
        ends_with_suffix = string.endswith(suffix)
        
    return starts_with_prefix, ends_with_suffix

# Example usage:
test_string = "HelloWorld"
prefix_to_check = "Hello"
suffix_to_check = "World"

# Check if the string starts with the prefix
starts_with_prefix, ends_with_suffix = check_prefix_suffix(test_string, prefix_to_check, suffix_to_check)

if starts_with_prefix:
    print(f"The string '{test_string}' starts with '{prefix_to_check}'.")
else:
    print(f"The string '{test_string}' does not start with '{prefix_to_check}'.")

if ends_with_suffix:
    print(f"The string '{test_string}' ends with '{suffix_to_check}'.")
else:
    print(f"The string '{test_string}' does not end with '{suffix_to_check}'.")
