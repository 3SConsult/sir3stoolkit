"""
Network 3: "Musterstadt" - a fictional district heating network.

Builds a SIR 3S district heating model from scratch with the SIR 3S Toolkit. The network is
made up (no real infrastructure), so the model can be published and shared - it is the shared
demo model of the mantle tutorials.

Contents (all deterministic, only the tks differ between builds):

- Heat plant "Heizwerk" in its own container: return pressure holding (PKON, 3 bar), two
  parallel network pumps, a non-return (flap) valve, a heat feeder with a supply temperature
  table, and shut-off valves to the network. Plant and network are linked via block connection
  nodes (VKNO), as elements cannot be connected across containers directly.
- Network in the main container: a main street ("Hauptstrasse", 1.6 km) with five side streets
  to the north and south, a ring road with a sectioning valve, about 170 houses and four large
  consumers (school, indoor pool, hospital, town hall), each with supply (VL) and return (RL).
- Daily load profiles (load factor tables), two longitudinal sections (AGSN) with supply and
  return, two groups, the thermal balance of the whole network.
- Calculation: quasi-stationary over one day (2026-01-15, 1 h time step) incl. thermal
  calculation. Output factors small = 1 (time curves: thermal balance, plant and hospital
  pressures/temperatures, pump flow, feeder output; hourly) and large = 2 (all elements; every 2 h).

Elements have unique IDREFERENZ values (e.g. "V-HS-08", "FWVB-SCHULE", "AGSN-KRANKENHAUS"),
so tutorials can look them up with GetTkFromIDReference() instead of hard-coding tks - the tks
change with every build.

Run: python Network3.py [path of the .db3 to create]  (default: Network3.db3 next to this file)
"""

import math
import os
import random
import sqlite3
import struct
import sys
from pathlib import Path

from sir3stoolkit.core import wrapper

SIR3S_SIRGRAF_DIR = r"C:\3S\SIR 3S\SirGraf-90-15-00-24_Quebec-Upd2"  # change to local path
DB_FILE = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "Network3.db3"))

wrapper.Initialize_Toolkit(SIR3S_SIRGRAF_DIR)
model = wrapper.SIR3S_Model()
OT = model.ObjectTypes

rng = random.Random(3)  # fixed seed: same network on every build

# ---------------------------------------------------------------------------------------------
# Network data (pure Python, no SIR 3S calls)
# ---------------------------------------------------------------------------------------------
RL_OFFSET = (4.0, -4.0)  # return line drawn next to the supply line
HEIZWERK_SYMBOL = (40, 975, 90, 1015)  # block symbol in the main view (xmin, ymin, xmax, ymax), next to node HS-00
HEIZWERK_SHEET = (0, 940, 140, 1020)  # drawing area (grid) inside the block, around the plant elements
T_SUPPLY, T_RETURN = 90.0, 60.0  # design temperatures [°C]
LF_PEAK = 1.25  # max. load factor of the daily profile, used for pipe sizing


def height(x, y):
    """Geodetic height [m]: gently rising to the east, with some hills."""
    return round(200.0 + 0.012 * x + 6.0 * math.sin(y / 230.0) + 3.0 * math.cos(x / 170.0), 2)


nodes = {}  # id -> dict(x, y, street)
pipes = []  # dict(id, ki, kk, kind: main|street|ring|house)
consumers = []  # dict(id, node, w0, profile, description)
valves = []  # dict(id, ki, kk, description)


def add_node(nid, x, y, street=""):
    nodes[nid] = {"x": float(x), "y": float(y), "street": street}
    return nid


# Main street: boundary node HS-00 next to the plant, then a node every 100 m
add_node("HS-00", 100, 1000, "Hauptstrasse")
for i in range(1, 17):
    add_node(f"HS-{i:02d}", 100 + 100 * i, 1000, "Hauptstrasse")
    pipes.append({"id": f"HS-{i:02d}", "ki": f"HS-{i - 1:02d}", "kk": f"HS-{i:02d}", "kind": "main"})

# Side streets branch off every 300 m, each with 8 segments of 50 m to the north (N) and south (S).
# The first segment of each side street starts with a shut-off valve.
SIDE_STREETS = [("AW", "Ahornweg", 2), ("BW", "Birkenweg", 5), ("KA", "Kastanienallee", 8),
                ("LS", "Lindenstrasse", 11), ("EW", "Eichenweg", 14)]
