# This entrypoint file to be used in development. Start by reading README.md
from unittest import main
from arithmetic_arranger import arithmetic_arranger

# print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]))
# arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49"], True)

# Run unit tests automatically
main(module='test_module', exit=False)
