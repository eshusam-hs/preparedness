import argparse
import json
import os

def validate_leaf_rubric_and_weight(rubric_tree: dict) -> bool:

    category = rubric_tree.get("task_category")
    assert "requirements" in rubric_tree and isinstance(rubric_tree["requirements"], str)
    assert "weight" in rubric_tree and (isinstance(rubric_tree["weight"], float) or isinstance(rubric_tree["weight"], int))
    if not rubric_tree["sub_tasks"]:
        assert category is not None
    if not rubric_tree["sub_tasks"]:
        return True

    for node in rubric_tree["sub_tasks"]:
        result = validate_leaf_rubric_and_weight(node)
        assert result
    return True




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process a rubric file.")
    parser.add_argument("-f", "--file", type=str, required=True, help="The rubric file to process")
    args = parser.parse_args()

    rubric_file = args.file
    if "rubric.json" not in rubric_file:
        rubric_file = os.path.join(rubric_file, "rubric.json")

    print(f"Processing file: {rubric_file}")
    with open(rubric_file) as f:
        rubric_dict = json.load(f)
    pass_validate = validate_leaf_rubric_and_weight(rubric_dict)
    assert pass_validate
    print("Pass!")