for code, street, hs in SIDE_STREETS:
    x0 = 100 + 100 * hs
    for side, sign in (("N", 1), ("S", -1)):
        valve_in = add_node(f"{code}{side}-A0", x0, 1000 + sign * 10, street)
        valve_out = add_node(f"{code}{side}-A1", x0, 1000 + sign * 20, street)
        pipes.append({"id": f"{code}{side}-A0", "ki": f"HS-{hs:02d}", "kk": valve_in, "kind": "street"})
        valves.append({"id": f"{code}{side}", "ki": valve_in, "kk": valve_out, "description": f"Absperrschieber {street} {'Nord' if sign > 0 else 'Sued'}"})
        prev = valve_out
        for k in range(1, 9):
            nid = add_node(f"{code}{side}-{k:02d}", x0, 1000 + sign * (20 + 50 * k), street)
            pipes.append({"id": f"{code}{side}-{k:02d}", "ki": prev, "kk": nid, "kind": "street"})
            prev = nid

# Ring road connecting the north ends of the side streets (meshes the network), with a
# sectioning valve between Kastanienallee and Lindenstrasse.
ring_ends = [f"{code}N-08" for code, _, _ in SIDE_STREETS]
for a, b in zip(ring_ends[:-1], ring_ends[1:]):
    if a.startswith("KA"):
        xa, xb, y = nodes[a]["x"], nodes[b]["x"], nodes[a]["y"]
        add_node("RS-A0", (xa + xb) / 2 - 10, y, "Ringstrasse")
        add_node("RS-A1", (xa + xb) / 2 + 10, y, "Ringstrasse")
        pipes.append({"id": "RS-03", "ki": a, "kk": "RS-A0", "kind": "ring"})
        valves.append({"id": "RS", "ki": "RS-A0", "kk": "RS-A1", "description": "Trennschieber Ringstrasse"})
        pipes.append({"id": "RS-04", "ki": "RS-A1", "kk": b, "kind": "ring"})
    else:
        pipes.append({"id": f"RS-{ring_ends.index(a) + 1:02d}", "ki": a, "kk": b, "kind": "ring"})

# House connections: two houses per side street node (west/east), one per main street node
# without a side street (alternately north/south). Each house: connection pipe + consumer.
def add_house(street_node, dx, dy, house_id, w0, profile, description):
    hid = add_node(f"H-{house_id}", nodes[street_node]["x"] + dx, nodes[street_node]["y"] + dy, nodes[street_node]["street"])
    pipes.append({"id": f"H-{house_id}", "ki": street_node, "kk": hid, "kind": "house"})
    consumers.append({"id": house_id, "node": hid, "w0": w0, "profile": profile, "description": description})


for code, street, _ in SIDE_STREETS:
    for side in ("N", "S"):
        for k in range(1, 9):
            sn = f"{code}{side}-{k:02d}"
            for hs_side, dx in (("W", -15), ("O", 15)):
                no = 2 * k - (1 if hs_side == "W" else 0)
                add_house(sn, dx, 0, f"{code}{side}-{k:02d}{hs_side}", round(rng.uniform(12, 35), 1), "Wohnen",
                          f"Wohnhaus {street} {'Nord' if side == 'N' else 'Sued'} {no}")
branch_hs = {hs for _, _, hs in SIDE_STREETS}
for i in range(1, 17):
    if i not in branch_hs:
        dy = 15 if i % 2 else -15
        add_house(f"HS-{i:02d}", 0, dy, f"HS-{i:02d}", round(rng.uniform(15, 45), 1), "Wohnen", f"Wohnhaus Hauptstrasse {i}")

# Large consumers at street ends
for cid, street_node, dx, dy, w0, desc in [
    ("SCHULE", "BWS-08", 0, -30, 250.0, "Schule"),
    ("HALLENBAD", "LSS-08", 0, -30, 400.0, "Hallenbad"),
    ("KRANKENHAUS", "HS-16", 40, 0, 600.0, "Krankenhaus"),
    ("RATHAUS", "KAS-04", -30, 0, 150.0, "Rathaus"),
]:
    add_house(street_node, dx, dy, cid, w0, "Gewerbe", desc)

# Pipe sizing: peak flow downstream of each pipe on the tree (ring ignored), velocity limit
DN_KMR = [32, 40, 50, 65, 80, 100, 125, 150, 200, 250, 300]
DI_KMR = {32: 37.2, 40: 43.1, 50: 54.5, 65: 70.3, 80: 82.5, 100: 107.1, 125: 132.5, 150: 160.3, 200: 210.1, 250: 263.0, 300: 312.7}
DN_FLEX = [25, 32, 50, 65, 80]
DI_FLEX = {25: 30.4, 32: 39.4, 50: 60.0, 65: 76.2, 80: 98.0}
children = {}
for p in pipes:
    if p["kind"] != "ring":
        children.setdefault(p["ki"], []).append(p)
for v in valves:
    if v["id"] != "RS":
        children.setdefault(v["ki"], []).append({"kk": v["kk"]})
load_at = {c["node"]: c["w0"] for c in consumers}


