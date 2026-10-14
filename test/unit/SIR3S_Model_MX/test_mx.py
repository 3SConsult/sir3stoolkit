"""Unit tests for the internal MX result-file reading (sir3stoolkit.mantle.mx.SIR3S_Model_MX) on small
synthetic .MX1/.MX2/.MXS files (no SIR 3S needed)."""
import os
import struct

import numpy as np
import pandas as pd
import pytest

from sir3stoolkit.mantle.mx import SIR3S_Model_MX

TKS = ["1001", "1002", "1003"]
N_OF_POINTS = [2, 3, 1]
CVERSO = "SIR 3S 90-15-02-46 3S Consult, 30827 Garbsen - 04.09.2026 14:31 - M-1-0-1"
SNAPSHOTS = [
    ("STAT", "2023-02-12 23:00:00.000000+00:00"),
    ("TIME", "2023-02-12 23:00:00.000000+00:00"),
    ("TIME", "2023-02-13 00:00:00.000000+00:00"),
    ("TIME", "2023-02-13 01:00:00.000000+00:00"),
    ("TMIN", "2023-02-13 01:00:00.000000+00:00"),
    ("TMAX", "2023-02-13 01:00:00.000000+00:00"),
]


def _channels():
    """(OBJTYPE, NAME1, NAME2, OBJTYPE_PK, ATTRTYPE, DATATYPE, DATALENGTH, DATATYPELENGTH)"""
    n, n_pts = len(TKS), sum(N_OF_POINTS)
    return [
        ("ALLG", "", "", "42", "TIMESTAMP", "CHAR", 32, 32),
        ("ALLG", "", "", "42", "SNAPSHOTTYPE", "CHAR", 4, 4),
        ("ALLG", "", "", "42", "CVERSO", "CHAR", 80, 80),
        ("ROHR", "*", "*", "*", "QMAV", "REAL", 4 * n, 4),
        ("ROHR", "*", "*", "*", "IAKTIV", "INT4", 4 * n, 4),
        ("ROHR", "*", "*", "*", "STAT", "CHAR", 4 * n, 4),
        ("ROHR", "*", "*", "*", "PVEC", "RVEC", 4 * n_pts, 4),
        ("ROHR", "*", "*", "*", "XVEC", "RVEC", 4 * (n_pts + 1), 4),  # doesn't match N_OF_POINTS
        ("ROHR", "*", "*", "*", "ODD", "REAL", 4 * (n + 1), 4),       # doesn't match the tk list
        ("ROHR", "*", "*", "*", "FUTURE", "XTYP", 8, 8),              # unknown datatype
        ("KNOT", "*", "*", "*", "PH", "REAL", 4 * 2, 4),
        ("ROHR", "R-1", "R-2", "1002", "DP", "REAL", 4, 4),           # single-object channel only
        ("ROHR", "R-1", "R-2", "1002", "QMAV", "REAL", 4, 4),         # element-type channel wins
        ("ROHR", "R-1", "R-2", "1001", "MVEC", "RVEC", 4 * 2, 4),     # single-object interior points
    ]


def _value(record, channel, i):
    """Deterministic test value of item i of a numeric channel in a record."""
    return float(record * 100 + i) + {"QMAV": 0.5, "PVEC": 0.25, "PH": 0.75}.get(channel, 0.0)


