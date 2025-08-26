from template import Template

# Test case handler
test_case = input()

if test_case == "basic_test":
    # TODO: Create a Template object with name "Test Name"
    # TODO: Call the display_info() method on the object
    t1 = Template("Test Name")
    t1.display_info()

elif test_case == "validation_test":
    # TODO: Create a Template object with name "Validation Test"
    # TODO: Print the name using the name property in format: "Name: {obj.name}"
    t2 = Template("Validation Test")
    print(f"Name: {t2.name}")