def downstream_load(nid):
    return load_at.get(nid, 0.0) + sum(downstream_load(c["kk"]) for c in children.get(nid, []))


def size_dn(load_kw, dns, dis, v_max, dn_min):
    q = load_kw * LF_PEAK / (4.19 * (T_SUPPLY - T_RETURN)) / 1000.0  # m3/s
    for dn in dns:
        if dn >= dn_min and q / (math.pi / 4 * (dis[dn] / 1000) ** 2) <= v_max:
            return dn
    return dns[-1]


for p in pipes:
    load = downstream_load(p["kk"])
    if p["kind"] == "house":
        p["table"], p["dn"] = "FLEXWELL-F", size_dn(load, DN_FLEX, DI_FLEX, 1.0, 25)
    elif p["kind"] == "ring":
        p["table"], p["dn"] = "KMR-Daemmr2", 80
    else:
        p["table"], p["dn"] = "KMR-Daemmr2", size_dn(load, DN_KMR, DI_KMR, 1.5, 50)
    a, b = nodes[p["ki"]], nodes[p["kk"]]
    p["L"] = round(math.hypot(b["x"] - a["x"], b["y"] - a["y"]), 1)
total_load = sum(c["w0"] for c in consumers)

# Daily profiles (hour -> factor) and plant supply temperature (hour -> °C)
PROFILES = {
    "Wohnen": [0.55, 0.50, 0.50, 0.50, 0.55, 0.75, 1.15, 1.25, 1.10, 0.95, 0.85, 0.80, 0.80,
               0.75, 0.70, 0.75, 0.85, 1.00, 1.10, 1.10, 1.00, 0.85, 0.70, 0.60, 0.55],
    "Gewerbe": [0.30, 0.30, 0.30, 0.30, 0.35, 0.60, 1.00, 1.20, 1.20, 1.15, 1.10, 1.05, 1.00,
                1.00, 1.00, 1.00, 0.95, 0.80, 0.60, 0.45, 0.40, 0.35, 0.30, 0.30, 0.30],
}
SUPPLY_TEMP = [(0, 85.0), (5, 85.0), (6, 95.0), (10, 95.0), (12, 90.0), (16, 90.0), (17, 95.0), (21, 95.0), (22, 85.0), (24, 85.0)]

print(f"Network 3: {len(nodes)} network nodes (x2 for VL/RL), {len(pipes)} pipes (x2), {len(consumers)} consumers, "
      f"{len(valves)} valves (x2), total load {total_load / 1000:.2f} MW")

# ---------------------------------------------------------------------------------------------
# Build the SIR 3S model
# ---------------------------------------------------------------------------------------------
if os.path.exists(DB_FILE):
    raise SystemExit(f"{DB_FILE} already exists - delete it first (NewModel adds a new model to an existing database).")

model.NewModel(dbName=DB_FILE, providerType=model.ProviderTypes.SQLite, netType=model.NetworkType.DistrictHeating,
               modelDescription="Network 3 - Musterstadt (fictional district heating network)", namedInstance="", userID="", password="")
main = model.GetMainContainer()[0]


def rl(x, y):
    return x + RL_OFFSET[0], y + RL_OFFSET[1]


model.StartEditSession("Network 3")

# --- tables --------------------------------------------------------------------------------
def fill_time_table(table_tk, rows, value_property):
    """Overwrite the default row of a new time table and append the rest: rows = [(seconds, value)]."""
    existing = model.GetTableRows(table_tk)[0]
    for i, (t, value) in enumerate(rows):
        row = existing[i] if i < len(existing) else model.AddTableRow(table_tk)[0]
        model.SetValue(row, "Zeit", str(t))
        model.SetValue(row, value_property, str(value))


lfkt = {}
lfkt["Wohnen"] = model.GetTksofElementType(OT.LoadFactorTable)[0]  # default table of a new model
lfkt["Gewerbe"] = model.InsertElement(OT.LoadFactorTable, "LFKT-GEWERBE")
for name, tk in lfkt.items():
    model.SetValue(tk, "Name", name)
    model.SetValue(tk, "Beschreibung", f"Tageslastgang {name}")
    model.SetValue(tk, "Idreferenz", f"LFKT-{name.upper()}")
    fill_time_table(tk, [(3600 * h, f) for h, f in enumerate(PROFILES[name])], "Lf")

tevt = model.GetTksofElementType(OT.TemperatureTable)[0]  # default table of a new model
model.SetValue(tevt, "Name", "TVL Heizwerk")
model.SetValue(tevt, "Beschreibung", "Vorlauftemperatur Heizwerk")
model.SetValue(tevt, "Idreferenz", "TEVT-HEIZWERK")
fill_time_table(tevt, [(3600 * h, t) for h, t in SUPPLY_TEMP], "T")

