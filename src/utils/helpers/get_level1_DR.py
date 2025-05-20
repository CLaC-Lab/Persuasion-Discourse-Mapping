def get_level1_DR(level2_relation):
    """
    Returns the corresponding level-1 discourse relation (DR) for a given level-2 DR.

    Args:
        level2_relation (str): The name of the level-2 discourse relation.

    Returns:
        str or None: Corresponding level-1 DR if found; otherwise, None.
    """

    # Define a dictionary that maps level-2 relations to their level-1 equivalents
    level2_to_level1 = {
        # Temporal
        "synchronous": "temporal",
        "asynchronous": "temporal",

        # Contingency
        "cause": "contingency",
        "cause+belief": "contingency",
        "cause+speechact": "contingency",
        "condition": "contingency",
        "condition+speechact": "contingency",
        "negative-condition": "contingency",
        "negative-condition+speechact": "contingency",
        "purpose": "contingency",

        # Comparison
        "concession": "comparison",
        "concession+speechact": "comparison",
        "contrast": "comparison",
        "similarity": "comparison",

        # Expansion
        "conjunction": "expansion",
        "disjunction": "expansion",
        "equivalence": "expansion",
        "exception": "expansion",
        "instantiation": "expansion",
        "level-of-detail": "expansion",
        "manner": "expansion",
        "substitution": "expansion"
    }

    return level2_to_level1.get(level2_relation.lower(), None)