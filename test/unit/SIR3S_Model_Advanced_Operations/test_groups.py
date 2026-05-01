from types import SimpleNamespace


class DummyObjectTypes:
    LAYR_Layer = "LAYR_Layer"
    Node = "Node"
    Pipe = "Pipe"

    def __getitem__(self, key):
        return getattr(self, key)


def _attach_group_state_stubs(instance, group_store, object_type_tks):
    instance.ObjectTypes = DummyObjectTypes()

    def _get_tks_of_element_type(element_type):
        return object_type_tks.get(element_type, [])

    def _get_value(tk, key):
        if key != "ObjsString":
            raise KeyError(key)
        return [group_store[tk]]

    def _set_value(tk, key, value):
        if key != "ObjsString":
            raise KeyError(key)
        group_store[tk] = value

    instance.GetTksofElementType = _get_tks_of_element_type
    instance.GetValue = _get_value
    instance.SetValue = _set_value


def test_get_tks_of_group_elements_parses_objs_string(s3s_model_advanced_operations_instance):
    group_store = {
        100: "KNOT~1\tROHR~2\t",
    }
    object_type_tks = {
        "LAYR_Layer": [100],
        "Node": ["1"],
        "Pipe": ["2"],
    }
    _attach_group_state_stubs(s3s_model_advanced_operations_instance, group_store, object_type_tks)

    result = s3s_model_advanced_operations_instance.get_tks_of_group_elements(100)

    assert result == [("KNOT", "1"), ("ROHR", "2")]


def test_remove_elements_from_group_removes_only_matching_existing_tks(s3s_model_advanced_operations_instance):
    group_store = {
        100: "KNOT~1\tROHR~2\tKNOT~3\t",
    }
    object_type_tks = {
        "LAYR_Layer": [100],
        "Node": ["1", "3", "4"],
        "Pipe": ["2"],
    }
    _attach_group_state_stubs(s3s_model_advanced_operations_instance, group_store, object_type_tks)

    s3s_model_advanced_operations_instance.remove_elements_from_group(
        group_tk=100,
        element_tks=[("KNOT", "3"), ("KNOT", "4")],
    )

    result = s3s_model_advanced_operations_instance.get_tks_of_group_elements(100)

    assert result == [("KNOT", "1"), ("ROHR", "2")]


def test_add_elements_to_group_adds_only_missing_existing_tks(s3s_model_advanced_operations_instance):
    group_store = {
        100: "KNOT~1\tROHR~2\t",
    }
    object_type_tks = {
        "LAYR_Layer": [100],
        "Node": ["1", "3"],
        "Pipe": ["2"],
    }
    _attach_group_state_stubs(s3s_model_advanced_operations_instance, group_store, object_type_tks)

    s3s_model_advanced_operations_instance.add_elements_to_group(
        group_tk=100,
        element_tks=[("KNOT", "1"), ("KNOT", "3")],
    )

    result = s3s_model_advanced_operations_instance.get_tks_of_group_elements(100)

    assert result == [("KNOT", "1"), ("ROHR", "2"), ("KNOT", "3")]


def test_set_group_elements_overwrites_group_content_with_valid_tks(s3s_model_advanced_operations_instance):
    group_store = {
        100: "KNOT~1\tROHR~2\t",
    }
    object_type_tks = {
        "LAYR_Layer": [100],
        "Node": ["1", "3"],
        "Pipe": ["2"],
    }
    _attach_group_state_stubs(s3s_model_advanced_operations_instance, group_store, object_type_tks)

    s3s_model_advanced_operations_instance.set_group_elements(
        group_tk=100,
        element_tks=[("KNOT", "3"), ("KNOT", "999999")],
    )

    result = s3s_model_advanced_operations_instance.get_tks_of_group_elements(100)

    assert result == [("KNOT", "3")]


def test_add_element_types_to_tk_list_maps_tks_to_group_codes(s3s_model_advanced_operations_instance):
    group_store = {100: ""}
    object_type_tks = {
        "LAYR_Layer": [100],
        "Node": ["1"],
        "Pipe": ["2"],
    }
    _attach_group_state_stubs(s3s_model_advanced_operations_instance, group_store, object_type_tks)

    result = s3s_model_advanced_operations_instance.add_element_types_to_tk_list(["1", "2"])

    assert result == [("KNOT", "1"), ("ROHR", "2")]


def test_add_elements_to_group_does_not_validate_element_type_matches_tk(s3s_model_advanced_operations_instance):
    group_store = {
        100: "",
    }
    object_type_tks = {
        "LAYR_Layer": [100],
        "Node": ["1"],
        "Pipe": [],
    }
    _attach_group_state_stubs(s3s_model_advanced_operations_instance, group_store, object_type_tks)

    s3s_model_advanced_operations_instance.add_elements_to_group(
        group_tk=100,
        element_tks=[("ROHR", "1")],
    )

    result = s3s_model_advanced_operations_instance.get_tks_of_group_elements(100)

    assert result == [("ROHR", "1")]