# Network pumps: the default pump curve (4-52 m3/h) is too small, scale its flows
pumk = model.GetTksofElementType(OT.PumpCharTable)[0]
model.SetValue(pumk, "Name", "Netzpumpe")
for row in model.GetTableRows(pumk)[0]:
    q = float(model.GetValue(row, "Q")[0].replace(",", "."))
    model.SetValue(row, "Q", str(round(q * 2.5, 2)))

# --- network nodes, VL and RL --------------------------------------------------------------
tk_v, tk_r = {}, {}
for nid, n in nodes.items():
    x, y, z = n["x"], n["y"], height(n["x"], n["y"])
    tk_v[nid] = model.AddNewNode(main, f"V-{nid}", "QKON", x, y, z, 0, 1, n["street"], f"V-{nid}", 1)
    tk_r[nid] = model.AddNewNode(main, f"R-{nid}", "QKON", *rl(x, y), z, 0, 1, n["street"], f"R-{nid}", 2)
    model.SetValue(tk_v[nid], "Fk2lknot", tk_r[nid])  # links the supply node to its return node

# --- pipes: VL in flow direction away from the plant, RL towards the plant -----------------
tk_pipe_v, tk_pipe_r = {}, {}
for p in pipes:
    a, b = nodes[p["ki"]], nodes[p["kk"]]
    desc = f"{a['street'] or b['street']}"
    tk_pipe_v[p["id"]] = model.AddNewPipe(main, tk_v[p["ki"]], tk_v[p["kk"]], p["L"], "", p["table"], str(p["dn"]), 0.1, f"VL-{p['id']}", desc, 1)
    tk_pipe_r[p["id"]] = model.AddNewPipe(main, tk_r[p["kk"]], tk_r[p["ki"]], p["L"], "", p["table"], str(p["dn"]), 0.1, f"RL-{p['id']}", desc, 2)

# --- valves in the network -----------------------------------------------------------------
tk_valves = {}
for v in valves:
    a, b = nodes[v["ki"]], nodes[v["kk"]]
    xm, ym = (a["x"] + b["x"]) / 2, (a["y"] + b["y"]) / 2
    dn = max(p["dn"] for p in pipes if p["kk"] == v["ki"] or p["ki"] == v["kk"])
    tk_valves[f"VL-{v['id']}"] = model.AddNewConnectingElement(main, tk_v[v["ki"]], tk_v[v["kk"]], xm, ym, height(xm, ym), OT.Valve, float(dn), 1, 0, f"A-VL-{v['id']}", v["description"] + " VL")
    tk_valves[f"RL-{v['id']}"] = model.AddNewConnectingElement(main, tk_r[v["kk"]], tk_r[v["ki"]], *rl(xm, ym), height(xm, ym), OT.Valve, float(dn), 1, 0, f"A-RL-{v['id']}", v["description"] + " RL")

# --- consumers -----------------------------------------------------------------------------
tk_fwvb = {}
for c in consumers:
    n = nodes[c["node"]]
    tk = model.AddNewConnectingElement(main, tk_v[c["node"]], tk_r[c["node"]], n["x"] + 2, n["y"] - 2, height(n["x"], n["y"]),
                                       OT.DistrictHeatingConsumer, 32.0, 1, 0, f"FWVB-{c['id']}", c["description"])
    for prop, value in [("W0", c["w0"]), ("Tvl0", T_SUPPLY), ("Trs0", T_RETURN), ("Imbg", 0), ("bz.Fklfkt", lfkt[c["profile"]])]:
        model.SetValue(tk, prop, str(value))
    tk_fwvb[c["id"]] = tk

