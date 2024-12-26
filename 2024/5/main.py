from collections import deque, defaultdict


def earlier_page(rule):
    return rule.split('|')[0]


def later_page(rule):
    return rule.split('|')[1]


def read_input():
    rules = []
    safety_manuals = []
    input_file = 'input.txt'
    with open(input_file, 'r') as f:
        [rules.append(line.strip()) for line in f if '|' in line]
    with open(input_file, 'r') as f:
        for line in f:
            if ',' in line:
                safety_manuals.append(line.strip().split(','))

    return rules, safety_manuals


def build_graph(pages, relevant_rules):
    """
    Builds a graph (adjacency list) and in-degree map from the given pages and rules.
    Nodes are page numbers, edges represent ordering constraints.
    """
    graph = {page: [] for page in pages}
    in_degree = {page: 0 for page in pages}

    for rule in relevant_rules:
        ep, lp = rule.split('|')
        # Add edge ep -> lp if both are in this manual
        if ep in pages and lp in pages:
            graph[ep].append(lp)
            in_degree[lp] += 1

    return in_degree


def custom_sort(pages, relevant_rules):
    in_degree = build_graph(pages, relevant_rules)

    sorted_order = []
    for locator in range(len(pages)):
        for page in pages:
            if in_degree.get(page) == locator:
                sorted_order.append(page)
    return sorted_order


def main():
    rules, safety_manuals = read_input()

    valid_safety_manuals = []
    incorrectly_ordered_manuals = []
    middle_pages = []
    corrected_manuals = []

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
            incorrectly_ordered_manuals.append(safety_manual)
            corrected_manuals.append(custom_sort(safety_manual, relevant_rules))
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

    corrected_middle_pages = []

    # sum all the middle page numbers
    print(f'The total sum of middle pages is: {sum(list(map(int, middle_pages)))}')
    for safety_manual in corrected_manuals:
        if len(safety_manual) % 2 == 0:
            print(f'ERROR: The following manual has an even number of pages and the middle page is ambiguous: {safety_manual}')
            continue
        else:
            corrected_middle_pages.append(safety_manual[len(safety_manual)//2])

    print(f'The total sum of the corrected sort order middle pages is: {sum(list(map(int, corrected_middle_pages)))}')


if __name__ == '__main__':
    main()



# Let's break down what the graph and in_degree represent based on the given data:
#
# Your Provided Graph:
#
# graph = {
#   '47': ['53', '61'],
#   '53': [],
#   '61': ['53'],
#   '75': ['53', '47', '61'],
#   '97': ['61', '47', '53', '75']
# }
#
# This means:
#
#     From page 47, we have edges to pages 53 and 61. ("47 must come before 53 and 61")
#     From page 53, there are no outgoing edges. (No pages depend on 53)
#     From page 61, we have an edge to page 53. ("61 must come before 53")
#     From page 75, we have edges to pages 53, 47, and 61. ("75 must come before 53, 47, and 61")
#     From page 97, we have edges to pages 61, 47, 53, and 75. ("97 must come before 61, 47, 53, and 75")
#
# Counting In-Degrees: The in_degree of a node is the number of edges coming into it. Let's count them:
#
#     For '53':
#         It has an incoming edge from '47' (47->53)
#         It has an incoming edge from '61' (61->53)
#         It has an incoming edge from '75' (75->53)
#         It has an incoming edge from '97' (97->53)
#
#     Total incoming edges for '53': 4
#
#     For '61':
#         Incoming from '47' (47->61)
#         Incoming from '75' (75->61)
#         Incoming from '97' (97->61)
#
#     Total incoming edges for '61': 3
#
#     For '47':
#         Incoming from '75' (75->47)
#         Incoming from '97' (97->47)
#
#     Total incoming edges for '47': 2
#
#     For '75':
#         Incoming from '97' (97->75)
#
#     Total incoming edges for '75': 1
#
#     For '97':
#         No pages lead into '97', so it has no incoming edges.
#
#     Total incoming edges for '97': 0
#
# So the in_degree you provided:
#
# in_degree = {
#   '47': 2,
#   '53': 4,
#   '61': 3,
#   '75': 1,
#   '97': 0
# }
#
# is actually correct given the graph.
#
# Why is it not what you expected?
# If you thought '53' should have 0 and '97' should have 4, it suggests you might have misunderstood the direction of the edges. The rules state "X|Y means X must be printed before Y". This means the edge is from X to Y (X->Y), which would increase Y's in-degree, not X's.
#
# Since '97' appears to be a prerequisite for many pages (it points to a lot of them), it will have an in_degree of 0 because nothing needs to come before it. On the other hand, '53' appears after multiple other pages, so it ends up with a high in_degree (4), because you have four rules placing other pages before '53'.
#
# In Conclusion:
# The in_degree you've derived is correct based on the standard interpretation of the rules and the direction of edges. If you expected the opposite, double-check the direction of the edges you intended to create from the rules.
