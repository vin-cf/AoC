
def earlier_page(rule):
    return rule.split('|')[0]


def later_page(rule):
    return rule.split('|')[1]


def read_input():
    rules = []
    safety_manuals = []
    with open('input.txt', 'r') as f:
        [rules.append(line.strip()) for line in f if '|' in line]
    with open('input.txt', 'r') as f:
        for line in f:
            if ',' in line:
                safety_manuals.append(line.strip().split(','))

    return rules, safety_manuals


def main():
    rules, safety_manuals = read_input()

    valid_safety_manuals = []
    middle_pages = []
    # for each safety manual, filter out the relevant rules
    for safety_manual in safety_manuals:
        relevant_rules = []
        for rule in rules:
            if (earlier_page(rule) in safety_manual) and (later_page(rule) in safety_manual):
                # a relevant rule contains a number from the safety manual in both the earlier and later page where
                # rules are expressed in the format rule: earlier_page | later_page
                relevant_rules.append(rule)
        # print(f'DEBUG: The following rules are applicable for safety manual {safety_manual}: {relevant_rules}')

        # from the relevant rules, determine if the safety manual meets the requirement
        # As a result, capture 'valid' safety manuals
        if False in [safety_manual.index(later_page(rule)) > safety_manual.index(earlier_page(rule)) for rule in relevant_rules]:
            continue
        else:
            valid_safety_manuals.append(safety_manual)

    print(f'DEBUG: The following safety rules are valid: {valid_safety_manuals}')

    # From the collated list of valid safety manuals, return the middle page number
    for safety_manual in valid_safety_manuals:
        if len(safety_manual) % 2 == 0:
            print(f'ERROR: The following manual has an even number of pages and the middle page is ambiguous: {safety_manual}')
            continue
        else:
            middle_pages.append(safety_manual[len(safety_manual)//2])

    # sum all the middle page numbers
    print(f'The total sum of middle pages is: {sum(list(map(int, middle_pages)))}')


if __name__ == '__main__':
    main()