# --- heat plant: built in the main container, then moved into its own container ------------
z0 = height(0, 1000)
plant = {
    "R-HW": model.AddNewNode(main, "R-HW", "PKON", 20, 970, z0, 4.0, 1, "Druckhaltung Heizwerk", "R-HW", 2),
    "R-HW-P": model.AddNewNode(main, "R-HW-P", "QKON", 50, 970, z0, 0, 1, "Pumpendruckseite", "R-HW-P", 2),
    "R-HW-K": model.AddNewNode(main, "R-HW-K", "QKON", 70, 985, z0, 0, 1, "nach Rueckschlagklappe", "R-HW-K", 2),
    "V-HW": model.AddNewNode(main, "V-HW", "QKON", 70, 1000, z0, 0, 1, "Vorlauf Heizwerk", "V-HW", 1),
}
plant["P-1"] = model.AddNewConnectingElement(main, plant["R-HW"], plant["R-HW-P"], 35, 965, z0, OT.Pump, 200.0, 1, 0, "PUMPE-1", "Netzpumpe 1")
plant["P-2"] = model.AddNewConnectingElement(main, plant["R-HW"], plant["R-HW-P"], 35, 975, z0, OT.Pump, 200.0, 1, 0, "PUMPE-2", "Netzpumpe 2")
plant["KLAP"] = model.AddNewConnectingElement(main, plant["R-HW-P"], plant["R-HW-K"], 60, 978, z0, OT.FlapValve, 200.0, 1, 0, "KLAPPE-HW", "Rueckschlagklappe Pumpen")
plant["FWES"] = model.AddNewConnectingElement(main, plant["R-HW-K"], plant["V-HW"], 70, 992, z0, OT.DistrictHeatingFeeder, 200.0, 1, 0, "FWES-HW", "Heizkessel")
plant["A-VL"] = model.AddNewConnectingElement(main, plant["V-HW"], tk_v["HS-00"], 85, 1000, z0, OT.Valve, 200.0, 1, 0, "A-VL-HW", "Absperrschieber Heizwerk VL")
plant["A-RL"] = model.AddNewConnectingElement(main, tk_r["HS-00"], plant["R-HW"], 60, 960, z0, OT.Valve, 200.0, 1, 0, "A-RL-HW", "Absperrschieber Heizwerk RL")
model.SetValue(plant["V-HW"], "Fk2lknot", plant["R-HW-K"])
model.SetValue(plant["FWES"], "bz.Ithtyp", "3")  # supply temperature from table
model.SetValue(plant["FWES"], "bz.Fktevt", tevt)

heizwerk = model.InsertElement(OT.ObjectContainerSymbol, "HEIZWERK")
model.SetValue(heizwerk, "Name", "Heizwerk")
x1, y1, x2, y2 = HEIZWERK_SYMBOL
model.SetGeometryInformation(heizwerk, f"POLYGON(({x1} {y2}, {x2} {y2}, {x2} {y1}, {x1} {y1}, {x1} {y2}))")
for tk in plant.values():
    model.SetValue(tk, "Fkcont", heizwerk)
for node_id in ("HS-00",):  # the plant's boundary nodes stay in the main container, shown in the plant via VKNO
    for tk, (x, y) in ((tk_v[node_id], (100, 1000)), (tk_r[node_id], rl(100, 1000))):
        vkno = model.InsertElement(OT.BlockConnectionNode, "-1")
        for prop, value in [("Fkknot", tk), ("Fkcont", heizwerk), ("Pointinsertx", str(x)), ("Pointinserty", str(y))]:
            model.SetValue(vkno, prop, value)

# --- longitudinal sections (supply pipes from the plant; SIR 3S adds the return path) -------
def path_to(target):
    parent = {c["kk"]: (nid, c) for nid, cs in children.items() for c in cs}
    path, n = [], target
    while n in parent:
        n, edge = parent[n]
        path.append(edge)
    return [e["id"] for e in reversed(path) if "id" in e and e["id"] in tk_pipe_v]


for lfdnr, (agsn_id, name, target) in enumerate([("AGSN-KRANKENHAUS", "Heizwerk - Krankenhaus", "H-KRANKENHAUS"),
                                                  ("AGSN-SCHULE", "Heizwerk - Schule", "H-SCHULE")], start=1):
    agsn = model.InsertElement(OT.AGSN_HydraulicProfile, agsn_id)
    model.SetValue(agsn, "Name", name)
    model.SetValue(agsn, "Lfdnr", str(lfdnr))
    model.SetValue(agsn, "Aktiv", "101")
    path = path_to(target)  # first line: supply pipes, second line: the same path in the return
    model.SetValue(agsn, "ObjsString", "".join(f"\tROHR~{tk_pipe_v[pid]}" for pid in path) + "\n"
                   + "".join(f"\tROHR~{tk_pipe_r[pid]}" for pid in path))

# --- groups ----------------------------------------------------------------------------------
for lfdnr, (layr_id, name, kinds) in enumerate([("LAYR-HAUPTLEITUNG", "Hauptleitung", {"main"}),
                                                 ("LAYR-HAUSANSCHLUESSE", "Hausanschluesse", {"house"})], start=1):
    layr = model.InsertElement(OT.LAYR_Layer, layr_id)
    model.SetValue(layr, "Name", name)
    model.SetValue(layr, "Lfdnr", str(lfdnr))
    objs = [tk for p in pipes if p["kind"] in kinds for tk in (tk_pipe_v[p["id"]], tk_pipe_r[p["id"]])]
    model.SetValue(layr, "ObjsString", "".join(f"ROHR~{tk}\t" for tk in objs))

# --- thermal balance and time curves ------------------------------------------------------------
# The default thermal balance of a new model (whole network) is inactive.
wblz = model.GetTksofElementType(OT.WBLZ_ThermalBalance)[0]
model.SetValue(wblz, "Aktiv", "1")

