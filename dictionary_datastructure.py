def generate_dict():
    brm_dict = {
        # from BrM Work Candidates
        'Work Items Description': [[], []],
        'Work Items Action': [[], []],
        'Work Items Priority': [[], []],
        'Work Items Responsibility': [[], []],
        # from BrM Condition Page
        'Structure ID': [[1, 2], ''],
        'Date': [[4, 2], ''],
        'Route #': [[7, 2], ''],
        'Bridge/Culvert': [[14, 2], ''],
        'B.C.01 (Deck) (Item 58)': [[25, 2], ''],
        'B.C.02 (Superstructure) (Item 59)': [[28, 2], ''],
        'B.C.03 (Substructure) (Item 60)': [[31, 2], ''],
        'B.C.04 (Culverts) (Item 62)': [[34, 2], ''],
        'B.C.09 (Channel) (Item 61)': [[49, 2], ''],
        #'B.AP.02 (Overtopping Likelihood) (Item 71 - Waterway Adequacy)': [[55, 2], ''],
        'Scour Observed': [[20, 5], ''],
        'No of Spans': [[15, 2], ''],
        #'Required Posting': [[9, 5], ''],
        'Posting Values': [[[12, 5], [13, 5], [14, 5], [15, 5], [16, 5], [17, 5], [18, 5], [19, 5]], []],
        'Inspection Type': [[5, 2], ''],
        'Inspection Frequency': [[5, 3], ''],
        'Elements': [[], []],
        'Total Quantity': [[], []],
        'CS1': [[], []],
        'CS2': [[], []],
        'CS3': [[], []],
        'CS4': [[], []],
        'Description': [[], []],
    }

    return brm_dict