def _write_files(directory, snapshots=SNAPSHOTS, trailing=b""):
    directory.mkdir(parents=True, exist_ok=True)
    offset, xml_rows, layout = 0, [], []
    for objtype, n1, n2, pk, attr, dtype, length, item_len in _channels():
        xml_rows.append(
            f'<XL1 OBJTYPE="{objtype}" NAME1="{n1}" NAME2="{n2}" OBJTYPE_PK="{pk}" ATTRTYPE="{attr}" '
            f'TITLE="t" UNIT="[]" FLAGS="0" DATATYPE="{dtype}" DATAOFFSET="{offset}" '
            f'DATALENGTH="{length}" DATATYPELENGTH="{item_len}" />'
        )
        layout.append((attr, dtype, offset, length, item_len))
        offset += length
    record_length = offset
    (directory / "M-1-0-1.1.MX1").write_text(
        '<?xml version="1.0" encoding="Windows-1252"?>\n<DocumentElement>\n' + "\n".join(xml_rows) + "\n</DocumentElement>\n",
        encoding="Windows-1252",
    )

    with open(directory / "M-1-0-1.MX2", "wb") as f:
        def block(objtype, attr, dtype, item_len, payload):
            f.write(struct.pack("12s12s4si28xi", objtype.ljust(12).encode(), attr.ljust(12).encode(),
                                dtype.ljust(4).encode(), item_len, len(payload)))
            f.write(payload)
        block("ROHR", "tk", "CHAR", 20, b"".join(tk.ljust(20).encode() for tk in TKS))
        block("ROHR", "N_OF_POINTS", "INT4", 4, struct.pack(f"{len(TKS)}i", *N_OF_POINTS))
        block("KNOT", "tk", "CHAR", 20, b"".join(tk.ljust(20).encode() for tk in ["5001", "5002"]))

    with open(directory / "M-1-0-1.1.MXS", "wb") as f:
        for r, (snapshot, timestamp) in enumerate(snapshots):
            rec = bytearray(record_length)
            for attr, dtype, off, length, item_len in layout:
                if attr == "TIMESTAMP":
                    rec[off:off + length] = timestamp.ljust(length).encode()
                elif attr == "SNAPSHOTTYPE":
                    rec[off:off + length] = snapshot.encode()
                elif attr == "CVERSO":
                    rec[off:off + length] = CVERSO.ljust(length).encode()
                elif dtype in ("REAL", "RVEC"):
                    rec[off:off + length] = np.array([_value(r, attr, i) for i in range(length // 4)], "<f4").tobytes()
                elif dtype == "INT4":
                    rec[off:off + length] = np.array([r * 10 + i for i in range(length // 4)], "<i4").tobytes()
                elif dtype == "CHAR":
                    rec[off:off + length] = b"".join([b"OK\x00 ", f"R{r}  ".encode()[:4], b"\x00   "])
            f.write(rec)
        f.write(trailing)
    return str(directory / "M-1-0-1.1.MX1")


@pytest.fixture
def mx1(tmp_path):
    return _write_files(tmp_path / "BZ1")


@pytest.fixture
def mx():
    return SIR3S_Model_MX.__new__(SIR3S_Model_MX)  # the file methods need no toolkit


def _frame(mx, f, layout, tks, props, records, place_holder_value=99999.0, vec_format="str"):
    df, _ = mx._mx_read_frame(f, layout, tks, props, records, [f"r{r}" for r in records],
                              place_holder_value, vec_format, max_chunk_bytes=2**40)
    return df


def test_channels_and_record_index(mx, mx1):
    f = mx._mx_open_file(mx1)
    assert "ROHR~*~*~*~FUTURE" not in f.channels  # unknown datatype skipped
    assert f.n_records == len(SNAPSHOTS)
    assert f.version == CVERSO
    assert list(f.records["snapshot_type"]) == [s for s, _ in SNAPSHOTS]
    assert f.records["timestamp"].iloc[2] == pd.Timestamp("2023-02-13 00:00", tz="UTC")


def test_timeline_keeps_first_record_per_timestamp_like_pt3s(mx, mx1):
    f = mx._mx_open_file(mx1)
    # STAT wins at the first timestamp, TIME at the last one (before TMIN/TMAX).
    assert list(mx._mx_timeline_records(f)) == [0, 2, 3]



def test_file_timestamps_labels_indices_and_strings(mx, mx1):
    f = mx._mx_open_file(mx1)  # file timestamps: "...+00:00" local time
    labels, records = mx._mx_file_timestamps(f, None)
    assert records == [0, 2, 3]
    assert labels == ["2023-02-12 23:00:00.000 +00:00", "2023-02-13 00:00:00.000 +00:00", "2023-02-13 01:00:00.000 +00:00"]
    assert mx._mx_file_timestamps(f, [0, -1, 7]) == ([labels[0], labels[2]], [0, 3])  # 7: out of range, excluded
    # strings are matched by instant, whatever offset they are written with
    assert mx._mx_file_timestamps(f, ["2023-02-13 01:00:00.000 +01:00", "2030-01-01 00:00:00.000 +01:00"]) == ([labels[1]], [2])


def test_timestamp_label_like_get_timestamps():
    label = SIR3S_Model_MX._mx_timestamp_label
    utc = pd.Timestamp("2023-02-12 23:00", tz="UTC")
    assert label("2023-02-13 00:00:00.000000+01:00", utc) == "2023-02-13 00:00:00.000 +01:00"
    assert label("2026-09-02 13:50:55.123456+02:00", utc) == "2026-09-02 13:50:55.123 +02:00"
    assert label("2023-02-13 00:00:00+01:00", utc) == "2023-02-13 00:00:00.000 +01:00"
    assert label("2023-02-12 23:00:00", utc) == "2023-02-12 23:00:00.000 +00:00"  # no offset in the file

def test_stationary_calculation_has_stat_record_only(mx, tmp_path):
    f = mx._mx_open_file(_write_files(tmp_path / "stat", snapshots=SNAPSHOTS[:1]))
    assert list(mx._mx_timeline_records(f)) == [0]


def test_read_values_and_dtypes(mx, mx1):
    f = mx._mx_open_file(mx1)
    out = mx._mx_read(f, ["ROHR~*~*~*~QMAV", "ROHR~*~*~*~IAKTIV", "ROHR~*~*~*~PVEC"], records=[3, 1])
    assert out["ROHR~*~*~*~QMAV"].dtype == np.float32
    assert out["ROHR~*~*~*~IAKTIV"].dtype == np.int32
    np.testing.assert_array_equal(out["ROHR~*~*~*~QMAV"][0], [300.5, 301.5, 302.5])
    np.testing.assert_array_equal(out["ROHR~*~*~*~IAKTIV"][1], [10, 11, 12])
    assert out["ROHR~*~*~*~PVEC"].shape == (2, sum(N_OF_POINTS))


def test_char_decoded_verbatim(mx, mx1):
    f = mx._mx_open_file(mx1)
    channel = f.channels["ROHR~*~*~*~STAT"]
    raw = mx._mx_read(f, [channel.sir3s_id], records=[2])[channel.sir3s_id]
    assert list(SIR3S_Model_MX._mx_decode_char(raw, channel)[0]) == ["OK\x00 ", "R2  ", "\x00   "]


def test_object_layout(mx, mx1):
    layout = mx._mx_object_layout(mx._mx_open_file(mx1), "ROHR")
    assert layout.tks == TKS
    assert set(layout.scalar_channels) == {"QMAV", "IAKTIV", "STAT"}
    assert set(layout.vector_channels) == {"PVEC"}
    assert layout.unresolvable_vector_props == ["XVEC"]
    assert layout.skipped_props == ["ODD"]
    assert set(layout.single_channels) == {"DP", "MVEC"}
    assert set(layout.single_channels["DP"]) == {"1002"}
    np.testing.assert_array_equal(layout.segment_offsets, [0, 2, 5, 6])


def test_result_frame_str_and_multiindex(mx, mx1):
    f = mx._mx_open_file(mx1)
    layout = mx._mx_object_layout(f, "ROHR")
    tks = ["1002", "9999"]  # 9999 is not in the file

    df = _frame(mx, f, layout, tks, ["QMAV", "PVEC"], [2], place_holder_value=-1.0, vec_format="str")
    assert df[("1002", "QMAV")].iloc[0] == 201.5
    expected_vec = "\t".join(SIR3S_Model_MX._mx_format_float(v) for v in [202.25, 203.25, 204.25])
    assert df[("1002", "PVEC")].iloc[0] == expected_vec
    assert df[("9999", "QMAV")].iloc[0] == -1.0 and df[("9999", "PVEC")].iloc[0] == -1.0

    mi = _frame(mx, f, layout, tks, ["QMAV", "PVEC"], [2], place_holder_value=-1.0, vec_format="multiindex")
    assert mi.columns.names == ["tk", "property", "interior points"]
    assert list(mi.loc["r2", ("1002", "PVEC")]) == [202.25, 203.25, 204.25]
    assert mi.loc["r2", ("1002", "QMAV", -1)] == 201.5
    assert mi.loc["r2", ("9999", "PVEC", 0)] == -1.0


@pytest.mark.parametrize("gap", [256 * 1024, 0])  # 0: every run of items is read separately
def test_tk_filtered_read_equals_full_read(mx, mx1, monkeypatch, gap):
    monkeypatch.setattr(SIR3S_Model_MX, "_MX_SPAN_MERGE_GAP_BYTES", gap)
    f = mx._mx_open_file(mx1)
    layout = mx._mx_object_layout(f, "ROHR")
    props = ["QMAV", "IAKTIV", "STAT", "PVEC", "DP"]
    for vec_format in ("str", "multiindex"):
        full = _frame(mx, f, layout, TKS, props, [0, 3, 5], vec_format=vec_format)
        for tks in (["1003", "1001"], ["1002"], ["1003"]):
            part = _frame(mx, f, layout, tks, props, [0, 3, 5], vec_format=vec_format)
            assert mx._mx_frame_plan(layout, tks, props).items[layout.scalar_channels["QMAV"].sir3s_id] is not None
            expected = full.loc[:, full.columns.get_level_values("tk").isin(tks)]
            pd.testing.assert_frame_equal(part, expected[part.columns])


def test_chunked_frames_equal_single_frame(mx, mx1):
    f = mx._mx_open_file(mx1)
    layout = mx._mx_object_layout(f, "ROHR")
    props = ["QMAV", "STAT", "PVEC"]
    records = list(range(f.n_records))
    one, _ = mx._mx_read_frame(f, layout, TKS, props, records, records, 99999.0, "str", max_chunk_bytes=2**40)
    many, _ = mx._mx_read_frame(f, layout, TKS, props, records, records, 99999.0, "str", max_chunk_bytes=1)
    pd.testing.assert_frame_equal(many, one)
    # timestamps not in the file (record None) are filled with the placeholder
    gaps, _ = mx._mx_read_frame(f, layout, TKS, props, [0, None, 2], ["a", "b", "c"], -1.0, "str", max_chunk_bytes=1)
    assert (gaps.loc["b"] == -1.0).all() and gaps.loc["c"].equals(one.loc[2].rename("c"))
    one_chunk, _ = mx._mx_read_frame(f, layout, TKS, props, [0, None, 2], ["a", "b", "c"], -1.0, "str", max_chunk_bytes=2**40)
    pd.testing.assert_frame_equal(one_chunk, gaps)  # known and missing timestamps in the same chunk


def test_read_frame_drops_full_placeholder_columns(mx, mx1):
    f = mx._mx_open_file(mx1)
    layout = mx._mx_object_layout(f, "ROHR")
    props = ["QMAV", "STAT", "PVEC", "DP"]   # DP: only tk 1002 has it -> 1001/1003 are all placeholder
    tks = TKS + ["9999"]                      # 9999: not in the file -> all placeholder
    records = list(range(f.n_records))
    for vec_format in ("str", "multiindex"):
        full, n0 = mx._mx_read_frame(f, layout, tks, props, records, records, 99999.0, vec_format, 2**40)
        dropped, n = mx._mx_read_frame(f, layout, tks, props, records, records, 99999.0, vec_format, 2**40,
                                       drop_full_place_holder_columns=True)
        expected = full.loc[:, ~full.eq(99999.0).all()]
        assert n0 == 0 and n == full.shape[1] - expected.shape[1] > 0
        pd.testing.assert_frame_equal(dropped, expected)


def test_result_dtype(mx, mx1):
    f = mx._mx_open_file(mx1)
    layout = mx._mx_object_layout(f, "ROHR")
    cid = layout.scalar_channels["QMAV"].sir3s_id
    raw = mx._mx_read(f, [cid], records=[2])[cid]
    df32 = _frame(mx, f, layout, TKS, ["QMAV", "PVEC"], [2], vec_format="multiindex")
    assert set(df32.dtypes) == {np.dtype("float32")}
    np.testing.assert_array_equal(df32.xs("QMAV", axis=1, level="property").to_numpy()[0], raw[0])  # bit-exact


def test_single_object_channel(mx, mx1):
    f = mx._mx_open_file(mx1)
    layout = mx._mx_object_layout(f, "ROHR")
    df = _frame(mx, f, layout, ["1001", "1002"], ["DP"], [1], place_holder_value=-1.0)
    assert df[("1001", "DP")].iloc[0] == -1.0
    assert df[("1002", "DP")].iloc[0] == _value(1, "DP", 0)


def test_read_results_snapshots(mx, mx1):
    df = mx._mx_read_results("ROHR", properties=["QMAV"], snapshot_types=["TMIN", "TMAX"], mx1_filepath=mx1)
    assert list(df.index.get_level_values("snapshot_type")) == ["TMIN", "TMAX"]
    assert df[("1001", "QMAV", -1)].iloc[1] == _value(5, "QMAV", 0)


def test_mxs_older_than_mx1_raises(mx, mx1):
    os.utime(mx1.replace(".MX1", ".MXS"), (1_000_000, 1_000_000))
    with pytest.raises(ValueError, match="older"):
        mx._mx_open_file(mx1)


def test_order_columns():
    cols = pd.MultiIndex.from_tuples([("b", "Y"), ("a", "Y"), ("b", "X"), ("a", "X")])
    df = pd.DataFrame([[1, 2, 3, 4]], columns=cols)
    ordered = SIR3S_Model_MX._mx_order_columns(df, ["a", "b"], ["X", "Y"])
    assert list(ordered.columns) == [("a", "X"), ("a", "Y"), ("b", "X"), ("b", "Y")]


def test_trailing_bytes_ignored(mx, tmp_path):
    f = mx._mx_open_file(_write_files(tmp_path / "trail", trailing=b"\x01\x02"))
    assert f.n_records == len(SNAPSHOTS)


def test_changed_file_detected(mx, mx1):
    f = mx._mx_open_file(mx1)
    with open(f.mxs_path, "ab") as fh:
        fh.write(b"\x00" * f.record_length)
    with pytest.raises(SIR3S_Model_MX._MxFileChangedError):
        mx._mx_read(f, ["ROHR~*~*~*~QMAV"])


def test_empty_mx1_raises(mx, tmp_path):
    path = tmp_path / "empty.1.MX1"
    path.write_text('<?xml version="1.0"?>\n<DocumentElement>\n</DocumentElement>\n')
    (tmp_path / "empty.1.MXS").write_bytes(b"")
    with pytest.raises(ValueError, match="no channels"):
        mx._mx_open_file(str(path))


def test_format_float():
    fmt = SIR3S_Model_MX._mx_format_float
    assert fmt(0.0) == "0"
    assert fmt(1.23456785) == "1.234568"
    assert fmt(1e-9) == "1E-09"


def test_format_floats_matches_scalar_version():
    rng = np.random.default_rng(0)
    values = np.concatenate([
        (rng.standard_normal(20000) * 10.0 ** rng.integers(-8, 9, 20000)).astype(np.float32),
        np.array([1234568.5, 1234567.5, -1234568.5, 637073.25, 0.0, -0.0, 1e-9, 99999.0,
                  np.nan, np.inf], dtype=np.float32),  # exact ties, zeros, special values
        np.repeat(np.float32(59.83105), 50),  # duplicates
    ]).reshape(-1, 2)
    expected = np.array([SIR3S_Model_MX._mx_format_float(v) for v in values.ravel().tolist()],
                        dtype=object).reshape(values.shape)
    assert (SIR3S_Model_MX._mx_format_floats(values) == expected).all()
    assert SIR3S_Model_MX._mx_format_floats(np.array([], dtype=np.float32)).shape == (0,)


def _result_dir(mx, tmp_path, files):
    """Result directory with empty files; files: {name: mtime}."""
    bz = tmp_path / "B1" / "V0" / "BZ1"
    bz.mkdir(parents=True)
    for name, mtime in files.items():
        (bz / name).write_bytes(b"")
        os.utime(bz / name, (mtime, mtime))
    mx.Mid = "M-1-0-1"
    mx.GetWorkingDirectory = lambda: str(tmp_path)
    return bz


def test_output_factors_include_older_files(mx, tmp_path):
    # .2/.4 from the latest calculation (.MX1 < .MX2 <= .MXS), .1 left over from an earlier one
    bz = _result_dir(mx, tmp_path, {
        "M-1-0-1.1.MX1": 100, "M-1-0-1.1.MXS": 101,
        "M-1-0-1.2.MX1": 200, "M-1-0-1.4.MX1": 200, "M-1-0-1.MX2": 201,
        "M-1-0-1.2.MXS": 202, "M-1-0-1.4.MXS": 202,
    })
    assert mx._mx_result_factors() == ([1, 2, 4], [2, 4])
    assert mx._mx_output_factors() == (2, 4)                            # most recent calculation
    assert mx._mx_current_mx1_filepath() == str(bz / "M-1-0-1.4.MX1")  # DTFAK_GROSS file
    assert mx._mx_resolve_mx1(1) == str(bz / "M-1-0-1.1.MX1")          # older file is still selectable
    with pytest.raises(ValueError, match=r"1 \(earlier calculation\)"):
        mx._mx_resolve_mx1(3)


def test_default_is_most_recent_even_if_an_older_file_has_a_larger_factor(mx, tmp_path):
    # old .4 left over, the most recent calculation only wrote .1
    bz = _result_dir(mx, tmp_path, {"M-1-0-1.4.MX1": 100, "M-1-0-1.4.MXS": 101,
                                    "M-1-0-1.1.MX1": 200, "M-1-0-1.MX2": 201, "M-1-0-1.1.MXS": 202})
    assert mx._mx_resolve_mx1() == str(bz / "M-1-0-1.1.MX1")
    assert mx._mx_resolve_mx1(4) == str(bz / "M-1-0-1.4.MX1")


def test_older_result_file_logs_warning(mx, tmp_path, caplog):
    import shutil, logging
    src = _write_files(tmp_path / "src")
    bz = tmp_path / "bz"
    bz.mkdir()
    for name in ("M-1-0-1.1.MX1", "M-1-0-1.MX2", "M-1-0-1.1.MXS"):
        shutil.copy2(os.path.join(os.path.dirname(src), name), bz / name)
    os.utime(bz / "M-1-0-1.1.MX1", (100, 100))
    os.utime(bz / "M-1-0-1.1.MXS", (101, 101))
    os.utime(bz / "M-1-0-1.MX2", (200, 200))      # newer calculation after this .MXS
    with caplog.at_level(logging.WARNING):
        f = mx._mx_open_file(str(bz / "M-1-0-1.1.MX1"))
    assert f.n_records == len(SNAPSHOTS)
    assert "older than the most recent calculation" in caplog.text


def test_output_factors_single_file(mx, tmp_path):
    _result_dir(mx, tmp_path, {"M-1-0-1.1.MX1": 100, "M-1-0-1.MX2": 101, "M-1-0-1.1.MXS": 102})
    assert mx._mx_output_factors() == (1, 1)


def test_resolve_mx1_prefers_file_without_output_factor(mx, tmp_path):
    bz = _result_dir(mx, tmp_path, {"M-1-0-1.2.MX1": 200, "M-1-0-1.4.MX1": 200, "M-1-0-1.MX2": 201,
                                    "M-1-0-1.2.MXS": 202, "M-1-0-1.4.MXS": 202})
    assert mx._mx_resolve_mx1() == str(bz / "M-1-0-1.4.MX1")   # no plain file: DTFAK_GROSS
    (bz / "M-1-0-1.MX1").write_bytes(b"")
    assert mx._mx_resolve_mx1() == str(bz / "M-1-0-1.MX1")     # plain file takes precedence
    assert mx._mx_resolve_mx1(2) == str(bz / "M-1-0-1.2.MX1")  # explicit factor: that file
    assert mx._mx_resolve_mx1(4) == str(bz / "M-1-0-1.4.MX1")
    with pytest.raises(ValueError, match="has no result files"):
        mx._mx_resolve_mx1(3)


def test_open_file_without_output_factor(mx, tmp_path):
    src = _write_files(tmp_path / "src")
    plain = tmp_path / "plain"
    plain.mkdir()
    import shutil
    shutil.copy2(src, plain / "M-1-0-1.MX1")
    shutil.copy2(src.replace(".1.MX1", ".MX2"), plain / "M-1-0-1.MX2")
    shutil.copy2(src.replace(".MX1", ".MXS"), plain / "M-1-0-1.MXS")
    f = mx._mx_open_file(str(plain / "M-1-0-1.MX1"))
    assert f.mxs_path.endswith("M-1-0-1.MXS") and f.mx2_path.endswith("M-1-0-1.MX2")
    assert f.n_records == len(SNAPSHOTS)


def test_get_result_file_properties(tmp_path):
    from enum import Enum
    from sir3stoolkit.mantle.dataframes import SIR3S_Model_Dataframes
    s3s = SIR3S_Model_Dataframes.__new__(SIR3S_Model_Dataframes)
    mx1 = _write_files(tmp_path / "B1" / "V0" / "BZ1")
    s3s.Mid = "M-1-0-1"
    s3s.GetWorkingDirectory = lambda: str(tmp_path)
    s3s.ObjectTypes = Enum("ObjectTypes", ["Pipe", "Node"])

    df = s3s.get_result_file_properties()
    assert set(df["objtype"]) == {"ROHR", "KNOT"}
    rohr = df[df["objtype"] == "ROHR"].set_index("property")
    assert rohr.loc["QMAV", "stored_for"] == "all elements" and rohr.loc["QMAV", "element_type"] == "Pipe"
    assert rohr.loc["PVEC", "stored_for"] == "all elements"
    assert rohr.loc["DP", "stored_for"] == "single elements"
    assert set(rohr.index[rohr["stored_for"] == "not splittable"]) == {"XVEC", "ODD"}
    assert "FUTURE" not in rohr.index  # unknown datatype
    assert set(df["result_file"]) == {os.path.basename(mx1)} and set(df["n_timestamps"]) == {3}
    assert list(s3s.get_result_file_properties(element_type=s3s.ObjectTypes.Node)["property"]) == ["PH"]


def test_single_object_vector_channel(mx, mx1):
    f = mx._mx_open_file(mx1)
    layout = mx._mx_object_layout(f, "ROHR")
    expected = [_value(2, "MVEC", i) for i in range(2)]
    df = _frame(mx, f, layout, ["1001", "1002"], ["MVEC"], [2], place_holder_value=-1.0)
    assert df[("1001", "MVEC")].iloc[0] == "\t".join(SIR3S_Model_MX._mx_format_float(v) for v in expected)
    assert df[("1002", "MVEC")].iloc[0] == -1.0
    mi = _frame(mx, f, layout, ["1001", "1002"], ["MVEC"], [2], place_holder_value=-1.0, vec_format="multiindex")
    assert list(mi.loc["r2", ("1001", "MVEC")]) == expected
    assert (mi.loc["r2", ("1002", "MVEC")] == -1.0).all()


def test_progress_logs_every_20_percent(caplog):
    import logging
    log = logging.getLogger("test_mx_progress")
    with caplog.at_level(logging.INFO, logger="test_mx_progress"):
        progress = SIR3S_Model_MX._MxProgress(log, "reading", 10, "records")
        for n in (1, 1, 5, 3):  # 10 %, 20 %, 70 % (passes 40 and 60), 100 %
            progress.update(n)
        SIR3S_Model_MX._MxProgress(log, "off", 10, "records", enabled=False).update(10)
    assert [m.split(":")[1].split("%")[0].strip() for m in caplog.messages] == ["20", "70", "100"]


# --- generate_element_results_dataframe(bulk=True) end to end, on the synthetic files ---------------

@pytest.fixture
def s3s(tmp_path):
    """SIR3S_Model_Dataframes on the synthetic result files; the API result calls fail the test."""
    from enum import Enum
    from sir3stoolkit.mantle.dataframes import SIR3S_Model_Dataframes
    s = SIR3S_Model_Dataframes.__new__(SIR3S_Model_Dataframes)
    _write_files(tmp_path / "B1" / "V0" / "BZ1")
    s.Mid = "M-1-0-1"
    s.GetWorkingDirectory = lambda: str(tmp_path)
    s.ObjectTypes = Enum("ObjectTypes", ["Pipe", "Node", "Valve"])
    s._SIR3S_Model_Dataframes__resolve_given_tks = lambda element_type, tks, filter_container_tks: tks or TKS
    s._SIR3S_Model_Dataframes__is_get_endnodes_applicable = lambda element_type: True
    s.GetValue = lambda Tk, propertyName: (f"name_{Tk}",)
    s.GetEndNodes = lambda Tk: ("N1", "N2")
    s.GetResultProperties_from_elementType = lambda elementType, onlySelectedVectors=False: ["PVEC", "QMAV"]

    def no_api(**kwargs):
        raise AssertionError("bulk=True must not call GetResultfortimestamp()")
    s.GetResultfortimestamp = no_api
    s.GetTimeStamps = no_api
    return s


def test_bulk_results_dataframe_all_properties(s3s, mx, caplog):
    import logging
    with caplog.at_level(logging.WARNING):
        df = s3s.generate_element_results_dataframe(s3s.ObjectTypes.Pipe, bulk=True)
    assert "['ODD', 'XVEC']" in caplog.text  # stored, but can't be split per element
    labels, records = mx._mx_file_timestamps(s3s._mx_get_file(s3s._mx_resolve_mx1()), None)
    assert list(df.index) == labels
    assert df.columns.names == ["tk", "name", "end_nodes", "property"]
    # API order first (PVEC, QMAV), then the rest in file order; DP/MVEC only where a channel exists
    assert list(df["1001"].columns.get_level_values("property")) == ["PVEC", "QMAV", "IAKTIV", "STAT", "MVEC"]
    assert list(df["1002"].columns.get_level_values("property")) == ["PVEC", "QMAV", "IAKTIV", "STAT", "DP"]
    assert df.loc[labels[1], ("1002", "name_1002", "('N1', 'N2')", "QMAV")] == _value(records[1], "QMAV", 1)
    assert df.loc[labels[1], ("1003", "name_1003", "('N1', 'N2')", "IAKTIV")] == records[1] * 10 + 2
    assert df[("1001", "name_1001", "('N1', 'N2')", "QMAV")].dtype == np.float32
    # same values as the file-level frame
    f = s3s._mx_get_file(s3s._mx_resolve_mx1())
    layout = mx._mx_object_layout(f, "ROHR")
    raw, _ = mx._mx_read_frame(f, layout, TKS, ["PVEC", "QMAV", "IAKTIV", "STAT", "DP", "MVEC"], records, labels,
                               99999.0, "str", 2**40, drop_full_place_holder_columns=True)
    flat = df.copy()
    flat.columns = flat.columns.droplevel(["name", "end_nodes"])
    pd.testing.assert_frame_equal(flat, raw[flat.columns], check_names=False)


def test_bulk_results_dataframe_filters_and_multiindex(s3s, caplog):
    import logging
    with caplog.at_level(logging.WARNING):
        df = s3s.generate_element_results_dataframe(
            s3s.ObjectTypes.Pipe, tks=["1003"], properties=["QMAV", "PVEC", "NOPE", "XVEC"], timestamps=[-1],
            bulk=True, vec_format="multiindex")
    assert "['XVEC']" in caplog.text and "['NOPE']" in caplog.text
    assert list(df.index) == ["2023-02-13 01:00:00.000 +00:00"]
    assert df.columns.names == ["tk", "name", "end_nodes", "property", "interior points"]
    assert list(df.columns.get_level_values("property")) == ["QMAV", "PVEC"]
    assert df.iloc[0, 0] == _value(3, "QMAV", 2) and df.iloc[0, 1] == _value(3, "PVEC", 5)
    assert set(df.dtypes) == {np.dtype("float32")}


def test_bulk_results_dataframe_errors(s3s, caplog):
    import logging
    pipe = s3s.ObjectTypes.Pipe
    with pytest.raises(ValueError, match="vec_format"):
        s3s.generate_element_results_dataframe(pipe, bulk=True, vec_format="flat")
    with pytest.raises(ValueError, match="output_factor=7"):
        s3s.generate_element_results_dataframe(pipe, bulk=True, output_factor=7)
    with caplog.at_level(logging.WARNING):
        assert s3s.generate_element_results_dataframe(s3s.ObjectTypes.Valve, bulk=True).empty
    assert "holds no results for 'Valve'" in caplog.text
    s3s._mx_physical_memory = lambda: (1000, 1000)
    with pytest.raises(MemoryError):
        s3s.generate_element_results_dataframe(pipe, bulk=True)
    del s3s._mx_physical_memory
    mx1 = s3s._mx_resolve_mx1()
    os.utime(mx1.replace(".MX1", ".MXS"), (1_000_000, 1_000_000))  # .MXS older than .MX1: inconsistent
    with pytest.raises(RuntimeError, match="bulk=False"):
        s3s.generate_element_results_dataframe(pipe, bulk=True)
    for name in os.listdir(os.path.dirname(mx1)):
        os.remove(os.path.join(os.path.dirname(mx1), name))
    with pytest.raises(FileNotFoundError):
        s3s.generate_element_results_dataframe(pipe, bulk=True)


def test_merge_str_and_multiindex_results_give_the_same_rows(s3s):
    pipe = s3s.ObjectTypes.Pipe
    model = pd.DataFrame({"tk": ["1001", "1002"], "L": [1.0, 2.0]})
    kwargs = dict(tks=["1001", "1002"], properties=["QMAV", "PVEC"], timestamps=[1], bulk=True)

    df_str = s3s.generate_element_results_dataframe(pipe, **kwargs)
    df_str = s3s.add_interior_points_to_start_end_sequence(df_str)
    assert df_str[("1002", "name_1002", "('N1', 'N2')", "QMAV")].dtype == np.float32  # scalars stay float32
    df_str, timestamp_to_tuple_index = s3s.convert_rows_to_single_tuple_row(df_str)
    assert timestamp_to_tuple_index == {"2023-02-13 00:00:00.000 +00:00": 0}
    merged_str = s3s.merge_model_data_and_results(model, df_str)

    merged_multi = s3s.merge_model_data_and_results(
        model, s3s.generate_element_results_dataframe(pipe, vec_format="multiindex", **kwargs))

    pd.testing.assert_frame_equal(merged_str[sorted(merged_str.columns)], merged_multi[sorted(merged_multi.columns)])
    row = merged_multi.set_index("tk").loc["1002"]
    assert row["QMAV"] == (201.5,)  # float32 values in shortest representation
    assert row["PVEC_sequence"] == ((202.25, 203.25, 204.25),)
    assert row["PVEC_start"] == (202.25,) and row["PVEC_end"] == (204.25,)


def test_str_merge_needs_a_single_row(s3s):
    df = s3s.generate_element_results_dataframe(s3s.ObjectTypes.Pipe, properties=["QMAV"], bulk=True)
    assert s3s.merge_model_data_and_results(pd.DataFrame({"tk": TKS}), df).empty  # 3 timestamps
    out, mapping = s3s.convert_rows_to_single_tuple_row(pd.concat([df, df]))  # index not unique
    assert out.empty and mapping == {}