# Time curves are data points (DPKT) of single elements in the data point group of the small output
# factor ("Internal02", Dtfak -1). The new model holds one generic data point (Name1 "*") per object
# type and result property, which we copy for the elements we want time curves of.
dp_groups = {model.GetValue(tk, "Name")[0]: tk for tk in model.GetTksofElementType(OT.DPGR_DataPointGroup)}
dp_generic = {}
for tk in model.GetTksofElementType(OT.DPKT_Datapoint):
    if model.GetValue(tk, "bz.Name1")[0] == "*":
        dp_generic[(model.GetValue(tk, "Objtype")[0], model.GetValue(tk, "Attrtype")[0])] = tk


def add_time_curve(element_tk, objtype, result_property):
    generic = dp_generic[(objtype, result_property)]
    dp = model.InsertElement(OT.DPKT_Datapoint, "-1")
    for prop in ("Objtype", "Attrtype", "Epkz", "Title", "Unit", "Description", "Datatype", "Datalength"):
        value = model.GetValue(generic, prop)[0]
        if value:
            model.SetValue(dp, prop, value)
    model.SetValue(dp, "Flags", str(int(model.GetValue(generic, "Flags")[0]) & ~4))  # bit 4: all elements of the type
    model.SetValue(dp, "bz.Fkobjtype", element_tk)
    model.SetValue(dp, "bz.Name1", model.GetValue(element_tk, "Name")[0])
    model.SetValue(dp, "bz.LowerLimit", "-1E+20")
    model.SetValue(dp, "bz.UpperLimit", "1E+20")
    link_datapoint(dp, "Internal02")


def link_datapoint(dp, group_name):
    link = model.InsertElement(OT.DPGR_DPKT_DatapointDpgrConnection, "-1")
    model.SetValue(link, "Fkdpgr", dp_groups[group_name])
    model.SetValue(link, "Fkdpkt", dp)


for prop in ("WES", "WVB", "WVERL"):
    add_time_curve(wblz, "WBLZ", prop)
for tk in (plant["V-HW"], plant["R-HW"], tk_v["H-KRANKENHAUS"], tk_r["H-KRANKENHAUS"]):
    add_time_curve(tk, "KNOT", "PH")
    add_time_curve(tk, "KNOT", "T")
add_time_curve(plant["P-1"], "PUMP", "QM")
add_time_curve(plant["FWES"], "FWES", "W")

# Longitudinal sections read their results via generic data points in group "Internal03". A new
# model lacks some of them; SirGraf reports "Datenpunkte fuer Laengsschnitte nicht gefunden" when
# opening the model and offers to add them. We add them here, with the metadata SirGraf uses.
# Entries with 2 values exist in a new model; the others are created:
# (Objtype, Attrtype, Epkz, Title, Unit, Flags, Datatype, Datalength, Description, Name2)
LS_DATAPOINTS = [
    ("DPRG", "QM"), ("DPRG", "V"), ("FWES", "QM"),
    ("FWES", "V", 4, "Strömungsgeschwindigkeit", "[m/s]", 37, "REAL", 4, "Strömungsgeschwindigkeit", "*"),
    ("KLAP", "QM"), ("KLAP", "V"), ("KNOT", "H"),
    ("KNOT", "HMAX_INST", None, "Druckhöhenmaximum instationär", "[IDPH,6]", 2165, "REAL", 4, "Größte Druckhöhe, die bis zum aktuellen Zeitpunkt aufgetreten ist", None),
    ("KNOT", "HMIN_INST", None, "Druckhöhenminimum instationär", "[IDPH,6]", 2165, "REAL", 4, "Kleinste Druckhöhe, die bis zum aktuellen Zeitpunkt aufgetreten ist", None),
    ("KNOT", "P"), ("KNOT", "PDAMPF"), ("KNOT", "PH"),
    ("KNOT", "PMAX_INST", None, "Druckmaximum instationär", "[bar,a]", 2165, "REAL", 4, "Größter Druck, der bis zum aktuellen Zeitpunkt aufgetreten ist", None),
    ("KNOT", "PMIN_INST", None, "Druckminimum instationär", "[bar,a]", 2165, "REAL", 4, "Kleinster Druck, der bis zum aktuellen Zeitpunkt aufgetreten ist", None),
    ("KNOT", "RHO"), ("KNOT", "T"), ("MREG", "QM"), ("MREG", "V"), ("PHTR", "QM"), ("PHTR", "V"),
    ("PREG", "QM"), ("PREG", "V"), ("PUMP", "QM"), ("REGV", "QM"), ("REGV", "V"), ("ROHR", "JV"),
    ("ROHR", "MVEC", None, "Massenströme Rohrgitter", "[kg/s]", 33013, "RVEC", 4, "Massenströme Rohrgitter, Datenblock ist ein Vektor", "*"),
    ("ROHR", "PVEC", None, "Drücke Rohrgitter", "[bar,a]", 245, "RVEC", 4, "Drücke Rohrgitter, Datenblock ist ein Vektor", "*"),
    ("ROHR", "PVECMAX_INST", None, "Druckmaxima Rohrgitter instationär", "[bar,a]", 117, "RVEC", 4, "Größte Drücke auf dem Rohrgitter, die bis zum aktuellen Zeitpunkt aufgetreten sind, Datenblock ist ein Vektor", "*"),
    ("ROHR", "PVECMIN_INST", None, "Druckminima Rohrgitter instationär", "[bar,a]", 117, "RVEC", 4, "Kleinste Drücke auf dem Rohrgitter, die bis zum aktuellen Zeitpunkt aufgetreten sind, Datenblock ist ein Vektor", "*"),
    ("ROHR", "QMAV"),
    ("ROHR", "QMI", 2, "Durchfluss Knoten I", "[IDQM]", 37109, "REAL", 4, "Durchfluss am Rohranfang (Knoten I)", "*"),
    ("ROHR", "QMK", 256, "Durchfluss Knoten K", "[IDQM]", 37109, "REAL", 4, "Durchfluss am Rohrende (Knoten K)", "*"),
    ("ROHR", "RHOVEC", None, "Dichten Rohrgitter", "[kg/m3]", 245, "RVEC", 4, "Dichten Rohrgitter, Datenblock ist ein Vektor", "*"),
    ("ROHR", "SVEC", None, "Weglängen Rohrgitter", "[m]", 245, "RVEC", 4, "Weglängen Rohrgitter, Datenblock ist ein Vektor", "*"),
    ("ROHR", "TVEC", None, "Temperaturen Rohrgitter", "[°C]", 245, "RVEC", 4, "Temperaturen Rohrgitter, Datenblock ist ein Vektor", "*"),
    ("ROHR", "VAV"),
    ("ROHR", "VI", 4, "Strömungsgeschwindigkeit Knoten I", "[m/s]", 37109, "REAL", 4, "Strömungsgeschwindigkeit am Rohranfang (Knoten I)", "*"),
    ("ROHR", "VK", 512, "Strömungsgeschwindigkeit Knoten K", "[m/s]", 37109, "REAL", 4, "Strömungsgeschwindigkeit Rohrende (Knoten K)", "*"),
    ("ROHR", "ZVEC", None, "Geodätische Höhen Rohrgitter", "[m]", 245, "RVEC", 4, "Geodätische Höhen Rohrgitter, Datenblock ist ein Vektor", "*"),
    ("ROHR_VRTX", "H", None, "Druckhöhe", "[IDPH,6]", 245, "REAL", 4, "Druckhöhe", None),
    ("ROHR_VRTX", "M", None, "Massenstrom", "[kg/s]", 33013, "REAL", 4, "Massenstrom", "*"),
    ("ROHR_VRTX", "P", None, "Druck", "[bar,a]", 245, "REAL", 4, "Druck", "*"),
    ("ROHR_VRTX", "PMAX_INST", None, "Druckmaximum instationär", "[bar,a]", 117, "REAL", 4, "Größter Druck, der bis zum aktuellen Zeitpunkt aufgetreten ist", "*"),
    ("ROHR_VRTX", "PMIN_INST", None, "Druckminimum instationär", "[bar,a]", 117, "REAL", 4, "Kleinster Druck, der bis zum aktuellen Zeitpunkt aufgetreten ist", "*"),
    ("ROHR_VRTX", "RHO", None, "Dichte", "[kg/m3]", 245, "REAL", 4, "Dichte", "*"),
    ("ROHR_VRTX", "T", None, "Temperatur", "[°C]", 245, "REAL", 4, "Temperatur", "*"),
    ("SIVE", "QM"), ("SIVE", "V"), ("VENT", "QM"), ("VENT", "V"),
]
LS_LIMITS = {("ROHR", "RHOVEC"): ("0.001", "12000"), ("ROHR_VRTX", "RHO"): ("0.001", "12000"),
             ("ROHR", "TVEC"): ("-150", "550"), ("ROHR_VRTX", "T"): ("-150", "550")}  # default: +-1E+20
for entry in LS_DATAPOINTS:
    dp = dp_generic.get(entry[:2])
    if dp is None:
        if len(entry) == 2:
            raise RuntimeError(f"Generic data point {entry} missing in the new model")
        objtype, attrtype, epkz, title, unit, flags, datatype, datalength, description, name2 = entry
        lower, upper = LS_LIMITS.get(entry[:2], ("-1E+20", "1E+20"))
        dp = model.InsertElement(OT.DPKT_Datapoint, "-1")
        for prop, value in [("Objtype", objtype), ("Attrtype", attrtype), ("Epkz", epkz), ("Title", title), ("Unit", unit),
                            ("Flags", flags), ("Datatype", datatype), ("Datalength", datalength), ("Description", description),
                            ("bz.Name1", "*"), ("bz.Name2", name2), ("bz.Fkobjtype", "-1"), ("bz.Factor", 1),
                            ("bz.LowerLimit", lower), ("bz.UpperLimit", upper)]:
            if value is not None:
                model.SetValue(dp, prop, str(value))
    link_datapoint(dp, "Internal03")

# --- calculation settings ---------------------------------------------------------------------
model.SetCalculationType(model.CalculationType.Quasi_Stat)
model.SetSimulationTimeFrame(3600.0, 86400.0)
general = model.GetTksofElementType(OT.GeneralSection)[0]
model.SetValue(general, "bz.Cdat", "15.01.2026")
model.SetValue(general, "bz.Cuhr", "00:00:00")

model.EndEditSession()
model.SaveChanges()
model.CloseModel(True)

# Settings the Toolkit API does not expose (or does not write correctly) are set in the database:
# - output factors small/large (table TIMD)
# - drawing area (grid) of the views and the position of the block symbol: binary GRAF field of
#   CONT_BZ (setting Xkor/Ykor of a container via the Toolkit does not update it reliably, and
#   SetGeometryInformation not at all - SirGraf draws the block symbol from GRAF).
GRAF_SYMBOL, GRAF_VIEW, GRAF_SHEET, GRAF_SIZE = 8, 76, 116, 148  # byte offsets of the double values


def patch_graf(con, container_name, sheet, symbol=None):
    """sheet/symbol: (xmin, ymin, xmax, ymax). The symbol rectangle is stored as (x1, y top, x2, y bottom)."""
    graf = bytearray(con.execute("SELECT b.GRAF FROM CONT c JOIN CONT_BZ b ON b.fk=c.pk WHERE c.NAME=?", (container_name,)).fetchone()[0])
    xmin, ymin, xmax, ymax = sheet
    graf[GRAF_VIEW:GRAF_VIEW + 32] = struct.pack("<4d", xmin, ymin, xmax, ymax)
    graf[GRAF_SHEET:GRAF_SHEET + 32] = struct.pack("<4d", xmin, ymin, xmax, ymax)
    graf[GRAF_SIZE:GRAF_SIZE + 16] = struct.pack("<2d", xmax - xmin, ymax - ymin)
    if symbol:
        graf[GRAF_SYMBOL:GRAF_SYMBOL + 32] = struct.pack("<4d", symbol[0], symbol[3], symbol[2], symbol[1])
    con.execute("UPDATE CONT_BZ SET GRAF=? WHERE fk=(SELECT pk FROM CONT WHERE NAME=?)", (bytes(graf), container_name))
    return bytes(graf)


xs = [n["x"] + dx for n in nodes.values() for dx in (0, RL_OFFSET[0])]
ys = [n["y"] + dy for n in nodes.values() for dy in (0, RL_OFFSET[1])]
MAIN_SHEET = (math.floor(min(xs) / 100) * 100 - 100, math.floor(min(ys) / 100) * 100 - 100,
              math.ceil(max(xs) / 100) * 100 + 100, math.ceil(max(ys) / 100) * 100 + 100)
with sqlite3.connect(DB_FILE) as con:
    con.execute("UPDATE TIMD SET DTFAK_KLEIN=1, DTFAK_GROSS=2 WHERE pk<>'-1'")
    main_name = con.execute("SELECT NAME FROM CONT WHERE ID=1001").fetchone()[0]
    expected_graf = {main_name: patch_graf(con, main_name, MAIN_SHEET),
                     "Heizwerk": patch_graf(con, "Heizwerk", HEIZWERK_SHEET, HEIZWERK_SYMBOL)}

# ---------------------------------------------------------------------------------------------
# Calculate once, so the model is shipped with results
# ---------------------------------------------------------------------------------------------
model.OpenModel(dbName=DB_FILE, providerType=model.ProviderTypes.SQLite, Mid="M-1-0-1", saveCurrentlyOpenModel=False,
                namedInstance="", userID="", password="")
model.ExecCalculation(True)
model.CloseModel(False)
with sqlite3.connect(DB_FILE) as con:
    for name, graf in expected_graf.items():
        stored = con.execute("SELECT b.GRAF FROM CONT c JOIN CONT_BZ b ON b.fk=c.pk WHERE c.NAME=?", (name,)).fetchone()[0]
        if stored != graf:
            print(f"WARNING: drawing area/symbol of container '{name}' was changed after patching it.")
print(f"Network 3 written to {DB_FILE}")
